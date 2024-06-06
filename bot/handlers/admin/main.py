from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from aiogram.types import Message, ContentType
from aiogram.filters import Command


from bot.misc import TgKeys


def register_admin_handlers(dp: Dispatcher):
    # todo: register all admin handlers
    dp.message.register(checking_work, Command("checking_work"))



async def checking_work(msg: Message, bot:Bot):
    m = await msg.answer("200")
    await bot.delete_message(msg.chat.id, m.message_id)
    await bot.delete_message(msg.chat.id, msg.message_id)



async def send_to_channel(mes, bot: Bot):
    await bot.send_message(TgKeys.CHANNEL_ID, mes, parse_mode=ParseMode.HTML)

