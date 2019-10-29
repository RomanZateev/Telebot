import telebot
import json
import random

from telebot.types import Message
from telebot import apihelper

apihelper.proxy = {
 "https": "http://146.88.51.237:80",
}

bot = telebot.TeleBot("972242987:AAEBckYsY4kxn9C362DCCfdNUH8p4NNOsKM")

# setWebhook нужен сертификат
# bot.set_webhook(url="http://example.com", certificate=open('mycert.pem'))
# unset webhook
# bot.remove_webhook()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, 
    "Привет! Меня зовут Брокулятор и я помогу тебе найти брокера под твой запрос. Я знаком с 7 лучшими брокерами, у которых есть нужные лицензии. Все они проверены временем и тысячами клиентов, так что предложу тебе парочку хороших вариантов.")
'''
with open('questions.json') as json_file:
    data = json.load(json_file)
'''
@bot.message_handler(commands=['go'])
def send_welcome(message: Message):
	bot.reply_to(message.text, "Zdarova")

bot.polling(timeout=60)