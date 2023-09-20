from aiogram import types
from filters import IsPrivate
from loader import dp
from keyboards.inline.inline_markup import add_group

# Echo bot
@dp.message_handler(IsPrivate(),state=None)
async def bot_echo(message: types.Message):
    await message.answer("Bu botdan faqat gruhda foydalanishingiz mumkin",reply_markup=add_group)
