from pyrogram import Client
from config import api_id, api_hash

# --------------------------------------------

# --------------------------------------------
commands = dict(root='commands')
app = Client("my_account", api_id=api_id, api_hash=api_hash, plugins=commands)
# --------------------------------------------
app.run()
