from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def add_group(username):
    url = f'http://t.me/{username}?startgroup=new'
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton(text = "👥 Gruhga qo'shish ➕",url=url))
    return markup