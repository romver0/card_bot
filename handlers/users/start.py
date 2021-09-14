from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils.markdown import hitalic, italic, hcode, code, strikethrough, hstrikethrough, hbold, bold

from loader import dp

html_text = "\n".join(
    [
        hbold("Жизнь — это не всегда вопрос хороших карт. Иногда это хороший розыгрыш плохой руки."),
        hbold("© Джек Лондон"),

    ]
)
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer_sticker(open("animation/wave_animated_sticker.gif_", 'rb'))
    await message.answer(f"Привет, {message.from_user.full_name}!")
    await message.answer(html_text, parse_mode=types.ParseMode.HTML)
