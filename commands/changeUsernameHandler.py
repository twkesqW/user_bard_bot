from pyrogram import filters, Client
from pyrogram.types import Message


@Client.on_message(filters.command("нік", prefixes=["."]) & filters.me)
async def find(client: Client, message: Message):
    title = " ".join(message.command[1:])
    await client.update_profile(first_name=title)
    # await message.reply(message.reply_to_message)




