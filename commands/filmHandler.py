from pyrogram import filters, Client

from utils.getDataFilm import getDataFilm


@Client.on_message(filters.command("film",prefixes=[","]))
async def find(client,message):
    title = " ".join(message.command[1:])
    res = getDataFilm(title=title)
    await message.reply_photo(photo=res["image"],caption=f'**Пошук за назвою:** <i>{title}</i> \n \n**Назва:** {res["title"]} \n \n**Опис фільму:** {res["overview"]} \n \n**Оцінка:** --{res["vote"]}--')