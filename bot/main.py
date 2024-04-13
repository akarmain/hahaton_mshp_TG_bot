import loguru
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from bot.handlers.main import register_all_handlers
from bot.misc import *
from bot.misc.util import MY_BOT

async def in_start(bot: Bot):
    # await set_me(bot)
    loguru.logger.info(f"Bot aiogram START {MY_BOT}")


async def in_stop():
    loguru.logger.info(f"Bot aiogram STOP {MY_BOT}")


async def start_bot():
    print(TgKeys.TOKEN)
    bot = Bot(token=TgKeys.TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.startup.register(in_start)
    dp.shutdown.register(in_stop)
    register_all_handlers(dp)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
