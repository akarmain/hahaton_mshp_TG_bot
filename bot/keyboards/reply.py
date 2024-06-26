from aiogram import Bot
from aiogram.types import KeyboardButton
from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.keyboards import *
from bot.misc.util import langs


async def btn_menu(user, text_menu, bot: Bot):
    # Создание кнопок
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text=langs[user.language()]["main_btn_gpt_helper"])
    )

    builder.row(
        KeyboardButton(text=langs[user.language()]["main_btn_task_scheduler"])
    )

    builder.row(
        KeyboardButton(text=langs[user.language()]["btn_detailed_settings"], web_app=WebAppInfo(url="https://jocular-mooncake-3eb52e.netlify.app/home")) # ссылка на webApp
    )

    await bot.send_message(user.u_id, text_menu, reply_markup=builder.as_markup(resize_keyboard=True))


def btn_leave_assistant(user_lang: str):
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text=langs[user_lang]["main_btn_leave_assistant"])
    )
    return builder
