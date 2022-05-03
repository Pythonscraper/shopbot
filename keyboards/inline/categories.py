from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from loader import db

category_cb = CallbackData('category', 'id', 'action')


def categories_markup():

    global category_cb
    
    markup = InlineKeyboardMarkup(row_width=2)
    for idx, title in db.fetchall('SELECT * FROM categories'):
        markup.row(InlineKeyboardButton(title, callback_data=category_cb.new(id=idx, action='view')))

    return markup
