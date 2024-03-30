from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from utils.db_api import server_commands, quick_commands
from keyboards.inline import server_menu, server_list_menu
from utils.misc import (
    server_monitoring,
    get_maps,
    map_change,
    start_server,
    stop_server,
    restart_server,
    console_send,
    is_valid_token
)

from states import ConsoleInput, ServerAddStates
from aiogram.types import ParseMode



@dp.callback_query_handler(text_contains='server_monitoring')
async def server_check(callback_query: types.CallbackQuery):

    await callback_query.message.edit_text('Выполняю запрос.📨 Пожалуйста, подождите! ⏳',
                                           reply_markup=server_menu)

    status = await server_monitoring(await quick_commands.get_user_active_token(callback_query.from_user.id))
    if status:
        await callback_query.message.edit_text(f'''
🏷️ <b>Название сервера:</b> {status['name']}
📌 <b>Тип сервера:</b> {status['server_type']}                                            
🌍 <b>Адрес сервера:</b> <code>{status['server_address']}</code>
📍 <b>Локация сервера:</b> {status['server_location']}                                                                                         
📡 <b>Статус сервера:</b> {status['online']}
🗺️ <b>Карта:</b> {status['map']}
👥 <b>Онлайн игроков:</b> {status['players']}/{status['playersmax']}                                            
⏳ <b>Осталось дней аренды:</b> {status['server_daystoblock']}                                                                                                                              
''',
parse_mode=ParseMode.HTML,
reply_markup=server_menu)
        
    else:
        await callback_query.message.edit_text('❌Запрос не прошел.',
                                               reply_markup=server_menu)
        

@dp.callback_query_handler(text_contains='server_change_map')
async def map_change_callback(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Выполняю запрос.📨 Пожалуйста, подождите! ⏳',
                                           reply_markup=server_menu)
    maps_list = await get_maps(await quick_commands.get_user_active_token(callback_query.from_user.id))
    if maps_list:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        for map_name in maps_list:
            callback_data = f"map|{map_name}"
            keyboard.add(types.InlineKeyboardButton(map_name, 
                                                    callback_data=callback_data))
        
        await callback_query.message.edit_text('🗺️Выберите карту:', 
                                               reply_markup=keyboard)
    else:
        await callback_query.message.edit_text('❌Запрос не прошел.', 
                                               reply_markup=server_menu)

@dp.callback_query_handler(text_contains='map|')
async def handle_map_selection(callback_query: types.CallbackQuery):
    map_name = callback_query.data.split('|')[1]
    await map_change(map_name, await quick_commands.get_user_active_token(callback_query.from_user.id))
    await callback_query.message.edit_text(f'✅Карта {map_name} успешно изменена!', 
                                           reply_markup=server_menu)

@dp.callback_query_handler(text_contains='server_start')
async def server_start(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Выполняю запрос.📨 Пожалуйста, подождите! ⏳',
                                           reply_markup=server_menu)
    status = await start_server(await quick_commands.get_user_active_token(callback_query.from_user.id))

    if status:       
        await callback_query.message.edit_text('✅Сервер успешно запущен!', 
                                               reply_markup=server_menu)
    else:
        await callback_query.message.edit_text('❌Запрос не прошел.', 
                                               reply_markup=server_menu)

@dp.callback_query_handler(text_contains='server_stop')
async def server_stop(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Выполняю запрос.📨 Пожалуйста, подождите! ⏳',
                                           reply_markup=server_menu)
    status = await stop_server(await quick_commands.get_user_active_token(callback_query.from_user.id))
    if status:       
        await callback_query.message.edit_text('✅Сервер успешно остановлен!', 
                                               reply_markup=server_menu)
    else:
        await callback_query.message.edit_text('❌Запрос не прошел.', 
                                               reply_markup=server_menu)


