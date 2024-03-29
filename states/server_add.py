from aiogram.dispatcher.filters.state import StatesGroup, State


class ServerAddStates(StatesGroup):
    WaitingForToken = State()
    WaitingForName = State()