from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить игру"),
            types.BotCommand("id", "узнать свой айдишник"),
            types.BotCommand("invite", "Пригласить друга"),
            types.BotCommand("accept", "Проверить соединение(P.s:Для приглашающего)"),
            types.BotCommand("support_call", "Пообщаться с техподдержкой"),
            types.BotCommand("photo", "Хочу фотку"),
            types.BotCommand("menu", "посмотреть меню"),
            types.BotCommand("help", "Помощь"),
        ]
    )
