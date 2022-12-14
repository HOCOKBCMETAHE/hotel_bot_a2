from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram import types, Dispatcher

from ..misc.states import FSM_Admin_AddConferenceRoom

from ..keyboards.admin_inline import ADD_ROOM

# adding a conference room to the price list
async def add_a_conference_room_start(message: Message):
    await FSM_Admin_AddConferenceRoom.photo.set()
    await ADD_ROOM(message, src ='Загрузи фото')

async def load_photo(message: Message, state=FSMContext):
    async with state.proxy() as data:
        data['photo']=message.photo[0].file_id
    await FSM_Admin_AddConferenceRoom.next()
    await ADD_ROOM(message, src ='Введи название конференц зала')

async def add_name_conference_room(message: Message, state=FSMContext):
    async with state.proxy() as data:
        data['name']=message.text
    await FSM_Admin_AddConferenceRoom.next()
    await ADD_ROOM(message, src ='Введи описание конференц зала')

async def add_description_conference_room(message: Message, state=FSMContext):
    async with state.proxy() as data:
        data['description']=message.text
    await FSM_Admin_AddConferenceRoom.next()
    await ADD_ROOM(message, src ='Укажи цену')

async def add_price_conference_room(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['price']=float(message.text)

    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()





# registering a handler to add a conference room
def register_add_conference_room(dp: Dispatcher):
    # dp.register_message_handler(add_a_conference_room_start, Text(equals='Добавить конференц зал'), state=None, is_admin=True)
    dp.register_message_handler(load_photo ,content_types=['photo'], state=FSM_Admin_AddConferenceRoom.photo)
    dp.register_message_handler(add_name_conference_room, state=FSM_Admin_AddConferenceRoom.name)
    dp.register_message_handler(add_description_conference_room, state=FSM_Admin_AddConferenceRoom.description)
    dp.register_message_handler(add_price_conference_room, state=FSM_Admin_AddConferenceRoom.price)
    
    dp.register_message_handler(add_a_conference_room_start, Text(equals='Добавить конференц зал'), state=None)
    