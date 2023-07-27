from pyrogram import Client,filters
import json

count = 0
with open('data.json','r') as f:
    data = json.load(f)
count = data['count']
print(count)

@Client.on_message(filters.me & filters.all & filters.text)
async def index(client , message):
    last_msg = message.text
    global count
    txt = 'лох'
    if txt in message.text.lower():
        with open('data.json','w') as f:
            json.dump({"count":count+1},f)
        with open('data.json', 'r') as f:
            data = json.load(f)
        count = data["count"]
        await message.edit(f"{last_msg} \n \n <b><i>Рахунок лохів обновлено - кількість обізваних лохів:</i></b> {count}")
