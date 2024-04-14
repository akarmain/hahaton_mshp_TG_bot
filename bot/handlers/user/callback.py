from aiogram import Dispatcher
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile
from loguru import logger

import bot.database as bd
from bot.database.models import User
from bot.keyboards.reply import btn_leave_assistant
from bot.misc.util import langs
from bot.utils.all_state.user import GptHelperBtnExplain, GptHelperBtnPickMaterials, GptHelperBtnCodeHelp, GptHelperBtnMakeSynopsis


def register_callback_handlers(dp: Dispatcher):
    # todo: register all callback handlers
    # Пользователь нажал на старт c deep_linking с ref_url
    dp.callback_query.register(callback_helper_btn_explain, F.data == "gpt_helper_btn_explain")
    dp.callback_query.register(callback_helper_btn_pick_materials, F.data.startswith("gpt_helper_btn_pick_materials"))
    dp.callback_query.register(callback_helper_btn_code_help, F.data.startswith("gpt_helper_btn_code_help"))
    dp.callback_query.register(callback_helper_btn_make_synopsis, F.data.startswith("gpt_helper_btn_make_synopsis"))


async def callback_helper_btn_explain(call: CallbackQuery, state: FSMContext):
    logger.info("callback_helper_btn_explain")
    my_user = User(call.from_user.id)
    builder = btn_leave_assistant(my_user.language())
    await call.bot.send_message(my_user.u_id, langs[my_user.language()]["mode_enabled_gpt_helper_explain"], reply_markup = builder.as_markup(resize_keyboard=True))
    await state.set_state(GptHelperBtnExplain.DATA.state)


async def callback_helper_btn_pick_materials(call: CallbackQuery, state: FSMContext):
    logger.info("callback_helper_btn_pick_materials")
    user = User(call.from_user.id)
    builder = btn_leave_assistant(user.language())
    await call.bot.send_message(user.u_id, langs[user.language()]["mode_enabled_gpt_helper_pick_materials"], reply_markup = builder.as_markup(resize_keyboard=True))
    await state.set_state(GptHelperBtnPickMaterials.DATA.state)


async def callback_helper_btn_code_help(call: CallbackQuery, state: FSMContext):
    logger.info("callback_helper_btn_pick_materials")
    user = User(call.from_user.id)
    builder = btn_leave_assistant(user.language())
    await call.bot.send_message(user.u_id, langs[user.language()]["mode_enabled_gpt_helper_code_help"], reply_markup = builder.as_markup(resize_keyboard=True))
    await state.set_state(GptHelperBtnCodeHelp.DATA.state)


async def callback_helper_btn_make_synopsis(call: CallbackQuery, state: FSMContext):
    logger.info("callback_helper_btn_pick_materials")
    user = User(call.from_user.id)
    builder = btn_leave_assistant(user.language())
    await call.bot.send_message(user.u_id, langs[user.language()]["mode_enabled_gpt_helper_make_synopsis"], reply_markup = builder.as_markup(resize_keyboard=True))
    await state.set_state(GptHelperBtnMakeSynopsis.DATA.state)
