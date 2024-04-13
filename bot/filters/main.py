from aiogram import Dispatcher

from bot.misc.util import MAIN_ADMIN_ID


def register_all_filters(dp: Dispatcher):
    # todo: register all filters - dp.bind_filter()
    pass


from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        try:
            return message.from_user.id == MAIN_ADMIN_ID
        except Exception:
            return False
