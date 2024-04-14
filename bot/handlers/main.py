from aiogram import Dispatcher

from bot.handlers.admin import register_admin_handlers
from bot.handlers.other import register_other_handlers
from bot.handlers.user import register_user_handlers
from bot.handlers.user.callback import register_callback_handlers
from bot.handlers.user.state import register_all_state


def register_all_handlers(dp: Dispatcher) -> None:
    handlers = (
        register_callback_handlers,
        register_all_state,
        register_user_handlers,
        register_admin_handlers,
        register_other_handlers,
    )
    for handler in handlers:
        handler(dp)
