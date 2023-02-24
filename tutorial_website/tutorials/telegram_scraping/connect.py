import json # to load our API credentials
from telethon.sync import TelegramClient # the Telegram client
from pprint import pprint

with open('secrets.json') as f:
    credentials = json.load(f)

client = TelegramClient('user', credentials['api_id'], credentials['api_hash']).start()

account_name = 'ovalmedia_english'

chat = client.get_entity(account_name)

messages = client.get_messages(chat)
print(messages.total)

message = messages[0]

pprint(message.to_dict())