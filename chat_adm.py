import config
from telegram import Update, message
from telegram.ext import CallbackQueryHandler, CallbackContext


def check_admin(update : Update, context : CallbackContext):
    user_id = update.effective_user.id
    user_name = update.effective_user.username
    
    if user_id != config.admin:
        update.effective_message.reply_text('Access denied for {}.'.format(user_name))

class AdmComm(object):
           
    @staticmethod 
    @run_async
    def test(update : Update, context : CallbackContext):
        if check_admin(update, context): return
        
        else:
            update.effective_message.reply_text('Кидай фото')
            if message.photo:
                photo_id = update.message.photo[-1].get_file()
                update.effective_message.reply_text(photo_id)


          