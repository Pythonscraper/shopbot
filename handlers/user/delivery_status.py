
from aiogram.types import Message
from loader import dp, db
from .menu import delivery_status, about
from filters import IsUser


@dp.message_handler(IsUser(), text=delivery_status)
async def process_delivery_status(message: Message):
    
    orders = db.fetchall('SELECT * FROM orders WHERE cid=?', (message.chat.id,))
    
    if len(orders) == 0: await message.answer('У вас нет активных заказов.')
    else: await delivery_status_answer(message, orders)


@dp.message_handler(IsUser(), text=about)
async def send_about(message: Message):
    await message.answer('Связь: +998 99 994 78 34')


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