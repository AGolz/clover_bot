import time

import telegram
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import CallbackContext, CallbackQueryHandler
from telegram.ext import CommandHandler, ConversationHandler, Filters, MessageHandler
from telegram.utils import helpers

import config


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
            reply_markup=ReplyKeyboardRemove()
        
        return PHOTO
        
            
    def photo_add(update : Update, context : CallbackContext):
        photo_id = None
        photo_id = update.message.photo[-1].get_file()
        context.bot.send_message(chat_id=config.admin, text=photo_id)       
            
        return ConversationHandler.END
        



          