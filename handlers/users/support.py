# отправка одного сообщения оператору и обратно
from time import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.config import support_ids
from keyboards.inline.support import support_keyboard, support_callback
from loader import dp, bot
from state.invite import Invite


@dp.message_handler(Command("invite"))
async def ask_support(message: types.Message, state: FSMContext):
    await message.answer(" Введите id для того,чтобы пригласить друга: ")
    await Invite.unique_id.set()
    # await state.update_data(reply1=message.text)


@dp.message_handler(state=Invite.unique_id)
async def invite2(message: types.Message, state: FSMContext):
    await state.update_data(reply1=message.text)
    data = await state.get_data()
    support_ids.append(data.get("reply1"))
    keyboards = await support_keyboard(messages="one")
    await message.answer("Осталось совсем чуть-чуть...", reply_markup=keyboards)
    await state.finish()


@dp.callback_query_handler(support_callback.filter(messages="one"))
async def send_to_support(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer()
    user_id = int(callback_data.get("user_id"))
    await call.message.answer("Пришлите ваше сообщение,которым вы хотите поделиться c другом")
    await state.set_state("wait_for_support_message")  # состояние одного сообщения
    await state.update_data(second_id=user_id)  # это id оператора


@dp.message_handler(state="wait_for_support_message", content_types=types.ContentType.ANY)
async def get_support_message(message: types.Message, state: FSMContext):
    data = await state.get_data()
    second_id = data["second_id"]

    # user_id = message.from_user.username
    # if (user_id == None):
    #     await message.answer("Поройтесь в вашем профиле!")
    #     await message.answer_photo(open("photo/tg_1.png", "rb"), caption="Зайдите в настройки")
    #     await message.answer_photo(open("photo/tg_2.png", "rb"), caption="Измените профиль")
    #     await message.answer_photo(open("photo/tg_3.png", "rb"), caption="Придумайте себе имя👌")
    # await bot.send_message(second_id,
    #                        f"Вам письмо от t.me/{message.from_user.username} {message.from_user.id}.\nВы можете ответить нажав на кнопку ниже😉")

    keyboard = await support_keyboard(messages="one", user_id=message.from_user.id)
    await message.send_copy(second_id, reply_markup=keyboard) #copy_to
    await message.answer("Вы отправили это сообщение!")
    await state.reset_state()  # закрытие состояния


@dp.message_handler(Command("accept"))
async def accept(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user_friend = support_ids
    await message.reply(f"Эти два пользователя соединены:\n"
                        f"{user_id} - Вы,\n"
                        f"{','.join(user_friend)} - Ваш друг")
