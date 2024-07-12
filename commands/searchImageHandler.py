from pyrogram import filters, Client
from pyrogram.types import Message, InputMediaPhoto, ReplyKeyboardMarkup,KeyboardButton
from utils.getImage import getImage


@Client.on_message(filters.command("пошук", prefixes=["."]))
async def find(client: Client, message: Message):
    print('Start')
    title = " ".join(message.command[1:])
    res = getImage(title)
    await message.reply_photo(res[0], reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Hi")]]))
    print('End')
