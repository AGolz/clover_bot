
from telegram import Update, update
from telegram.ext import CallbackQueryHandler, CallbackContext


@staticmethod
def start(update : Update, context : CallbackContext):
        update.effective_message.reply_text("Ку")

@staticmethod           
def echo(update : Update, context : CallbackContext):
        update.effective_message.reply_text(update.message.text)