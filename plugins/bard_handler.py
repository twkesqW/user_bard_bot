from pyrogram import Client,filters
import time
from utils.bard import get_ans
@Client.on_message(filters.me & filters.command(["bard"],prefixes="$"))
async def bard(client,message):
    start = time.time()
    msg = message.text.replace('$bard','').lstrip()
    res = get_ans(msg)
    end = round(time.time() - start)
    await message.edit(f'Bard:\n \n{res} \n \n Час виконання <b>{end}s</b>')