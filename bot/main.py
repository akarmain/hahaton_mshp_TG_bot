from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from loguru import logger

from bot.handlers.main import register_all_handlers
from bot.misc import *
from bot.misc.util import MY_BOT




async def in_start(bot: Bot):
    # from bot.utils.set_me import set_me
    # await set_me(bot)
    logger.info(f"Aiogram START bot: @{MY_BOT}")


async def in_stop():
    print("Aiogram bot is stopped")


async def start_bot():
    bot = Bot(token=TgKeys.TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.startup.register(in_start)
    dp.shutdown.register(in_stop)
    register_all_handlers(dp)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
