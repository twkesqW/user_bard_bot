from pyrogram import Client,filters
from config import get_api_id ,get_api_hash

api_id = get_api_id()
api_hash = get_api_hash()

plugins = dict(root='plugins')
app = Client("my_account",api_id=api_id , api_hash=api_hash , plugins=plugins)


app.run()