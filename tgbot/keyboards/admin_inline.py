from aiogram import types
from aiogram.types import Message, InlineKeyboardButton, \
    InlineKeyboardMarkup, ReplyKeyboardRemove


def MENU_ADM():
    buttons = [
        [
            types.InlineKeyboardButton(
                text= "📄 админпанель",
                callback_data= "menuAdm:adminpanel"
                )
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard= buttons
    )
    return keyboard

def ADMIN_PANEL():
    buttons = [
        [
            types.InlineKeyboardButton(
                text= 'Добавить конференц зал',
                callback_data= "addRoom:ConferenceRoom"
                ),
            types.InlineKeyboardButton(
                text= 'Добавить номер',
                callback_data= "addRoom:HotelRoom"
                )
        ],
        [
            types.InlineKeyboardButton(
                text= 'Назад',
                callback_data= "startAdm:back"
                )
        ]
    ]
    keyboard= types.InlineKeyboardMarkup(
        inline_keyboard= buttons
    )
    return keyboard

def ADD_ROOM():
    buttons= [
        [
            types.InlineKeyboardButton(
                text= 'отменить добавление',
                callback_data= "END:state"
                )
        ]
    ]
    keyboard= types.InlineKeyboardMarkup(
        inline_keyboard= buttons
    )
    return keyboard

def CHECK_ROOM():
    buttons=[
        [
        types.InlineKeyboardButton(
            text= 'Сохранить', 
            callback_data= "save:HotelRoom"
            ),
        types.InlineKeyboardButton(
            text='Изменить',
            callback_data= "change:HotelRoom"
            )
        ],   
    ]
    keyboard= types.InlineKeyboardMarkup(
        inline_keyboard= buttons
    )
    return keyboard

def CHANGE_HOTELROOM():
    buttons=[
        [
        types.InlineKeyboardButton(
            text= 'Фотографию', 
            callback_data= "HotelRoom:photo"
            )
        ],
        [
        types.InlineKeyboardButton(
            text='Тип(имя)',
            callback_data= "HotelRoom:name"
            ),
        types.InlineKeyboardButton(
            text='Описание',
            callback_data= "HotelRoom:description"
            )
        ],
        [
        types.InlineKeyboardButton(
            text='Колличество',
            callback_data= "HotelRoom:current_count"
            ),
        types.InlineKeyboardButton(
            text='Цену',
            callback_data= "HotelRoom:price"
            )
        ],
        [
        types.InlineKeyboardButton(
            text='Создать заново',
            callback_data= "HotelRoom:update"
            )
        ],
        [
        types.InlineKeyboardButton(
            text='Я передумал, сохраняем',
            callback_data= "save:HotelRoom"
            )

        ],   
    ]
    keyboard= types.InlineKeyboardMarkup(
        inline_keyboard= buttons
    )
    return keyboard