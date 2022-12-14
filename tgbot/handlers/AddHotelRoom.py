from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import types, Dispatcher

from ..misc.states import FSM_Admin_AddHotelRoom

from ..keyboards.admin_inline import ADMIN_PANEL
from ..keyboards.admin_inline import ADD_ROOM
from ..keyboards.reply import ADD_ROOM_CLOSE
from ..keyboards.admin_inline import CHECK_ROOM
from ..keyboards.admin_inline import CHANGE_HOTELROOM


async def add_a_hotel_room_start(callback: types.CallbackQuery, state: FSMContext):
    current_filter = callback.data.split(":")[1]
    if current_filter == "HotelRoom":
        
        await callback.message.edit_text('Загрузи фото', reply_markup= ADD_ROOM())
        await callback.answer()
        await FSM_Admin_AddHotelRoom.photo.set()

# async def retypeHotelroom(message: Message):
#    
#     await FSM_Admin_AddHotelRoom.next()
#     await message.reply("Загрузи фото", reply_markup=ADD_ROOM())

async def load_photo(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSM_Admin_AddHotelRoom.next()
    await message.answer('Введи тип(Люкс, Cтандарт и т.д)\nили название номера', reply_markup=ADD_ROOM_CLOSE())
    # await callback.answer()

async def add_name(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSM_Admin_AddHotelRoom.next()
    await message.answer('Введи описание номера')

async def add_description(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSM_Admin_AddHotelRoom.next()
    await message.answer('Введи количество номеров данного типа')

async def add_count(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['count']=int(message.text)
    await FSM_Admin_AddHotelRoom.next()
    await message.answer('Введи цену номера')

async def add_price(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['price']=int(message.text)

    async with state.proxy() as data:
        await message.answer("Теперь давай проверим, все ли верно", reply_markup= ReplyKeyboardRemove())
        await message.answer_photo(str(data['photo']), f"Класс номера: {data['name']}\n\nОписание: {data['description']}\n\nКолличество доступных номеров данного класса: {data['count']}\n\nТекущая стоимость {data['price']}рублей в сутки", reply_markup= CHECK_ROOM())
        # await message.answer(text=f'{str(data)}', reply_markup= CHECK_ROOM())

async def CallbackSaveRoom(callback: types.CallbackQuery, state: FSMContext):
    current_TypesRoom = callback.data.split(":")[1]

    if current_TypesRoom == "HotelRoom":
        await state.finish()
        await callback.message.delete()
        await callback.message.answer('Номер успешно сохранен\n\nТы вернулся в панель администратра', \
            reply_markup= ADMIN_PANEL())
    await callback.answer()
    
async def CallbackChangeRoom(callback: types.CallbackQuery, state: FSMContext):
    current_TypesRoom = callback.data.split(":")[1]

    if current_TypesRoom == "photo":
        await callback.message.delete()
        await callback.message.answer('Номер успешно сохранен\n\nТы вернулся в панель администратра', \
            reply_markup= ADMIN_PANEL())
    await callback.answer()

def register_add_hotel_room(dp: Dispatcher):
    dp.register_callback_query_handler(add_a_hotel_room_start, Text(startswith="addRoom:"), state=None, is_admin=True)

    # dp.register_message_handler(retypeHotelroom, state=FSM_Admin_AddHotelRoom.retype)
    # dp.register_message_handler(retypeHotelroom, Text(startswith="addRoom:"), state=FSM_Admin_AddHotelRoom.retype)

    dp.register_message_handler(load_photo,  state=FSM_Admin_AddHotelRoom.photo, content_types=['photo'])
    dp.register_message_handler(add_name, state=FSM_Admin_AddHotelRoom.name)
    dp.register_message_handler(add_description, state=FSM_Admin_AddHotelRoom.description)
    dp.register_message_handler(add_count, state=FSM_Admin_AddHotelRoom.current_count)
    dp.register_message_handler(add_price, state=FSM_Admin_AddHotelRoom.price)
    dp.register_callback_query_handler(CallbackSaveRoom, Text(startswith="save:"), state=FSM_Admin_AddHotelRoom.price)
    dp.register_callback_query_handler(CallbackChangeRoom, Text(startswith="HotelRoom:"), state=FSM_Admin_AddHotelRoom.price)