from pyrogram import filters, Client

from utils.getMonobankData import getMonobankData


@Client.on_message(filters.command("баланс",prefixes=[","]))
async def find(client,message):
    res = ""
    try:
        data = getMonobankData()
        for card in data:
            res += f'''
    <b>Баланс:</b> {card["balance"]/100} грн
    <b>Поповнити по посиланню:</b> <a>send.monobank.ua/{card["sendId"]}</a>
    ----------
    '''
        await message.edit(res)
    except:
        await message.edit("Error")
