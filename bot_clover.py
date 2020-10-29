import logging
import os
import cherrypy
import telegram

import config 

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import bot


@cherrypy.tools.json_in()
def POST(self):
    update = cherrypy.request.json
    update = telegram.Update.de_json(update, bot)
    self.dp.process_update(update)
    
    
def start(update, context):
    update.effective_message.reply_text("Ку")
    
    

def echo(update, context):
    update.effective_message.reply_text(update.effective_message.text)
    
    
def  main ():
    
    TOKEN = config.token
    NAME = config.nameapp
    PORT = os.environ.get('PORT', 8443)
    
    bot = telegram.Bot(TOKEN)

   
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, echo))
    
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()
    
if __name__ == '__main__':
    main()