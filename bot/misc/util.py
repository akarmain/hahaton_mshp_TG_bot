ALL_LANGUAGE_CODES = ["ru", "en"]
MY_BOT = "hahaton_mshp_bot"

first_request_gpt_helper_explain = "Ты gpt-4-turbo. Жди когда тебе зададут тему или явление, и дай на неё объяснение"
first_request_gpt_helper_pick_materials = "Ты gpt-4-turbo. Жди пока пользователь введет тему и напиши ресурсы маркированным списком с указанием ссылок в случае с интернет-статьями и названием работы и списком авторов в случае с книгами/научными статьями. Пока пользователь не написал тему проси чтобы он сделал это"
first_request_gpt_helper_code_help = "Ты gpt-4-turbo"
first_request_gpt_helper_make_synopsis = "Ты gpt-4-turbo"
ru_language = {
    "edit_name": "Главное имя бота",
    "edit_about": "Описание вверху или при в предпросмотре ссылки",
    "edit_description": "Описание, которое видит пользователь даже не нажав /start",
    "edit_commands": {"cmd": "cmd описание"},

    "start_msg": "Привет пользователь",
    "start_msg_new": "Ты новичок",
    "start_msg_old": "Ты не новичок",

    "main_btn_gpt_helper": "🤖 GPT-4 помощник",
    "main_btn_task_scheduler": "📅 Планировщика задач",
    "main_btn_leave_assistant": "Покинуть помощника",

    "text_upper_all_modes_gpt_helper": "Выберите режим помощника GPT-4:",
    "text_lower_all_modes_gpt_helper_btn_explain": "Объясни",
    "text_lower_all_modes_gpt_helper_btn_pick_materials": "Подбери материалы",
    "text_lower_all_modes_gpt_helper_btn_code_help": "Ответь на вопрос по коду",
    "text_lower_all_modes_gpt_helper_btn_make_synopsis": "Сделай конспект",

    "mode_enabled_gpt_helper_explain": "Вы включили режим по Объясни, пришлите тему или явление.  для отмены нажмите на кнопку снизу",
    "mode_enabled_gpt_helper_pick_materials": "Вы включили режим по Подбери материалы, пришлите .... для отмены нажмите на кнопку снизу",
    "mode_enabled_gpt_helper_code_help": "Вы включили режим по Ответь на вопрос по коду, пришлите ....  для отмены нажмите на кнопку снизу",
    "mode_enabled_gpt_helper_make_synopsis": "Вы включили режим по Сделай конспект, пришлите ....  для отмены нажмите на кнопку снизу",

    "mode_disabled_gpt_helper_explain": "Вы включили режим по Объясни",
    "mode_disabled_gpt_helper_pick_materials": "Вы включили режим по Подбери материалы",
    "mode_disabled_gpt_helper_code_help": "Вы включили режим по Ответь на вопрос по коду",
    "mode_disabled_gpt_helper_make_synopsis": "Вы включили режим по Сделай конспект",

    "text_upper_all_modes_task_scheduler": "Выберите что хотите сделать с заданиями:",

    "unknown_request": "⚠️ Не понимаю Вашего запроса \n /help",

    "mode_1": "режим Объясни",
    "mode_2": "Ответь на вопрос по коду",
    "mode_3": "Сделай конспект",
    "mode_4": "Сделай задачу",
    "mode_5": "Все задачи",
}


en_language = {
    "edit_name": "Main bot name",
    "edit_about": "Description at the top or when previewing a link",
    "edit_description": "Description that the user sees without even pressing /start",
    "edit_commands": {"cmd": "cmd description"},

    "start_msg": "Hello user",
    "start_msg_new": "You're a newbie",
    "start_msg_old": "You're not a newbie",
}

langs = {
    "ru": ru_language,
    "en": ru_language
}

ALL_KEYBOARD = []
for l in langs:
    ALL_KEYBOARD.append(langs[l]["main_btn_task_scheduler"])
    ALL_KEYBOARD.append(langs[l]["main_btn_gpt_helper"])
