from aiogram import Dispatcher
from aiogram import F
from aiogram.types import CallbackQuery


def register_callback_handlers(dp: Dispatcher):
    # todo: register all callback handlers
    dp.callback_query.register(example_callback_register, F.data.startswith("callback_data_123"))


async def example_callback_register(call: CallbackQuery):
    await call.message.answer("example_inline_text")
    await call.answer(
        text="Спасибо, что воспользовались ботом!",
        show_alert=True
    )
    # или просто await callback.answer()