@dp.callback_query_handler(text_contains='server_restart')
async def server_restart(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Выполняю запрос.📨 Пожалуйста, подождите! ⏳',
                                           reply_markup=server_menu)
    status = await restart_server(await quick_commands.get_user_active_token(callback_query.from_user.id))
    if status:       
        await callback_query.message.edit_text('✅Сервер успешно перезапущен!', 
                                               reply_markup=server_menu)
    else:
        await callback_query.message.edit_text('❌Запрос не прошел.', 
                                               reply_markup=server_menu)


@dp.callback_query_handler(text_contains='server_send_console')
async def server_send(callback_query: types.CallbackQuery, state: FSMContext):
    original_message = await callback_query.message.edit_text('Введите команду:', 
                                                              reply_markup=server_menu)
    await state.update_data(original_message=original_message)
    await ConsoleInput.waiting_for_command.set()

@dp.message_handler(state=ConsoleInput.waiting_for_command)
async def process_command(message: types.Message, state: FSMContext):
    data = await state.get_data()
    original_message = data['original_message']
    chat_id = original_message['chat']['id']
    message_id = original_message['message_id']
    
    await bot.edit_message_text(chat_id=chat_id, 
                                message_id=message_id, 
                                text=f'Выполняю запрос.📨 Пожалуйста, подождите! ⏳', 
                                reply_markup=server_menu)
    command = message.text
    await dp.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await state.finish() 
    status = await console_send(command, await quick_commands.get_user_active_token(message.from_user.id))
    if status:       
       await bot.edit_message_text(chat_id=chat_id, 
                                   message_id=message_id, 
                                   text=f'✅Комманда "{command}" успешно отправлена!', 
                                   reply_markup=server_menu)
    else:
      await bot.edit_message_text(chat_id=chat_id, 
                                  message_id=message_id, 
                                  text='❌Запрос не прошел.', 
                                  reply_markup=server_menu)
      


@dp.callback_query_handler(text_contains='server_list')
async def servers_menu(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('⚠️ Здесь вы можете выбрать, добавить или удалить сервер',
                                           reply_markup=server_list_menu)

@dp.callback_query_handler(text_contains='server_add')
async def server_add_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.edit_text('🟢 Введите токен сервера:', reply_markup=server_list_menu)

    await state.update_data(original_chat_id=callback_query.message.chat.id, original_message_id=callback_query.message.message_id)
    await ServerAddStates.WaitingForToken.set()

@dp.message_handler(state=ServerAddStates.WaitingForToken)
async def process_server_token(message: types.Message, state: FSMContext):
    await dp.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

    data = await state.get_data()
    chat_id = data['original_chat_id']
    message_id = data['original_message_id']


    if not await is_valid_token(message.text):
        await message.bot.edit_message_text(chat_id=chat_id,
                                            message_id=message_id,
                                            text='❌ Введенный токен недействителен. Пожалуйста, повторите попытку!',
                                            reply_markup=server_list_menu)
        await state.finish()
        return
    await state.update_data(token=message.text)

    await message.bot.edit_message_text(chat_id=chat_id,
                                        message_id=message_id,
                                        text='🟢 Теперь введите название сервера, которое будет отображаться в телеграме!',
                                        reply_markup=server_list_menu)
    await ServerAddStates.WaitingForName.set()


@dp.message_handler(state=ServerAddStates.WaitingForName)
async def process_server_name(message: types.Message, state: FSMContext):
    await dp.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    
    data = await state.get_data()
    chat_id = data['original_chat_id']
    message_id = data['original_message_id']
    token = data.get('token')


    if await server_commands.create_server(server_token=token, server_name=message.text):
        await message.bot.edit_message_text(chat_id=chat_id,
                                            message_id=message_id,
                                            text='✅ Информация о сервере успешно сохранена.',
                                            reply_markup=server_list_menu)
    else:
        await message.bot.edit_message_text(chat_id=chat_id,
                                            message_id=message_id,
                                            text='❌ Информация не сохранилась.',
                                            reply_markup=server_list_menu)

    await state.finish()


# создание инлайн кнопок для серверов из БД
async def get_servers_inline_keyboard(user_id: int):
    servers = await server_commands.get_all_servers()
    user = await quick_commands.get_user_by_id(user_id)
    active_token = user.active_token if user else None

    inline_keyboard = []
    for server in servers:
        button_text = server.server_name

        if active_token == server.server_token:
            button_text = "🟢" + button_text
        inline_keyboard.append([types.InlineKeyboardButton(text=button_text, callback_data=f"server_select_{server.server_token}")])

    inline_keyboard.append([types.InlineKeyboardButton(text="Назад в меню", callback_data="back_to_menu")])

    return types.InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


# выбор сервера
@dp.callback_query_handler(lambda query: query.data == 'select_server')
async def process_select_server(callback_query: types.CallbackQuery):
    await send_servers_list(callback_query.message, callback_query.from_user.id)

# функция для отправки сообщения с инлайн клавиатурой выбора сервера
async def send_servers_list(message: types.Message, user_id: int):
    inline_keyboard = await get_servers_inline_keyboard(user_id)
    await bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text="Выберите сервер:", reply_markup=inline_keyboard)


