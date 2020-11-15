import time

from telegram import Update
from telegram.ext import CallbackQueryHandler, CallbackContext
import config
from postgre_sql import PostgreSQL

class GenericComm(object):
   
    def start(update : Update, context : CallbackContext):
        update.effective_message.reply_text("Ку")
        time.sleep(3)
                  
    def music_get(update : Update, context : CallbackContext):
        config.column_id = 101
        psql = PostgreSQL()
        file_id = psql.extract_id()
        context.bot.send_audio(chat_id=update.effective_chat.id, audio=file_id)
        time.sleep(3)
        
