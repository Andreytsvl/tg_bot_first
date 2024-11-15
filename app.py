import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart  # отвечает только на команду "старт"

from  dotenv import  find_dotenv, load_dotenv

load_dotenv(find_dotenv())

ALLOWED_UPDATES = ['message, edited_message'] # перечень разрешённых сообщений, которые слушает бот

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


@dp.message(CommandStart())  # хендлер
async def start_cmd(message: types.Message):
    await message.answer('Это была команда старт')


# @dp.message()
# async def echo(message: types.Message):
#     text = message.text
#
#     if text in ["привет", "Привет", "hi", "hello"]:
#         await  message.answer("И тебе привет")
#     elif text in ['Пока', 'пока', 'До свидания']:
#         await message.answer('И тебе пока!')
#     else:
#         await message.answer(message.text)  # отвечает эхом

@dp.message()
async def echo(message: types.Message, bot: Bot): # второй аргумент - если Бот в другом файле
    #await bot.send_message(message.from_user.id, 'Ответ')
    await message.answer(message.text) # отвечает эхом
    #await message.reply(message.text) # ответить с упоминанием автора

async def main():
    await bot.delete_webhook(drop_pending_updates=True) #пропустить обновления , пока бот был офлайн
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES) # бот слушает бесконечно


asyncio.run(main())  # запуск функции
