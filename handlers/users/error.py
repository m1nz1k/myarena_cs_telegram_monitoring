# Обработчик несуществующих комманд и сообщений. В __init__ всегда должен стоять последним!

from aiogram import types
from loader import dp

@dp.message_handler()
async def command_error(message: types.Message):
    await message.answer(f'Команда {message.text} не найдена.')