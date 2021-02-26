from aiogram import types

from loader import dp


@dp.message_handler(commands='tag_bydlostan')
async def tag_all(message: types.Message):
    answer = ''
    answer += '<a href="tg://user?id=576927517">Би</a>'
    answer += '<a href="tg://user?id=695444908">дло</a>'
    answer += '<a href="tg://user?id=556042536">с</a>'
    answer += '<a href="tg://user?id=829242296">т</a>'
    answer += '<a href="tg://user?id=609459963">а</a>'
    answer += '<a href="tg://user?id=669442518">н</a>'
    await message.answer(answer)
