from aiogram import Dispatcher, types
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.utils.callback_data import CallbackData

from ..misc.states import FSM_Admin_AddHotelRoom
from ..keyboards.admin_inline import ADD_ROOM, ADMIN_PANEL



async def END (callback: types.CallbackQuery, state: FSMContext):

    current_state = await state.get_state()
    current_TypesRoom = callback.data.split(":")[1]

    if current_TypesRoom == "state":
        await callback.message.delete()
        await callback.answer(show_alert=True)
        if current_state is None:
            await callback.message.answer('[SYSTEM]: No FSM process\n[STATUS]: OK',reply_markup= ADMIN_PANEL())
            return
        await state.finish()
        await callback.message.answer(f'[STATE]: {current_state}\n[STATUS]: Finished\nТы вернулся в панель администратра',reply_markup= ADMIN_PANEL())
        await callback.answer()

def register_CallBackDatas(dp: Dispatcher):
    dp.register_callback_query_handler(END, Text(startswith="END:"), state="*")
