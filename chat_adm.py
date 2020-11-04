import time

import telegram
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import CallbackContext, CallbackQueryHandler
from telegram.ext import CommandHandler, ConversationHandler, Filters, MessageHandler

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
        
        return config.PHOTO
        
            
    def photo_add(update : Update, context : CallbackContext):
        photo_id = None
        if update.message.photo:
            photo_id = update.message.photo[-1].file_id
            update.message.reply_text(photo_id)       
            
        return ConversationHandler.END
        



          