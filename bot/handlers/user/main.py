from aiogram import Dispatcher
from aiogram import F, Bot
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.database.methods.get import in_db_dl
from bot.database.models.user import *
from bot.keyboards.reply import menu
from bot.misc.util import langs


def register_user_handlers(dp: Dispatcher):
    # todo: register all user handlers
    # Пользователь нажал на старт c deep_linking c шаблоном для QR
    dp.message.register(cmd_start_handler_deep_linking, CommandStart(deep_link=True),
                        F.text.startswith("/start deep"))

    # Пользователь нажал на старт c deep_linking с ref_url
    dp.message.register(cmd_start_handler_deep_linking_ref, CommandStart(deep_link=True))

    # Пользователь нажал на старт без deep_linking
    dp.message.register(cmd_start_handler, CommandStart())


async def cmd_start_handler(msg: Message, bot: Bot) -> None:  # Пользователь нажал на старт без deep_linking
    my_user = MyUser(msg.from_user.id)
    if my_user.is_new:
        await reg_new_user(my_user, msg.from_user, bot)
        await bot.send_message(my_user.u_id, "Ты теперь смешарик")
        return
    await menu(my_user, langs[my_user.language]["cmd_start_already_using_bot"], bot)


async def cmd_start_handler_deep_linking(msg: Message, bot: Bot, state: FSMContext):
    # Пользователь нажал на старт c deep_linking c шаблоном на deep
    my_user = MyUser(msg.from_user.id)
    deep = msg.text.split()[1]

    match deep:
        case deep:
            await msg.answer(deep)
            # await reg_qr_template_url(my_user, msg, state)


async def cmd_start_handler_deep_linking_ref(msg: Message, bot: Bot):
    # Пользователь нажал на старт c deep_linking с ref_url
    my_user = MyUser(msg.from_user.id)
    deep_linking = msg.text.split()[1]
    if my_user.is_new and in_db_dl(deep_linking):
        await reg_new_user(my_user, bot, deep_linking)
    await menu(my_user, langs[my_user.language]["cmd_start_already_using_bot"], bot)






