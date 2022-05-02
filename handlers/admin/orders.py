

from aiogram.types import Message
from loader import dp, db
from handlers.user.menu import orders
from filters import IsAdmin


@dp.message_handler(IsAdmin(), text=orders)
async def process_orders(message: Message):
    
    orders = db.fetchall('SELECT * FROM orders')
    products = db.fetchall('SELECT * FROM products')
    
    if len(orders) == 0:
        await message.answer('У вас нет заказов.')
    else:
        await order_answer(message, orders, products)


async def order_answer(message, orders, products):

    res = ''
    # resp = ''

    for order in orders:
        res += f'Заказы <b>от {order[1]}</b>\nНомер телефона: {order[2]}\nНазвания товара: {order[3]}\n\n'

        # print(res)
    # for product in products:
    #     result += f'Названия товара: {product[5]}\n'

    await message.answer(res)
    # await message.answer(result)