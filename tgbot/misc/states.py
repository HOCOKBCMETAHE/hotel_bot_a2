from aiogram.dispatcher.filters.state import State, StatesGroup


# FSM ADMINS
class FSM_Admin_AddConferenceRoom(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

class FSM_Admin_AddHotelRoom(StatesGroup):
    # retype = State()
    photo = State()
    name = State()
    description = State()
    current_count = State()
    price = State()
    cehcksave = State()