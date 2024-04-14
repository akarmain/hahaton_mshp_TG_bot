from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.misc.util import langs


def get_gpt_helper_btn(user_rang: str):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text=langs[user_rang]["text_lower_all_modes_gpt_helper_btn_explain"],
        callback_data=f"gpt_helper_btn_explain"))
    builder.add(InlineKeyboardButton(
        text=langs[user_rang]["text_lower_all_modes_gpt_helper_btn_pick_materials"],
        callback_data=f"gpt_helper_btn_pick_materials"))
    builder.add(InlineKeyboardButton(
        text=langs[user_rang]["text_lower_all_modes_gpt_helper_btn_code_help"],
        callback_data=f"gpt_helper_btn_code_help"))
    builder.add(InlineKeyboardButton(
        text=langs[user_rang]["text_lower_all_modes_gpt_helper_btn_make_synopsis"],
        callback_data=f"gpt_helper_btn_make_synopsis"))
    builder.adjust(1)

    return builder
