from aiogram import types

from loader import dp


@dp.message_handler(commands='call_over')
async def call_over(message: types.Message):
    answer = ''
    answer += '<a href="tg://user?id=576927517">Пе</a>'
    answer += '<a href="tg://user?id=695444908">ре</a>'
    answer += '<a href="tg://user?id=556042536">к</a>'
    answer += '<a href="tg://user?id=829242296">л</a>'
    answer += '<a href="tg://user?id=609459963">и</a>'
    answer += '<a href="tg://user?id=669442518">ч</a>'
    answer += '<a href="tg://user?id=573972437">ка</a>'
    await message.answer(answer)
