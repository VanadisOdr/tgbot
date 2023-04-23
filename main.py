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
date_forthy = (today + timedelta(days=4)).strftime("%m-%d")
date_three = (today + timedelta(days=3)).strftime("%m-%d")
date_two = (today + timedelta(days=2)).strftime("%m-%d")
date_one = (today + timedelta(days=1)).strftime("%m-%d")


sms1 = []
sms2 = []
sms3 = []
sms4 = []
sms5 = []

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def tg_message5():
    # Отправка сообщения в тг
    BOT_API_KEY = os.getenv('API')
    MY_CHANNEL_NAME = '@aiogramtestoleg'
    MY_MESSAGE_TEXT = f'у {sms5} день рождения через 5 дней'

    response = requests.get(f'https://api.telegram.org/bot{BOT_API_KEY}/sendMessage', {
        'chat_id': MY_CHANNEL_NAME,
        'text': MY_MESSAGE_TEXT
    })

    if response.status_code == 200:
        print('ok')
    else:
        print(response.text)  # Do what you want with response

def tg_message4():
    # Отправка сообщения в тг
    BOT_API_KEY = os.getenv('API')
    MY_CHANNEL_NAME = '@aiogramtestoleg'
    MY_MESSAGE_TEXT = f'у {sms4} день рождения через 4 дней'

    response = requests.get(f'https://api.telegram.org/bot{BOT_API_KEY}/sendMessage', {
        'chat_id': MY_CHANNEL_NAME,
        'text': MY_MESSAGE_TEXT
    })

    if response.status_code == 200:
        print('ok')
    else:
        print(response.text)  # Do what you want with response

def tg_message3():
    # Отправка сообщения в тг
    BOT_API_KEY = os.getenv('API')
    MY_CHANNEL_NAME = '@aiogramtestoleg'
    MY_MESSAGE_TEXT = f'у {sms3} день рождения через 3 дня'

    response = requests.get(f'https://api.telegram.org/bot{BOT_API_KEY}/sendMessage', {
        'chat_id': MY_CHANNEL_NAME,
        'text': MY_MESSAGE_TEXT
    })

    if response.status_code == 200:
        print('ok')
    else:
        print(response.text)  # Do what you want with response

def tg_message2():
    # Отправка сообщения в тг
    BOT_API_KEY = os.getenv('API')
    MY_CHANNEL_NAME = '@aiogramtestoleg'
    MY_MESSAGE_TEXT = f'у {sms2} день рождения через 2 дня'

    response = requests.get(f'https://api.telegram.org/bot{BOT_API_KEY}/sendMessage', {
        'chat_id': MY_CHANNEL_NAME,
        'text': MY_MESSAGE_TEXT
    })

    if response.status_code == 200:
        print('ok')
    else:
        print(response.text)  # Do what you want with response

def tg_message1():
    # Отправка сообщения в тг
    BOT_API_KEY = os.getenv('API')
    MY_CHANNEL_NAME = '@aiogramtestoleg'
    MY_MESSAGE_TEXT = f'у {sms1} день рождения через 1 день'

    response = requests.get(f'https://api.telegram.org/bot{BOT_API_KEY}/sendMessage', {
        'chat_id': MY_CHANNEL_NAME,
        'text': MY_MESSAGE_TEXT
    })

    if response.status_code == 200:
        print('ok')
    else:
        print(response.text)  # Do what you want with response

#Есть ли у кого др через 5 дней?
with open('birthdays.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if date_start in row:
            sms5.append(row[3])
            print(sms5)
        if date_forthy in row:
            sms4.append(row[3])
            print(sms4)
        if date_three in row:
            sms3.append(row[3])
            print(sms3)
        if date_two in row:
            sms2.append(row[3])
            print(sms2)
        if date_one in row:
            sms1.append(row[3])
            print(sms1)


for l in zip(sms1,sms2,sms3,sms4,sms5):
    if len(sms1) > 0:
        tg_message1()
        sms1.clear()
    if len(sms2) > 0:
        tg_message2()
        sms2.clear()
    if len(sms3) > 0:
        tg_message3()
        sms3.clear()
    if len(sms4) > 0:
        tg_message4()
        sms4.clear()
    if len(sms5) > 0:
        tg_message5()
        sms5.clear()
    else:
        print('Пока без дней рождений')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

