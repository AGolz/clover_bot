from telegram import Update
from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
import telebot
import config
import os

TOKEN = config.token
PORT = int(os.environ.get('PORT', '8443'))

updater = Updater(TOKEN)
dispatcher = updater.dispatcher


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def webhook(update):
    update_queue.put(update)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="привет")
    
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)




updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook('https://botclover.herokuapp.com/' + TOKEN)
updater.idle()



