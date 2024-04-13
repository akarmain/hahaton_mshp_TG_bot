import pathlib
import sys

from aiogram import Dispatcher
from aiogram import F, Bot
from aiogram.types import ContentType
from aiogram.types import Message

import bot.utils.all_state as my_states
from bot.database.models.user import MyUser
from bot.keyboards.inline import example_inline_builder
from bot.misc.util import langs, ALL_KEYBOARD
from bot.utils.utils import uploading_photos

script_dir = pathlib.Path(sys.argv[0]).parent
PATH_USER_PHOTO = str(script_dir / 'bot/media/cash/from_user_{}_photo.jpg')


def register_all_media(dp: Dispatcher) -> None:
    dp.message.register(get_text, F.content_type == ContentType.TEXT)
    dp.message.register(get_photo, F.content_type == ContentType.PHOTO)


async def handlers_keyboards(my_user, m_text, bot: Bot, state: my_states.FSMContext):  # , state: FSMContext
    if m_text == langs[my_user.language]["reply_keyboards_test_1"]:
        await bot.send_message(my_user.u_id, langs[my_user.language]["reply_keyboards_test_3"])
    elif m_text == langs[my_user.language]["reply_keyboards_test_2"]:
        await bot.send_message(my_user.u_id, langs[my_user.language]["reply_keyboards_test_2"])
        await state.set_state(my_states.TestStates.TEST.state)
    elif m_text == langs[my_user.language]["reply_keyboards_test_3"]:
        await bot.send_message(my_user.u_id, langs[my_user.language]["reply_keyboards_test_1"], reply_markup=example_inline_builder(my_user).as_markup())


async def get_text(msg: Message, bot: Bot, state: my_states.FSMContext):
    # Обработка пользовательского текста
    m_text = msg.text
    my_user = MyUser(msg.from_user.id)
    if m_text in ALL_KEYBOARD:
        await handlers_keyboards(my_user, m_text, bot, state)
        return
    await msg.answer(m_text)


async def get_photo(msg: Message, bot: Bot):
    # Обрабатывает фото и сохраняет изображение в cash
    my_user = MyUser(msg.from_user.id)
    path_user_photo = await uploading_photos(my_user, msg, bot)
    await msg.answer(f"{path_user_photo}")
