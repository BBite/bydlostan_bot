from aiogram import types

from loader import dp


@dp.message_handler(commands='delete_markup')
async def delete_markup(message: types.Message):
    await message.answer('Видалено нахуй', reply_markup=types.ReplyKeyboardRemove())
