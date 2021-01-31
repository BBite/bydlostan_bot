from aiogram import types
from random import randint, random

from loader import dp


@dp.message_handler()
async def reply_bydlo(message: types.Message):
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
    do_reply = random() > 0.9
    if do_reply:
        await message.reply(answers[answer_num])
