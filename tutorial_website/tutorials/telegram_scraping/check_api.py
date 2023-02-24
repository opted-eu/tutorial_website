import json
from telethon.sync import TelegramClient

with open('secrets.json') as f:
    credentials = json.load(f)

client = TelegramClient('user', credentials['api_id'], credentials['api_hash']).start()

client.send_message('me', 'Hello to myself!')
