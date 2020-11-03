
from telegram import Update, update
from telegram.ext import CallbackQueryHandler, CallbackContext




def start(bot, update : Update, context : CallbackContext):
        update.effective_message.reply_text("Ку")
            
def echo(bot, update : Update, context : CallbackContext):
        update.effective_message.reply_text(update.message.text)