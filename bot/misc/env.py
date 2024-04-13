import os
from typing import Final
from dotenv import load_dotenv
from bot.misc.util import *

load_dotenv()


class TgKeys:
    TOKEN: Final = os.getenv('BOT_TG_TOKEN')
    CHANNEL_ID: Final = os.getenv('CHANNEL_TG_ID')



