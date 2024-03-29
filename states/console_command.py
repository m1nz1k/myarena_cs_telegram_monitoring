from aiogram.dispatcher.filters.state import StatesGroup, State


class ConsoleInput(StatesGroup):
    waiting_for_command  = State()
