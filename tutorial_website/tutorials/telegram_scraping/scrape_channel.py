import json # to load our API credentials
from telethon.sync import TelegramClient # the Telegram client
from pprint import pprint # helper to pretty print
from pathlib import Path # makes handling file paths a breeze

with open('secrets.json') as f:
    credentials = json.load(f)

client = TelegramClient('user', 
                        credentials['api_id'], 
                        credentials['api_hash']).start()

account_name = 'ovalmedia_english'

p = Path.cwd()

output_dir = p / 'output' / account_name
if not output_dir.exists():
    output_dir.mkdir(parents=True)

chat = client.get_entity(account_name)

for message in client.iter_messages(chat):
    print('Retrieving message:', message.id)
    cleaned_message =  {'channel_name': chat.username,
                        'id': message.id,
                        'date': message.date,
                        'content': message.message,
                        'forwards': message.forwards,
                        'views': message.views}
    
    file_name = output_dir / f'{message.id}.json'
    with open(file_name, 'w') as f:
        json.dump(cleaned_message, f, indent=True, default=str)
