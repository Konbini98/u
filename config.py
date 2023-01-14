import os
from telethon import TelegramClient

api_id = os.environ.get('API_ID', 22681384)
api_hash = os.environ.get('API_HASH', '14ae45755537c723aab0564a80d723a9')
bot_token = os.environ.get('BOT_TOKEN', '5945346287:AAE3gmyeGs-oK2UxcgbTDWjr48an4iv-oSY')

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
