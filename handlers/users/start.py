import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
import aiogram
from loader import dp, db, bot
from keyboards.inline.inline_markup import add_group
from filters import IsPrivate


@dp.message_handler(IsPrivate(),CommandStart(),state="*")
async def bot_start(message: types.Message,state: FSMContext):
    await state.finish()
    name = message.from_user.full_name
    bot_username = await bot.get_me()
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,name=name)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        if message.from_user.username is not None: 
            msg = f"Bazaga yangi foydalanuvchi qo'shildi\n🙎🏻‍♂️ Ismi: <a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a>\n🆔 ID si: <code>{message.from_user.id}</code>\n✉️ Foydalanuvchi nomi: @{message.from_user.username}\n✡️ Telegram tili: {message.from_user.language_code}\n\nBazada {count} ta foydalanuvchi bor"
            await bot.send_message(chat_id=ADMINS[0], text=msg,parse_mode='HTML')
        else:
            msg = f"Bazaga yangi foydalanuvchi qo'shildi\n🙎🏻‍♂️ Ismi: <a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a>\n🆔 ID si: <code>{message.from_user.id}</code>\n✡️ Telegram tili: {message.from_user.language_code}\n\nBazada {count} ta foydalanuvchi bor."
            await bot.send_message(chat_id=ADMINS[0], text=msg,parse_mode='HTML')
        await message.answer(f"Xush kelibsiz {name}!\nBu botdan faqat gruhda foydalanishingiz mumkin",reply_markup=add_group(username=bot_username.username))
    except sqlite3.IntegrityError as err:
        if message.from_user.username is not None: 
            msg = f"Bazaga yangi foydalanuvchi qo'shildi\n🙎🏻‍♂️ Ismi: <a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a>\n🆔 ID si: <code>{message.from_user.id}</code>\n✉️ Foydalanuvchi nomi: @{message.from_user.username}\n✡️ Telegram tili: {message.from_user.language_code}"
            await bot.send_message(chat_id=ADMINS[0], text=msg,parse_mode='HTML')
        else:
            msg = f"Bazaga yangi foydalanuvchi qo'shildi\n🙎🏻‍♂️ Ismi: <a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a>\n🆔 ID si: <code>{message.from_user.id}</code>\n✡️ Telegram tili: {message.from_user.language_code}"
            await bot.send_message(chat_id=ADMINS[0], text=msg,parse_mode='HTML')

        await message.answer(f"Xush kelibsiz {name}!\nBu botdan faqat gruhda foydalanishingiz mumkin",reply_markup=add_group(username=bot_username.username))
