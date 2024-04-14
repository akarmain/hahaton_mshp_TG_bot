from aiogram import Dispatcher
from aiogram import F
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from loguru import logger

from bot.database.models import User
from bot.database.models.tags import Tags
from bot.database.models.task import Tasks
from bot.keyboards.reply import btn_leave_assistant
from bot.misc.util import langs
from bot.utils.all_state.user import GptHelperBtnExplain, GptHelperBtnPickMaterials, GptHelperBtnCodeHelp, GptHelperBtnMakeSynopsis, Tag, Task


def register_callback_handlers(dp: Dispatcher):
    # todo: register all callback handlers
    # gpt_helper
    dp.callback_query.register(callback_helper_btn_explain, F.data == "gpt_helper_btn_explain")
    dp.callback_query.register(callback_helper_btn_pick_materials, F.data.startswith("gpt_helper_btn_pick_materials"))
    dp.callback_query.register(callback_helper_btn_code_help, F.data.startswith("gpt_helper_btn_code_help"))
    dp.callback_query.register(callback_helper_btn_make_synopsis, F.data.startswith("gpt_helper_btn_make_synopsis"))

    # tag
    dp.callback_query.register(callback_tag_create, F.data.startswith("tag_create"))
    dp.callback_query.register(callback_get_all_tag, F.data == "get_all_tag")
    dp.callback_query.register(callback_del_tag, F.data.startswith("del_tag_"))

    dp.callback_query.register(callback_task_add, F.data == "task_add")
    dp.callback_query.register(callback_task_all, F.data == "task_all")
    dp.callback_query.register(callback_info_task, F.data.startswith("info_task_"))
    # dp.callback_query.register(callback_add_tag, F.data.startswith("add_tag_"))
    dp.callback_query.register(callback_updata_tag, F.data.startswith("to_add_tag_"))
    dp.callback_query.register(callback_del_task, F.data.startswith("del_task_"))





async def callback_helper_btn_explain(call: CallbackQuery, state: FSMContext):
    logger.info("callback_helper_btn_explain")
    my_user = User(call.from_user.id)
    builder = btn_leave_assistant(my_user.language())
    await call.bot.send_message(my_user.u_id, langs[my_user.language()]["mode_enabled_gpt_helper_explain"], reply_markup=builder.as_markup(resize_keyboard=True))
    await state.set_state(GptHelperBtnExplain.DATA.state)


async def callback_helper_btn_pick_materials(call: CallbackQuery, state: FSMContext):
    logger.info("callback_helper_btn_pick_materials")
    user = User(call.from_user.id)
    builder = btn_leave_assistant(user.language())
    await call.bot.send_message(user.u_id, langs[user.language()]["mode_enabled_gpt_helper_pick_materials"], reply_markup=builder.as_markup(resize_keyboard=True))
    await state.set_state(GptHelperBtnPickMaterials.DATA.state)


async def callback_helper_btn_code_help(call: CallbackQuery, state: FSMContext):
    logger.info("callback_helper_btn_pick_materials")
    user = User(call.from_user.id)
    builder = btn_leave_assistant(user.language())
    await call.bot.send_message(user.u_id, langs[user.language()]["mode_enabled_gpt_helper_code_help"], reply_markup=builder.as_markup(resize_keyboard=True))
    await state.set_state(GptHelperBtnCodeHelp.DATA.state)


async def callback_helper_btn_make_synopsis(call: CallbackQuery, state: FSMContext):
    logger.info("callback_helper_btn_pick_materials")
    user = User(call.from_user.id)
    builder = btn_leave_assistant(user.language())
    await call.bot.send_message(user.u_id, langs[user.language()]["mode_enabled_gpt_helper_make_synopsis"], reply_markup=builder.as_markup(resize_keyboard=True))
    await state.set_state(GptHelperBtnMakeSynopsis.DATA.state)


async def callback_tag_create(call: CallbackQuery, state: FSMContext):
    logger.info("callback_tag_create")
    user = User(call.from_user.id)
    await call.bot.send_message(user.u_id, langs[user.language()]["tag_create_title"])
    await state.set_state(Tag.NAME.state)


async def callback_get_all_tag(call: CallbackQuery):
    logger.info("callback_get_all_tag")
    user = User(call.from_user.id)
    all_tags = Tags(author=user.u_id).all_tags()
    builder = InlineKeyboardBuilder()
    for id, tag in all_tags:
        builder.add(InlineKeyboardButton(
            text=tag,
            callback_data=f"-"))
        builder.add(InlineKeyboardButton(
            text="Удалить",
            callback_data=f"del_tag_{id}"))
    builder.adjust(2)
    await call.bot.send_message(user.u_id, langs[user.language()]["all_yor_tags"], reply_markup=builder.as_markup())

async def callback_task_add(call: CallbackQuery, state: FSMContext):
    logger.info("callback_task_add")
    user = User(call.from_user.id)
    await call.bot.send_message(user.u_id, langs[user.language()]["get_tags_title"])
    await state.set_state(Task.TITLE.state)


async def callback_del_tag(call: CallbackQuery, state: FSMContext):
    logger.info("callback_del_tag")
    Tags(t_id=int(call.data[8:])).del_me()
    user = User(call.from_user.id)
    await call.bot.send_message(user.u_id, langs[user.language()]["get_tags_del"])
    await state.set_state(Task.TITLE.state)



async def callback_task_all(call: CallbackQuery):
    logger.info("callback_task_all")
    user = User(call.from_user.id)
    all_task = Tasks(author=user.u_id).all()
    t_msg = langs[user.language()]["all_yor_task"]

    builder = InlineKeyboardBuilder()
    for id, title in all_task:
        builder.add(InlineKeyboardButton(
            text=title,
            callback_data=f"info_task_{id}"))
    builder.adjust(1)
    await call.bot.send_message(user.u_id, t_msg, reply_markup=builder.as_markup())


async def callback_info_task(call: CallbackQuery, state: FSMContext):
    logger.info("callback_info_task")
    user = User(call.from_user.id)
    tasks = list(Tasks(t_id=int(call.data[10:])).info())
    print(tasks)
    builder = InlineKeyboardBuilder()
    all_tags = Tags(author=user.u_id).all_tags()
    for id, tag in all_tags:
        builder.add(InlineKeyboardButton(
            text="Add tag " + tag,
            callback_data=f"to_add_tag_{id}_{call.data[10:]}"))
    builder.add(InlineKeyboardButton(
        text=langs[user.language()]["del_task"],
        callback_data=f"del_task_{call.data[10:]}"))
    builder.adjust(1)
    await call.bot.send_message(user.u_id, langs[user.language()]["get_info_task"].format(
        tasks[1],
        tasks[2],
        tasks[3],
        tasks[4],
        tasks[5]), reply_markup=builder.as_markup())


async def callback_del_task(call: CallbackQuery, state: FSMContext):
    logger.info("callback_del_task")
    user = User(call.from_user.id)
    Tasks(int(call.data[9:])).del_me()
    await call.bot.send_message(user.u_id, langs[user.language()]["del_task_ok"])

async def callback_updata_tag(call: CallbackQuery, state: FSMContext):
    logger.info("callback_updata_tag")
    user = User(call.from_user.id)
    s = call.data[11:].split("_")

    task = s[1]
    tag  = s[0]
    Tasks(t_id=task).add_tag(tag)
    await call.bot.send_message(user.u_id, langs[user.language()]["add_tag_ok"])
