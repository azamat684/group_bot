from aiogram import types
from filters import IsGroup,AdminFilter
from loader import dp,db,bot 
from aiogram.dispatcher.filters import Command
import sqlite3

@dp.message_handler(IsGroup(), Command("start", prefixes="!/"), AdminFilter())
async def start_group(message: types.Message):
    chat_id = message.chat.id
    title = message.chat.title
    try:
        db.add_group(group_id=chat_id,title=title)
        await message.reply(f"{title} gruhi bazaga qo'shildi")
    except sqlite3.IntegrityError:
        await message.reply(f"{title} gruhi bazaga oldin qo'shilgan")