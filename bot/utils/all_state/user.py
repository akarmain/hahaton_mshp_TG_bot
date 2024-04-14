from aiogram.fsm.state import StatesGroup, State

class GptHelperBtnExplain(StatesGroup):
    CONTEXT = State()
    DATA = State()


class GptHelperBtnPickMaterials(StatesGroup):
    CONTEXT = State()
    DATA = State()


class GptHelperBtnCodeHelp(StatesGroup):
    CONTEXT = State()
    DATA = State()


class GptHelperBtnMakeSynopsis(StatesGroup):
    CONTEXT = State()
    DATA = State()


class Tag(StatesGroup):
    NAME = State()

class Task(StatesGroup):
    TITLE = State()
    DESCRIPTION = State()
    TIME_OVER = State()
    COMPLEXITY = State()
