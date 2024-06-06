from loguru import logger

from bot import start_bot
import asyncio


logger.add("bot/database/log.log",
           format="{time} {level} {message}",
           rotation="70 MB",
           compression="zip",
           diagnose=True)


if __name__ == '__main__':
    asyncio.run(start_bot())

