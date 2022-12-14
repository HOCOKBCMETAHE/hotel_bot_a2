from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, \
    ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text

from ..keyboards.admin_inline import MENU_ADM
from ..keyboards.admin_inline import ADMIN_PANEL

# from ..keyboards.reply import ADD_ROOM


async def admin_start(message: Message):
    if 'start' in message.text:
        await message.answer('Hello, ADMINушка!', reply_markup= MENU_ADM())

async def admin_main(callback: CallbackQuery):
    current_filter = callback.data.split(":")[1]
    if current_filter == 'back':
        await callback.message.edit_text("Ты вернулся в главное меню",reply_markup= MENU_ADM())
        await callback.answer()

async def open_adminpanel(callback: CallbackQuery):
    current_filter = callback.data.split(":")[1]
    if current_filter == 'adminpanel':
        await callback.message.edit_text("Открыта панель администратра",reply_markup= ADMIN_PANEL())
        await callback.answer()

async def canceling_states(callback: CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await callback.message.edit_text('[SYSTEM]: No FSM process\n[STATUS]: OK', reply_markup= ADMIN_PANEL)
        await callback.answer()
        return
    await state.finish()
    await callback.message.reply(f'[STATE]: {current_state}\n[STATUS]: Finished')
    await callback.message.edit_text(f'Ты вернулся в панель администратра\n{current_state}', reply_markup= ADMIN_PANEL)
    await callback.answer()

async def canceling_states_reply(message: Message, state: FSMContext):
    current_state = await state.get_state()
    await message.reply("Добавление отменено", reply_markup=ReplyKeyboardRemove())
    if current_state is None:
        await message.reply('[SYSTEM]: No FSM process\n[STATUS]: OK', reply_markup= ADMIN_PANEL())
        return
    await state.finish()
    await message.reply(f'[STATE]: {current_state}\n[STATUS]: Finished')
    await message.answer(f'Ты вернулся в панель администратра\n{current_state}', reply_markup= ADMIN_PANEL())

def register_admin(dp: Dispatcher):
    # dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    # dp.register_message_handler(admin_start, Text(equals='Назад'), state="*", is_admin=True)
    # dp.register_message_handler(open_adminpanel, Text(equals='📄 админпанель'), state="*", is_admin=True)
    dp.register_message_handler(canceling_states_reply, Text(equals='отменить добавление', ignore_case=True), state="*")

    dp.register_message_handler(admin_start, commands=["start"], state="*")
    dp.register_callback_query_handler(admin_main, Text(startswith='startAdm:'), state="*")
    dp.register_callback_query_handler(open_adminpanel, Text(startswith='menuAdm:'), state="*")