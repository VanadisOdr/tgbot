"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
import os
import requests
import pandas as pd

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API')


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")



@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)

def birthday_check():
    pass

def messagetg():
    BOT_API_KEY = os.getenv('API')
    MY_CHANNEL_NAME = '@aiogramtestoleg'
    MY_MESSAGE_TEXT = 'День рождения!'

    response = requests.get(f'https://api.telegram.org/bot{BOT_API_KEY}/sendMessage', {
        'chat_id': MY_CHANNEL_NAME,
        'text': MY_MESSAGE_TEXT
    })

    if response.status_code == 200:
        print('ok')
    else:
        print(response.text)  # Do what you want with response

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)