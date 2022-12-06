from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher

# FSM ADMINS
class FSM_Admin_AddConferenceRoom(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

# adding a conference room to the price list
async def add_a_conference_room_start(message: types.Message):
    await FSM_Admin_AddConferenceRoom.photo.set()
    await message.reply('Загрузи фото')
    
async def load_photo(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['photo']=message.photo[0].file_id
    await FSM_Admin_AddConferenceRoom.next()
    await message.reply('Введи название конференц зала')

async def add_name_conference_room(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['name']=message.text
    await FSM_Admin_AddConferenceRoom.next()
    await message.reply('Введи описание конференц зала')

async def add_description_conference_room(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['description']=message.text
    await FSM_Admin_AddConferenceRoom.next()
    await message.reply('Укажи цену')

async def add_price_conference_room(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price']=float(message.text)

    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()

async def canceling_states(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.reply('[SYSTEM]: No FSM process\n[STATUS]: OK')
        return
    await state.finish()
    await message.reply('[SYSTEM]: Finished\n[STATUS]: OK')

def register_fsm_admin(dp: Dispatcher):
    # registering a handler to add a conference room
    dp.register_message_handler(add_a_conference_room_start, commands=["addCR"], state=None)
    dp.register_message_handler(load_photo ,content_types=['photo'], state=FSM_Admin_AddConferenceRoom.photo)
    dp.register_message_handler(add_name_conference_room, state=FSM_Admin_AddConferenceRoom.name)
    dp.register_message_handler(add_description_conference_room, state=FSM_Admin_AddConferenceRoom.description)
    dp.register_message_handler(add_price_conference_room, state=FSM_Admin_AddConferenceRoom.price)
    dp.register_message_handler(canceling_states, commands='отмена', state="*")
    dp.register_message_handler(canceling_states, Text(equals='отмена', ignore_case=True), state="*")