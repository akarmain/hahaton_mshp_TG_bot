import os

import rollbar
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from dotenv import load_dotenv
from loguru import logger
import re
import datetime
from bot.database.models import User
from bot.handlers.admin.main import send_to_channel
from bot.misc.util import *

load_dotenv()
rollbar.init(
    access_token=os.getenv('ROLLBAR_API_KEY'),
    environment='venv',
    code_version='1.0'
)


def bot_bug_catcher_msg_bot(func):
    async def wrapper(msg: Message, bot: Bot):
        try:
            await func(msg, bot)
        except Exception as e:
            rollbar.report_exc_info(extra_data={"user_id": msg.from_user.id})
            logger.error(f"{msg.from_user.id} by bot_bug_catcher_msg | {func.__name__} | {e}")
            my_user = User(msg.from_user.id)
            await send_to_channel(f"""💢❗️SOS Я СЛОМАЛСЯ ❗💢
            <code>{msg.from_user.id}</code> от @{MY_BOT}
В {func.__name__} | 
{e}
            """, bot)
            await msg.answer(langs[my_user.language()]["text_error"])

    return wrapper


def bot_bug_catcher_msg_bot_state(func):
    async def wrapper(msg: Message, bot: Bot, state: FSMContext):
        try:
            await func(msg, bot, state)
        except Exception as e:
            rollbar.report_exc_info(extra_data={"user_id": msg.from_user.id})
            logger.error(f"{msg.from_user.id} by bot_bug_catcher_msg | {func.__name__} | {e}")
            my_user = User(msg.from_user.id)
            await send_to_channel(f"""💢❗️SOS Я СЛОМАЛСЯ ❗💢
            <code>{msg.from_user.id}</code> от @{MY_BOT}
В {func.__name__} | 
{e}
            """, bot)
            await msg.answer(langs[my_user.language]["text_error"])

    return wrapper


def check_time_format(time_str):
    if not re.match(r'^\d{2}\.\d{2}\.\d{2} \d{2}:\d{2}$', time_str):
        return False
    try:
        datetime.datetime.strptime(time_str, "%d.%m.%y %H:%M")
        return True
    except ValueError:
        return False
