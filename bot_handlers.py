import time
from telegram import Update
from telegram.ext import CallbackQueryHandler, CallbackContext
from telegram.ext.dispatcher import run_async


class GenericComm(object):
   
    @staticmethod
    @run_async
    def start(update : Update, context : CallbackContext):
        update.effective_message.reply_text("Ку")
        
    
    
    @staticmethod  
    @run_async      
    def echo(update : Update, context : CallbackContext):
        update.effective_message.reply_text(update.message.text)
        