from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode

from bot.misc import TgKeys


def register_admin_handlers(dp: Dispatcher):
    # todo: register all admin handlers
    pass


async def send_to_channel(mes, bot: Bot):
    await bot.send_message(TgKeys.CHANNEL_ID, mes, parse_mode=ParseMode.HTML)

