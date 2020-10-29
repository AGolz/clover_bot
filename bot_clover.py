import logging
import os
import cherrypy
import telegram

import config 

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def error(error, update):
        cherrypy.log('Error occurred - {}'.format(error))
    
def start(update, context):
    update.effective_message.reply_text("Ку")

def echo(update, context):
    update.effective_message.reply_text(update.effective_message.text)
    
    
def  main ():
    
    TOKEN = config.token
    NAME = config.nameapp
    PORT = os.environ.get('PORT', 8443)

   
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)
    
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()
    
if __name__ == '__main__':
    main()