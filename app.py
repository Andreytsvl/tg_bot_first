import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart  # отвечает только на команду "старт"

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from handlers.user_private import user_private_router

ALLOWED_UPDATES = ['message, edited_message']
# перечень разрешённых сообщений, которые слушает бот

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher() #более главный, чем роутеры


dp.include_routers(user_private_router)# подключение роутера
# можно писать хендлеры и в этом файле с декоратором @dp.message() см. гит
# @dp.message(CommandStart())  # хендлер
# async def start_cmd(message: types.Message):
#     await message.answer('Это была команда старт')

# @dp.message()
# async def echo(message: types.Message):# второй аргумент bot: Bot - если Бот в другом файле
#
#     await message.answer(message.text)
#     await message.reply(message.text)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    #пропустить обновления , пока бот был офлайн
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)
    # бот слушает бесконечно


asyncio.run(main())  # запуск функции
