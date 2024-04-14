import json

import loguru
from aiogram import Dispatcher
from aiogram import F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.database.models import User
from bot.database.models.tags import Tags, get_all_tags, all_tags
from bot.database.models.task import Tasks
from bot.handlers.admin.main import send_to_channel
from bot.keyboards.reply import btn_menu
from bot.misc.util import langs, MY_BOT, first_request_gpt_helper_explain, first_request_gpt_helper_pick_materials, first_request_gpt_helper_code_help, first_request_gpt_helper_make_synopsis
from bot.utils.all_state.user import GptHelperBtnExplain, GptHelperBtnPickMaterials, GptHelperBtnCodeHelp, GptHelperBtnMakeSynopsis, Tag, Task
from bot.utils.bug_catcher import check_time_format
from bot.utils.gpt import chatGPT

def register_all_state(dp: Dispatcher) -> None:
    dp.message.register(state_gpt_helper_explain, GptHelperBtnExplain.DATA)
    dp.message.register(state_gpt_helper_pick_materials, GptHelperBtnPickMaterials.DATA)
    dp.message.register(state_gpt_helper_code_help, GptHelperBtnCodeHelp.DATA)
    dp.message.register(state_gpt_helper_make_synopsis, GptHelperBtnMakeSynopsis.DATA)

    dp.message.register(state_get_tag_name, Tag.NAME)
    dp.message.register(state_get_task_title, Task.TITLE)
    dp.message.register(state_get_task_description, Task.DESCRIPTION)
    dp.message.register(state_get_task_time_over, Task.TIME_OVER)
    dp.message.register(state_get_task_complexity, Task.COMPLEXITY)



async def state_gpt_helper_explain(msg: Message, bot: Bot, state: FSMContext):
    # Создаем пользователя и проверяем что он не нажал на mode_disabled_gpt_helper_explain
    user = User(msg.from_user.id)
    if msg.text == langs[user.language()]["main_btn_leave_assistant"]:
        await btn_menu(user, langs[user.language()]["mode_disabled_gpt_helper_explain"], bot)
        await state.clear()
        return

    # Получаем контекст диалога и обрабатываем запросы
    user_data = await state.get_data()
    if user_data == {}:
        gtp_messages = [{"role": "system", "content": first_request_gpt_helper_explain},
                    {"role": "user", "content": msg.text}]
    else:
        gtp_messages = json.loads(user_data["CONTEXT"])

    gtp_messages.append({"role": "user", "content": msg.text})
    gpt = chatGPT(gtp_messages)
    ans = gpt.choices[0].message.content
    await msg.answer(ans)
    gtp_messages.append({"role": "assistant", "content": ans})
    await state.update_data(CONTEXT=json.dumps(gtp_messages))
    await state.set_state(GptHelperBtnExplain.DATA.state)


async def state_gpt_helper_pick_materials(msg: Message, bot: Bot, state: FSMContext):
    user = User(msg.from_user.id)
    if msg.text == langs[user.language()]["main_btn_leave_assistant"]:
        await btn_menu(user, langs[user.language()]["mode_disabled_gpt_helper_explain"], bot)
        await state.clear()
        return

    user_data = await state.get_data()
    if user_data == {}:
        gtp_messages = [{"role": "system", "content": first_request_gpt_helper_pick_materials},
                        {"role": "user", "content": msg.text}]
    else:
        gtp_messages = json.loads(user_data["CONTEXT"])

    gtp_messages.append({"role": "user", "content": msg.text})
    gpt = chatGPT(gtp_messages)
    ans = gpt.choices[0].message.content
    await msg.answer(ans)
    gtp_messages.append({"role": "assistant", "content": ans})
    await state.update_data(CONTEXT=json.dumps(gtp_messages))
    await state.set_state(GptHelperBtnExplain.DATA.state)


