from aiogram.fsm.state import StatesGroup, State

class GetFileId(StatesGroup):
    MEDIA = State()