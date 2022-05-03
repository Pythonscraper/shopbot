import os
import handlers
from aiogram import executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from data import config
from loader import dp, db, bot
import filters
import logging

filters.setup(dp)

# WEBAPP_HOST = "0.0.0.0"
# WEBAPP_PORT = int(os.environ.get("PORT", 5000))
user_message = 'Hush kelibsiz'
admin_message = '/admin'



@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):

    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row(user_message)

    text = 'Javohir sizlarni xizmatizda...'
    photo = open('data/assets/javohir.jpg', 'rb')

    await message.answer(f"Assalomu Alaykum <b>{message.from_user.full_name}</b>",reply_markup=markup)
    await message.answer_photo(photo=photo, caption=text)




@dp.message_handler(text=user_message)
async def user_mode(message: types.Message):

    cid = message.chat.id
    if cid in config.ADMINS:
        config.ADMINS.remove(cid)

    await message.answer('Buyurtma berish uchun bosing -> /menu', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text=admin_message)
async def admin_mode(message: types.Message):

    cid = message.chat.id
    if cid not in config.ADMINS:
        config.ADMINS.append(cid)

    await message.answer('Включен админский режим. Нажмите сюда -> /adminmenu', reply_markup=ReplyKeyboardRemove())


# async def on_startup(dp):
#     logging.basicConfig(level=logging.INFO)
#     db.create_tables()
#
#     await bot.delete_webhook()
#     await bot.set_webhook(config.BOT_TOKEN)


async def on_shutdown():
    logging.warning("Shutting down..")
    await bot.delete
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning("Bot down")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

