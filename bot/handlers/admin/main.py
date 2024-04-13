import asyncio

from aiogram import Dispatcher, Bot
from aiogram import F
from aiogram.enums import ContentType
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile
from bot.utils.all_state.admin_state import GetFileId

from bot.database.methods import PATH_BAZE, PATH_LOG
from bot.database.models.user import MyUser
from bot.misc.env import *
from bot.misc.util import langs, BOT_VERSION
import bot.database as db

loop = asyncio.get_event_loop()


def register_admin_handlers(dp: Dispatcher):
    dp.message.register(admin_cmd, F.from_user.id.in_({MAIN_ADMIN_ID}) & F.text == "/cmd")
    dp.message.register(send_baze, F.from_user.id.in_({MAIN_ADMIN_ID}) & F.text == "/send_baze")
    dp.message.register(send_version, F.from_user.id.in_({MAIN_ADMIN_ID}) & F.text == "/v")

    dp.message.register(i_not_admin, F.from_user.id.not_in({MAIN_ADMIN_ID}) & (F.text.in_({"/v", "/send_baze", "/cmd"})))
    dp.message.register(send_log,  Command("send_log"))
    dp.message.register(get_file_id,  Command("get_file_id"))
    dp.message.register(get_by_file_id,  Command("get_by_file_id"))

async def admin_cmd(msg: Message):
    cmd = """
/send_baze - отправить базу\n\n
/send_log - отправить логи\n\n
/v - версия бота\n\n
/ban - забанить пользователя\n\n
/create_ref - создать рефералку\n\n
/get_file_id - получить file_id\n\n
/get_by_file_id - получить медиа (id, type)
"""
    await msg.answer(cmd)


async def i_not_admin(msg: Message):
    await msg.answer(langs[MyUser(msg.from_user.id).language]["error_no_license"])


async def send_baze(msg: Message):
    await msg.answer_document(FSInputFile(PATH_BAZE))


async def send_version(msg: Message):
    await msg.answer(BOT_VERSION)

async def create_ref(msg: Message):
    args = msg.text.split()
    if len(args) > 2:
        main_name = args[1]
        description = ' '.join(args[2:])
        db.create_ref_url(main_name, description)
        await msg.answer(f"✅ Получилось -> https://t.me/{MY_BOT}?start={main_name}")
    else:
        await msg.answer("❌ Используйте команду так: /create_ref имя описание \n(/ban ytb трафик с youtube)")

async def send_log(msg: Message):
    await msg.answer_document(FSInputFile(PATH_LOG))


async def get_file_id(msg: Message, state: FSMContext):
    """
    Получает файл для file id медиа
    """
    await msg.answer("ЖДУ")
    await state.set_state(GetFileId.MEDIA.state)



async def send_file_id(msg: Message, state: FSMContext):
    """
    Отправляет file_id медиафайла лучшего качества (фото/видео/GIF).
    """
    await state.clear()
    if msg.content_type == ContentType.PHOTO:
        best_quality_photo = msg.photo[-1]
        await msg.answer(f"File ID фотографии лучшего качества: {best_quality_photo.file_id}")

    elif msg.content_type == ContentType.VIDEO:
        best_quality_video = msg.video
        await msg.answer(f"File ID видео лучшего качества: {best_quality_video.file_id}")

    elif msg.content_type == ContentType.ANIMATION:
        best_quality_gif = msg.animation
        await msg.answer(f"File ID GIF лучшего качества: {best_quality_gif.file_id}")

    else:
        await msg.answer("Сообщение не содержит медиафайл фото/видео/GIF.")

async def get_by_file_id(msg: Message, bot:Bot):
    """
    Отправляет файл по его id
    """
    args = msg.text.split()
    if len(args) != 3:
        await msg.answer("❌ Используйте команду так: /get_by_file_id команда \n(/get_by_file_id 912391231237123 photo)")
        return
    arg_file_id = args[1]
    match args[2]:
        case "photo":
            await bot.send_photo(msg.chat.id, arg_file_id)
        case "document":
            await bot.send_document(msg.chat.id, arg_file_id)
        case "audio":
            await bot.send_audio(msg.chat.id, arg_file_id)
        case "sticker":
            await bot.send_sticker(msg.chat.id, arg_file_id)
        case "animation" | "gif":
            await bot.send_animation(msg.chat.id, arg_file_id)


