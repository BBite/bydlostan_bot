from aiogram import types
from random import randint

from loader import dp


@dp.message_handler(commands='poslaty_bydlo')
async def poslaty_bydlo(message: types.Message):
    answers = \
        {
            1: 'Іди нахуй!',
            2: 'Сєбав нахуй, Бидло!',
            3: 'Уєбан, іди нахуй!',
            4: 'Коньчене створіння, іди нахуй звідси!'
        }
    answer_num = randint(1, 4)
    await message.answer(answers[answer_num])


# @dp.message_handler(
#     lambda message: message.text and "Павло" in message.from_user.full_name)
# async def poslaty_pavla(message: types.Message):
#     await message.answer('Я твою ласточку вкрав і у вихлопну від\'єбав')


@dp.message_handler()
async def reply_echo(message: types.Message):
    max_num = 5
    answers = \
        {
            1: 'Іди нахуй!',
            2: 'Сєбав нахуй, Бидло!',
            3: 'Уєбан, іди нахуй!',
            4: 'Коньчене створіння, іди нахуй звідси!',
            5: 'Яке ти тупе!'
        }
    if "Влад" in message.from_user.full_name:
        max_num += 1
        answers[max_num] = 'Владос Хуєсос'
    elif "Павло" in message.from_user.full_name:
        max_num += 1
        answers[max_num] = 'Пішов нахуй, Гей!'
        max_num += 1
        answers[max_num] = 'Твоя тачка гавно!'
        max_num += 1
        answers[max_num] = 'Я твою ласточку вкрав і у вихлопну від\'єбав'
    elif "Данило" in message.from_user.full_name:
        max_num += 1
        answers[max_num] = 'Знов твоя агресія'
    answer_num = randint(1, max_num)
    await message.reply(answers[answer_num])
