from aiogram import types
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# keyboard for admin main menu

def ADD_ROOM_CLOSE():
    buttons= [
        [
            types.KeyboardButton(
                text= 'отменить добавление'
                )
        ]
    ]
    keyboard= types.ReplyKeyboardMarkup(
        keyboard= buttons,
        resize_keyboard=True
    )
    return keyboard
