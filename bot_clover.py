import logging
from telegram import Update
from telegram.ext import Updater

import telebot
import config
import os

TOKEN = config.token
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, 'привет')

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


def webhook(update):
    update_queue.put(update)

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook('https://botclover.herokuapp.com/' + TOKEN)
updater.idle()



