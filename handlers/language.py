from aiogram import Router, Bot, types
from aiogram.fsm.context import FSMContext

from states import states
from utils import database
from . import language

dp = Router()

bot: Bot = None


@dp.message(lambda msg: msg.text == database.text.language[0])
async def eng(message: types.Message, state: FSMContext):
    import main
    language.id = 0
    main.keyboards = main.telegram_keyboards.get(main.database.eng_keyboard_text, main.database.eng_keyboard_parameters)
    await main.phone.get_phone(message, state)


@dp.message(lambda msg: msg.text == database.text.language[1])
async def rus(message: types.Message, state: FSMContext):
    import main

    language.id = 1
    main.keyboards = main.telegram_keyboards.get(main.database.rus_keyboard_text, main.database.rus_keyboard_parameters)
    await main.phone.get_phone(message, state)
