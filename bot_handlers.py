
from telegram import Update, update
from telegram.ext import CallbackQueryHandler, CallbackContext


def start(Manage_bot, update : Update, context : CallbackContext):
        update.effective_message.reply_text("Ку")
            
def echo(Manage_bot, update : Update, context : CallbackContext):
        update.effective_message.reply_text(update.message.text)