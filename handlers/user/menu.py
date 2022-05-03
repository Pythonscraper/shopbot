from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
from loader import dp
from filters import IsAdmin, IsUser

catalog = '🛍️ Buyurtma berish'
about = 'ℹ Biz haqimizda'
call = '💬 Biz bilan aloqa'
# balance = '💰 Balans'
cart = '🛒 Savat'
# delivery_status = '🚚 Статус заказа'


settings = '⚙️ Настройка каталога'
orders = '🚚 Заказы'
questions = '❓ Вопросы'


@dp.message_handler(IsAdmin(), commands='adminmenu')
async def admin_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True, resize_keyboard=True)
    markup.add(settings)
    markup.add(questions, orders)

    await message.answer('Меню', reply_markup=markup)


@dp.message_handler(IsUser(), commands='menu')
async def user_menu(message: Message):
    menu = ReplyKeyboardMarkup(selective=True, resize_keyboard=True)
    menu.add(catalog)
    menu.add(about, cart)
    menu.add(call)

    await message.answer('Меню', reply_markup=menu)
