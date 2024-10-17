class text:
    choose_language = "<b>🇺🇸 Choose a language\n" \
                      "🇷🇺 Выберите язык</b>"
    language = ['🇺🇸 Eng',
                '🇷🇺 Rus']

    welcome = ["<b>🏦 Welcome to iFoR's Bank 🏦</b>\n"\
               "\n"\
               "To authorize in the bank 🏦 and receive the code 🔑 we need your phone number 📱, which you provided during registration 📝 at the bank.",

               "<b>🏦 Добро пожаловать в iFoR's Bank 🏦</b>\n"\
               "\n"\
               "Для авторизации в банке 🏦 и получения кода 🔑 нам нужен ваш номер телефона 📱, который вы вводили при регистрации 📝 в банке."]

    get_code = ["The number has been received 📱, now you can get the authorization code 🔑.",
                "Номер получен 📱, теперь вы можете получить код авторизации 🔑."]

language_keyboard_text = {
    'lang': text.language,
}
language_keyboard_parameters = {}

rus_keyboard_text = {
    'phone': ['📱Дать номер'],
    'code': ['🔑Получить код'],
}
rus_keyboard_parameters = {
    'phone': {
        'request_contact': True
    }
}

eng_keyboard_text = {
    'phone': ['📱Give number'],
    'code': ['🔑Get code'],
}
eng_keyboard_parameters = {
    'phone': {
        'request_contact': True
    }
}

