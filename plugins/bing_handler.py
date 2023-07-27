import time
from pyrogram import Client, filters
from utils.bing import get_ans_bing

@Client.on_message(filters.me & filters.command(["bing"],prefixes="$"))
def bing(client,message):
    start = time.time()
    msg = message.text.replace('$bing','').strip()
    if msg.endswith('-creative'):
        res = get_ans_bing(msg,"creative")
    elif msg.endswith('-balanced'):
        res =  get_ans_bing(msg,"balanced")
    elif msg.endswith('-precise'):
        res = get_ans_bing(msg,"precise")
    else:
        res = get_ans_bing(msg,"balanced")
    end = round(time.time() - start)
    message.edit(f'Bing:\n \n{res} \n \nЧас виконання <b>{end}s</b>')