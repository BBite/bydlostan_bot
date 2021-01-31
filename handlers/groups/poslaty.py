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



