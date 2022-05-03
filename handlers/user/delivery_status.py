
from aiogram.types import Message
from loader import dp, db
from .menu import call, about
from filters import IsUser


@dp.message_handler(IsUser(), text=call)
async def process_delivery_status(message: Message):
    await message.answer("Biz bilan bog'laning: +998 99 994 78 34 ")


@dp.message_handler(IsUser(), text=about)
async def send_about(message: Message):
    await message.answer("Biz haqimizda endi yoziladide")


async def delivery_status_answer(message, orders):

    res = ''

    for order in orders:

        res += f'Заказ <b>№{order[3]}</b>'
        answer = [
            ' лежит на складе.',
            ' уже в пути!',
            ' прибыл и ждет вас на почте!'
        ]

        res += answer[1]
        res += '\n\n'

    await message.answer(res)