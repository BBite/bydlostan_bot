from aiogram import types

from loader import dp


@dp.message_handler(commands='go_cs')
async def bot_help(message: types.Message):
    answer = ''
    answer += '<a href="tg://user?id=576927517">г</a>'
    answer += '<a href="tg://user?id=695444908">о</a>' + ' '
    answer += '<a href="tg://user?id=556042536">к</a>'
    answer += '<a href="tg://user?id=829242296">с</a>' + ' '
    answer += '<a href="tg://user?id=609459963">г</a>'
    answer += '<a href="tg://user?id=669442518">о</a>'
    await message.answer(answer)


@dp.message_handler(commands='go_payday')
async def bot_help(message: types.Message):
    answer = ''
    answer += '<a href="tg://user?id=576927517">г</a>'
    answer += '<a href="tg://user?id=829242296">о</a>' + ' '
    answer += '<a href="tg://user?id=609459963">пей</a>'
    answer += '<a href="tg://user?id=669442518">дей</a>'
    await message.answer(answer)


@dp.message_handler(commands='go_civilization')
async def bot_help(message: types.Message):
    answer = ''
    answer += '<a href="tg://user?id=576927517">го</a>' + ' '
    answer += '<a href="tg://user?id=829242296">ци</a>'
    answer += '<a href="tg://user?id=669442518">ву</a>'
    await message.answer(answer)


@dp.message_handler(commands='go_civilization_with_paul')
async def bot_help(message: types.Message):
    answer = ''
    answer += '<a href="tg://user?id=576927517">г</a>'
    answer += '<a href="tg://user?id=829242296">о</a>' + ' '
    answer += '<a href="tg://user?id=609459963">ци</a>'
    answer += '<a href="tg://user?id=669442518">ву</a>'
    await message.answer(answer)
