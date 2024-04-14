from aiogram import Dispatcher, Bot, F
from aiogram.enums import ContentType
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from loguru import logger

from bot.database.models import User
from bot.keyboards.inline import get_gpt_helper_btn, get_task_btn
from bot.keyboards.reply import btn_menu
from bot.misc.util import langs, ALL_KEYBOARD


def register_user_handlers(dp: Dispatcher):
    # todo: register all user handlers
    dp.message.register(cmd_start_handler, CommandStart())
    dp.message.register(get_text, F.content_type == ContentType.TEXT)


async def cmd_start_handler(msg: Message, bot: Bot) -> None:  # Пользователь нажал на старт
    user = User(msg.from_user.id)
    await btn_menu(user, langs[user.language()]["start_msg"], bot)
    if user.is_new():
        parameters = {
            'username': msg.from_user.username,
            'first_name': msg.from_user.first_name,
            'last_name': msg.from_user.last_name,
            'language': msg.from_user.language_code
        }
        user.add_user(parameters)
        # await msg.answer(langs[user.language()]["start_msg_new"])
    # else:
    #     await msg.answer(langs[user.language()]["start_msg_old"])


async def handlers_keyboard(my_user, m_text, bot: Bot):
    if m_text == langs[my_user.language()]["main_btn_gpt_helper"]:
        logger.info(f"{my_user} handlers_keyboard_main_btn_gpt_helper")
        builder = get_gpt_helper_btn(my_user.language())
        await bot.send_message(my_user.u_id, langs[my_user.language()]["text_upper_all_modes_gpt_helper"], reply_markup=builder.as_markup())
    elif m_text == langs[my_user.language()]["main_btn_task_scheduler"]:
        logger.info(f"{my_user} handlers_keyboard_main_btn_task_scheduler")
        builder = get_task_btn(my_user.language())
        await bot.send_message(my_user.u_id, langs[my_user.language()]["text_upper_all_modes_task_scheduler"], reply_markup=builder.as_markup())




# @bot_bug_catcher_msg_bot_state
async def get_text(msg:Message, bot: Bot):
    m_text = msg.text
    user = User(msg.from_user.id)
    if m_text in ALL_KEYBOARD:
        await handlers_keyboard(user, m_text, bot)
        return
    await msg.answer(langs[user.language()]["unknown_request"])
