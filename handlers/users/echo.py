from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import test
from loader import dp


@dp.message_handler(Command("id"))
async def id(message: types.Message):
    await message.answer(text=f"Рад,что тебе захотелось узнать свой айдишник! \n"
                              f"А вот и он id:{message.from_user.id}", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Command("photo"))
async def photo(message: types.Message):
    await message.answer_photo(open("photo/1.jpg", "rb"))
    await message.answer_photo(open("photo/2.jpg", "rb"))
    await message.answer_photo(open("photo/4.jpg", "rb"), reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Command("menu"))
async def menu(message: types.Message):
    await message.answer(text="Вот твои кнопочки", reply_markup=test)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(f"Вот твоё сообщение: {message.text}", reply_markup=ReplyKeyboardRemove())
