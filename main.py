import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

import config
from utils import telegram_keyboards, database
from states import states
from handlers import language, phone

bot = Bot(token=config.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

lang_keyboards = telegram_keyboards.get(database.language_keyboard_text, database.language_keyboard_parameters)
keyboards = telegram_keyboards.get(database.eng_keyboard_text, database.eng_keyboard_parameters)


@dp.message(Command('start'))
async def message(message: types.Message, state: FSMContext):
    await message.answer(text=database.text.choose_language, reply_markup=lang_keyboards.lang.markup())
    await state.set_state(states.select_language)


async def main():
    logging.basicConfig(level=logging.DEBUG)

    dp.include_router(language.dp)
    dp.include_router(phone.dp)

    language.bot = bot
    phone.bot = bot

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