# обработчик для инлайн кнопок выбора сервера
@dp.callback_query_handler(lambda query: query.data.startswith('server_select'))
async def process_server_select(callback_query: types.CallbackQuery):

    server_token = callback_query.data.split('_')[2]

    await quick_commands.update_user_active_token(callback_query.from_user.id, server_token)

    await send_servers_list(callback_query.message, callback_query.from_user.id)


# обработчик для кнопки "Назад в меню"
@dp.callback_query_handler(lambda query: query.data == 'back_to_menu')
async def process_back_to_menu(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, 
                                message_id=callback_query.message.message_id, 
                                text="Привет! Я бот для мониторинга и управления сервером на проекте MyArena.",
                                reply_markup=server_menu)
    

# функция для создания инлайн клавиатуры с кнопками для удаления серверов
async def get_delete_server_inline_keyboard():
    servers = await server_commands.get_all_servers()

    inline_keyboard = []
    for server in servers:
        button_text = f"Удалить {server.server_name}"
        inline_keyboard.append([types.InlineKeyboardButton(text=button_text, callback_data=f"db_del_{server.server_token}")])

    inline_keyboard.append([types.InlineKeyboardButton(text="Назад в меню", callback_data="back_to_menu")])

    return types.InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

# обработчик для инлайн кнопки server_del
@dp.callback_query_handler(text_contains='server_del')
async def process_server_delete(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    delete_servers_keyboard = await get_delete_server_inline_keyboard()
    
    if not delete_servers_keyboard.inline_keyboard:
        await bot.edit_message_text(chat_id=user_id, 
                                    message_id=callback_query.message.message_id,
                                    text="Список серверов пуст.",
                                    reply_markup=server_list_menu)
        return

    await bot.edit_message_text(chat_id=user_id, 
                                message_id=callback_query.message.message_id,
                                text="Выберите сервер для удаления:", 
                                reply_markup=delete_servers_keyboard)

# обработчик для выбора сервера для удаления
@dp.callback_query_handler(lambda query: query.data.startswith('db_del_'))
async def process_server_delete_confirm(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    server_token = callback_query.data.split('_')[2]
    

    try:
        deleted = await server_commands.delete_server(server_token)
        if deleted:
            await bot.edit_message_text(chat_id=user_id, 
                                        message_id=callback_query.message.message_id,
                                        text=f"✅ Сервер успешно удален.",
                                        reply_markup=server_menu)
        else:
            await bot.edit_message_text(chat_id=user_id, 
                                        message_id=callback_query.message.message_id,
                                        text=f"❌ Сервер не найден.",
                                        reply_markup=server_menu)
    except Exception as e:
        await bot.edit_message_text(chat_id=user_id, 
                                    message_id=callback_query.message.message_id,
                                    text=f"❌ Ошибка при удалении сервера: {e}",
                                    reply_markup=server_menu)