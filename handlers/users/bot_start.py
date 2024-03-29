from aiogram import types
from loader import dp
from filters import IsPrivate, IsDatabaseUser
from keyboards.inline import server_menu
from utils.db_api import quick_commands as commands
from utils.misc import rate_limit
from data.config import admins

@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), text='/start', chat_id=admins)
async def command_start(message: types.Message):

    if await IsDatabaseUser().check(message):
        await message.answer('Привет! Я бот для мониторинга и управления сервером на проекте MyArena.',
                             reply_markup=server_menu)
    else:
        await commands.add_user(
            user_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            active_token=None,
        )
        await message.answer('Привет! Я бот для мониторинга и управления сервером на проекте MyArena.',
                             reply_markup=server_menu)