ALL_LANGUAGE_CODES = ["ru", "en"]
MY_BOT = "hahaton_mshp_bot"

first_request_gpt_helper_explain = "Ты gpt-4-turbo. Жди когда тебе зададут тему или явление, и дай на неё объяснение"
first_request_gpt_helper_pick_materials = "Ты gpt-4-turbo. Жди пока пользователь введет тему и напиши ресурсы маркированным списком с указанием ссылок в случае с интернет-статьями и названием работы и списком авторов в случае с книгами/научными статьями. Пока пользователь не написал тему проси чтобы он сделал это"
first_request_gpt_helper_code_help = "Ты gpt-4-turbo. Жди пока пользователь введет код, твоя задача объяснить что происходит на каждой строчке с примерами. Пока пользователь не написал код проси чтобы он сделал это"
first_request_gpt_helper_make_synopsis = "Ты gpt-4-turbo. Жди пока пользователь не пришлет конспект, твоя вытянуть самое главное и написать короткую справку в 60% от всего текста. Пока пользователь не прислал текст проси чтобы он сделал это"
ru_language = {
    "edit_name": "EduHelperAI",
    "edit_about": "🤖 Привет, я Учебный Помощник! Разработанный на хакатоне 2024 от МШП",
    "edit_description": "🤖 Привет, я Учебный Помощник! Разработанный на хакатоне 2024 от МШП",
    "edit_commands": {"start": "start"},

    "start_msg": "👋 Привет! Я умный бот, и я помогу тебе в учёбе",
    "start_msg_new": "👋 Привет новый пользователь!\n Я умный бот, и я помогу тебе в учёбе",
    "start_msg_old": "👋 Привет!\n Я умный бот, и я помогу тебе в учёбе",


    "main_btn_gpt_helper": "🤖 GPT-4 помощник",
    "main_btn_task_scheduler": "📅 Планировщика задач",
    "main_btn_leave_assistant": "Покинуть помощника",
    "btn_detailed_settings": "🧐 Что умеет бот",

    "text_upper_all_modes_gpt_helper": "Выберите режим помощника GPT-4:",
    "text_lower_all_modes_gpt_helper_btn_explain": "Объясни",
    "text_lower_all_modes_gpt_helper_btn_pick_materials": "Подбери материалы",
    "text_lower_all_modes_gpt_helper_btn_code_help": "Ответь на вопрос по коду",
    "text_lower_all_modes_gpt_helper_btn_make_synopsis": "Сделай конспект",

    "mode_enabled_gpt_helper_explain": "Вы включили режим Объясни, пришлите тему или явление, которое хотите понять. Для отмены нажмите на кнопку снизу",
    "mode_enabled_gpt_helper_pick_materials": "Вы включили режим Подбери материалы, пришлите тему, по которой хотите получить какие-либо материалы. Для отмены нажмите на кнопку снизу",
    "mode_enabled_gpt_helper_code_help": "Вы включили режим Ответь на вопрос по коду, пришлите сниппет кода и вопрос по нему. Для отмены нажмите на кнопку снизу",
    "mode_enabled_gpt_helper_make_synopsis": "Вы включили режим Сделай конспект, пришлите текст, который нужно законспектировать. Для отмены нажмите на кнопку снизу",

    "mode_disabled_gpt_helper_explain": "Вы включили режим Объясни",
    "mode_disabled_gpt_helper_pick_materials": "Вы включили режим Подбери материалы",
    "mode_disabled_gpt_helper_code_help": "Вы включили режим Ответь на вопрос по коду",
    "mode_disabled_gpt_helper_make_synopsis": "Вы включили режим Сделай конспект",

    "text_upper_all_modes_task_scheduler": "Выберите что хотите сделать с заданиями:",


    "mode_enabled_task_btn_tag_create": "🆕 Создать тег",
    "mode_enabled_task_btn_tag_all": "📑 Все теги",
    "mode_enabled_task_btn_task_add": "➕ Добавить задачу",
    "mode_enabled_task_btn_task_all": "📜 Список всех задач",
    "mode_enabled_task_btn_task_remind": "🔔 Напомнить о задаче",
    "mode_enabled_task_btn_task_statistics": "📊 Статистика",

    "tag_create_title": "🏷️ Напишите название тега",
    "tag_create_error": "🚫 Данное имя уже занято",
    "tag_create_ok": "✅ Вы создали тег: {}",
    "all_yor_tags": "🔖 Ваши теги:\n\n",

    "get_tags_title": "📝 Введите название",
    "get_tags_del": "🗑️ Тег был удален",

    "get_tags_description": "📄 Введите описание",
    "get_tags_time_over": "⏰ Введите время ДД.ММ.ГГ ММ:ЧЧ <code>14.04.24 20:31</code>",
    "get_tags_complexity": "🔢 Введите сложность]",
    "tags_create_ok": "✅ Вы создали задание: \n\nНазвание: <b>{}</b> \nОписание: {} \nКрайний срок: {}\nСложность: {}",
    "all_yor_task": "📋 Ваши задания:\n\n",
    "get_info_task": """📝 Задание: <b>{}</b>\n({})
До: {}
Сложность: {}
Тег: {}
    """,
    "del_task_ok": "🗑️ Задание удалено",
    "add_tag_to_task": "🏷️ Выберете тег",
    "unknown_request": "⚠️ Не понимаю Вашего запроса",
    "del_task": "🗑️ Удалить",
    "add_tag": "➕ Поставить тег",
    "add_tag_ok": "✅ Вы добавили тег",
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
