import time

import telegram
from telegram import Update
from telegram.ext import CallbackQueryHandler, CallbackContext
from telegram.utils import helpers

import config





bot = telegram.Bot(config.token)


def check_admin(update : Update, context : CallbackContext):
    if update.effective_user.id != config.admin:
        user_name = update.effective_user.username
        update.effective_message.reply_text('Access denied for {}.'.format(user_name))
        return update.effective_user.id == config.admin
        
    

class AdmComm(object):
     
    def test(update : Update, context : CallbackContext):
        if check_admin(update, context) == False: return     
        
        else:
            context.bot.send_message(chat_id=config.admin, text='Кидай фото')
            mt = helpers.effective_message_type(update.message)
            print(mt)
            if update.effective_message.photo:
                photo_id = None
                photo_id = update.message.photo[-1].get_file()
                context.bot.send_message(chat_id=config.admin, text=photo_id)
            else:
                update.effective_message.reply_text('это не фото %)')
        
        time.sleep(3)


          