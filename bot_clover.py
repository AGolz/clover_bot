
from telegram import Update
from telegram.ext import Updater, dispatcher


import telebot
import config
import os

TOKEN = config.token
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)


bot = telebot.TeleBot(TOKEN)


def webhook(update):
    dispatcher.process_update(update)



@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook('https://botclover.herokuapp.com/' + TOKEN)
updater.idle()



