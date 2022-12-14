from aiogram import Dispatcher
from aiogram.types import Message

async def user_start(message: Message):
    # await message.reply("Hello, user!")

    if 'start' in message.text:
        await MENU_ADM(message, src = 'Hello, ADMINушка!')
    elif 'Назад' in message.text:
        await MENU_ADM(message, src ='Ты вернулся в главное меню')

    
def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")