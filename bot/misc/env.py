import os
from typing import Final
from bot.misc.util import *
from dotenv import load_dotenv


load_dotenv()
class TgKeys:
    TOKEN: Final = os.getenv('BOT_TG_TOKEN')
    CHANNEL_ID: Final = os.getenv('CHANNEL_TG_ID')
    OPENAI_API_KEY: Final = os.getenv('OPENAI_API_KEY')