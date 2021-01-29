from aiogram import types
from random import randint

from loader import dp


@dp.message_handler()
async def poslaty_bydlo(message: types.Message):
    answers = \
        {
            1: 'Іди нахуй!',
            2: 'Сєбав нахуй, Бидло!',
            3: 'Уєбан, іди нахуй!',
            4: 'Коньчене створіння, іди нахуй звідси!',
            5: 'Яке ти тупе!'
        }
    answer_num = randint(1, 5)
    if not message.media_group_id:
        await message.answer(answers[answer_num])
