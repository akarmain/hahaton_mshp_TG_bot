import string

import pytz

MY_BOT = "hahaton_mshp_bot"
BOT_VERSION = "BOT VERSION: 0.0.1 25.11.23"

timezone = pytz.timezone('Europe/Moscow')
MAIN_ADMIN_ID = 912185600
ALL_LANGUAGE_CODES = ["ru", "en", "de"]
send_special_id = True
language_cach = {}
CHARACTERS = string.ascii_lowercase + string.ascii_uppercase + string.digits
for char_to_remove in "ABCDEFG":
    CHARACTERS = CHARACTERS.replace(char_to_remove, '')

ru_lang = {
    "edit_name": "запятая",
    "edit_about": "запятая",
    "edit_description": "Описание, которое видит пользователь даже не нажав /start",
    "edit_botpic": "Красивый QR-код",
    "edit_commands": {
        "lang": "🏳️ Изменить язык",

                      },

    "reply_keyboards_test_1": "1 кнопка",
    "reply_keyboards_test_2": "Пример state, введите текст:",
    "reply_keyboards_test_3": "пример клавиатуры",
    "example_inline_text": "пример",
    "example_inline_url": "ссылка",
    "cmd_start_already_using_bot": "Ты уже активировал бота",

    "error_no_license": "❌ Недостаточно прав доступа"
}

en_lang = {
    "edit_name": "Bot s main name",
    "edit_about": "Description at the top or in the link preview",
    "edit_description": "Description visible to the user even without clicking /start",
    "edit_botpic": "Beautiful QR code",
    "edit_commands": {"lang": "🏳️ Change language",
                      "cmd": "📍 Administrator commands"
                     },
    "reply_keyboards_test_1": "1 button",
    "reply_keyboards_test_2": "2 button",
    "reply_keyboards_test_3": "3 button",
    "example_inline_text": "example",
    "example_inline_url": "link",
    "cmd_start_already_using_bot": "You already using bot",
    "error_no_license": "❌ Insufficient access rights"
}

langs = {
    "ru": ru_lang,
    "en": ru_lang,
}
ALL_KEYBOARD = []  # словарь со всеми кнопками
for l in langs:
    ALL_KEYBOARD.append(langs[l]["reply_keyboards_test_1"])
    ALL_KEYBOARD.append(langs[l]["reply_keyboards_test_2"])
    ALL_KEYBOARD.append(langs[l]["reply_keyboards_test_3"])

if __name__ == '__main__':
    for name_cmd in langs["ru"]["edit_commands"]:
        print(name_cmd, langs["ru"]["edit_commands"][name_cmd])
