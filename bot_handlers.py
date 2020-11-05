import time

from telegram import Update
from telegram.ext import CallbackQueryHandler, CallbackContext

class GenericComm(object):
   
    def start(update : Update, context : CallbackContext):
        update.effective_message.reply_text("Ку")
        time.sleep(3)
                  
    def echo(update : Update, context : CallbackContext):
        update.effective_message.reply_text(update.message.text)
        time.sleep(3)
        
