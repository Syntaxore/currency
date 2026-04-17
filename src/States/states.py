from aiogram.fsm.state import StatesGroup, State

class UserData(StatesGroup):
    data = State()
    