async def state_gpt_helper_code_help(msg: Message, bot: Bot, state: FSMContext):
    user = User(msg.from_user.id)
    if msg.text == langs[user.language()]["main_btn_leave_assistant"]:
        await btn_menu(user, langs[user.language()]["mode_disabled_gpt_helper_explain"], bot)
        await state.clear()
        return

    user_data = await state.get_data()
    if user_data == {}:
        gtp_messages = [{"role": "system", "content": first_request_gpt_helper_code_help},
                        {"role": "user", "content": msg.text}]
    else:
        gtp_messages = json.loads(user_data["CONTEXT"])

    gtp_messages.append({"role": "user", "content": msg.text})
    gpt = chatGPT(gtp_messages)
    ans = gpt.choices[0].message.content
    await msg.answer(ans)
    gtp_messages.append({"role": "assistant", "content": ans})
    await state.update_data(CONTEXT=json.dumps(gtp_messages))
    await state.set_state(GptHelperBtnExplain.DATA.state)



async def state_gpt_helper_make_synopsis(msg: Message, bot: Bot, state: FSMContext):
    user = User(msg.from_user.id)
    if msg.text == langs[user.language()]["main_btn_leave_assistant"]:
        await btn_menu(user, langs[user.language()]["mode_disabled_gpt_helper_explain"], bot)
        await state.clear()
        return

    user_data = await state.get_data()
    if user_data == {}:
        gtp_messages = [{"role": "system", "content": first_request_gpt_helper_make_synopsis},
                        {"role": "user", "content": msg.text}]
    else:
        gtp_messages = json.loads(user_data["CONTEXT"])

    gtp_messages.append({"role": "user", "content": msg.text})
    gpt = chatGPT(gtp_messages)
    ans = gpt.choices[0].message.content
    await msg.answer(ans)
    gtp_messages.append({"role": "assistant", "content": ans})
    await state.update_data(CONTEXT=json.dumps(gtp_messages))
    await state.set_state(GptHelperBtnExplain.DATA.state)


async def state_get_tag_name(msg: Message, bot: Bot, state: FSMContext):
    user = User(msg.from_user.id)
    if msg.text in all_tags():
        await btn_menu(user, langs[user.language()]["tag_create_error"], bot)
        await state.clear()
        return
    Tags(name=msg.text, author=msg.from_user.id).add()
    await state.clear()
    await msg.answer(langs[user.language()]["tag_create_ok"].format(msg.text))

async def state_get_task_title(msg: Message, bot: Bot, state: FSMContext):
    user = User(msg.from_user.id)
    await state.update_data(TITLE=msg.text)
    await msg.answer(langs[user.language()]["get_tags_description"])
    await state.set_state(Task.DESCRIPTION.state)


async def state_get_task_description(msg: Message, bot: Bot, state: FSMContext):
    user = User(msg.from_user.id)
    await state.update_data(DESCRIPTION=msg.text)
    await msg.answer(langs[user.language()]["get_tags_time_over"])
    await state.set_state(Task.TIME_OVER.state)


async def state_get_task_time_over(msg: Message, bot: Bot, state: FSMContext):
    user = User(msg.from_user.id)
    if not check_time_format(msg.text):
        await msg.answer(langs[user.language()]["get_tags_time_over"])
        await state.set_state(Task.TIME_OVER.state)
        return
    await state.update_data(TIME_OVER=msg.text)
    await msg.answer(langs[user.language()]["get_tags_complexity"])
    await state.set_state(Task.COMPLEXITY.state)


async def state_get_task_complexity(msg: Message, bot: Bot, state: FSMContext):
    user = User(msg.from_user.id)
    user_data = await state.get_data()
    title = user_data["TITLE"]
    description = user_data["DESCRIPTION"]
    time_over = user_data["TIME_OVER"]
    complexity = msg.text
    Tasks(title=title,
          description=description,
          time_over=time_over,
          complexity=complexity,
          author=msg.from_user.id
          ).add()
    await msg.answer(langs[user.language()]["tags_create_ok"].format(title, description, time_over, complexity))
    await state.clear()
