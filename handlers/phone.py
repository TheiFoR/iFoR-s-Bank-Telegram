from aiogram import Router, Bot, types
from aiogram.fsm.context import FSMContext

from states import states
from utils import database
from . import language
from main import keyboards

dp = Router()

bot: Bot = None


async def get_phone(message: types.Message, state: FSMContext):
    await message.answer(text=database.text.welcome[language.id], reply_markup=keyboards.phone.markup())
    await state.set_state(states.get_number)


@dp.message(states.get_number)
async def get_phone_success(message: types.Message, state: FSMContext):
    await message.answer(text=database.text.get_code[language.id], reply_markup=keyboards.code.markup())

