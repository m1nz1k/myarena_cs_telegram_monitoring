from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from utils.db_api import quick_commands as commands


class IsDatabaseUser(BoundFilter):
    """
    Первый вариант
    """
    async def check(self, message: types.Message):
        user = await commands.select_user(message.from_user.id)
        if user:
            return True
        else:
            return False