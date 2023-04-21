"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
import os
import requests
import pandas as pd
import csv

from datetime import timedelta, datetime
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API')

today = datetime.now()
date_start = (today + timedelta(days=5)).strftime("%m-%d")

sms = []

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


#Есть ли у кого др через 5 дней?
with open('birthdays.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if date_start in row:
            sms.append(row[3])

# Отправка сообщения в тг
BOT_API_KEY = os.getenv('API')
MY_CHANNEL_NAME = '@aiogramtestoleg'
MY_MESSAGE_TEXT = f'у {sms} день рождения через 5 дней'

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