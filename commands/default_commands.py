from aiogram import types


# Установка команд бота при старте
async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
        ]
    )
