import pathlib
import sys

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import bot.utils.all_state as my_states

script_dir = pathlib.Path(sys.argv[0]).parent
PATH_USER_PHOTO = str(script_dir / 'bot/media/cash/from_user_{}_photo.jpg')


def register_all_state(dp: Dispatcher) -> None:
    dp.message.register(example_state, my_states.TestStates.TEST)


async def example_state(msg: Message, bot: Bot, state: FSMContext):
    # await state.set_state(my_states.TestStates.TEST) задать новый State

    await state.update_data(TEST=msg.text)
    user_data = await state.get_data()
    test = user_data["TEST"]
    await state.clear()
    await msg.answer(test)
