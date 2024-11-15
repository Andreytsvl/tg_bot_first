from aiogram import types, Router
from aiogram.filters import CommandStart, Command  # отвечает только на команду "старт"

user_private_router = Router()

@user_private_router.message(CommandStart())  # хендлер
async def start_cmd(message: types.Message):
    await message.answer('Привет, я виртуальный помощник')


# @user_private_router.message()
# async def echo(message: types.Message):
#     text = message.text
#
#     if text in ["привет", "Привет", "hi", "hello"]:
#         await  message.answer("И тебе привет")
#     elif text in ['Пока', 'пока', 'До свидания']:
#         await message.answer('И тебе пока!')
#     else:
#         await message.answer(message.text)  # отвечает эхом


#@user_private_router.message(Command('menu', 'name'))
#async def echo(message: types.Message):
    #await bot.send_message(message.from_user.id, 'Ответ')
    #await message.answer(message.text) # отвечает эхом
    #await message.reply(message.text) # ответить с упоминанием автора

@user_private_router.message(Command('menu', 'name'))
async def menu_cmd(message: types.Message):
    await message.answer("Вот меню:")