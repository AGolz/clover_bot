import logging
import os
from queue import Queue
 
import cherrypy
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext import Dispatcher, CallbackQueryHandler, CallbackContext

import config 
from bot_handlers import GenericComm
from chat_adm import AdmComm

class Website(object):
    @cherrypy.expose
    def index(self):
        return """<H1>Hi! Look for me in telegram @Padraig_clover_bot ;)</H1>"""
    index.exposed = True
        
class ManageBot(object):
    exposed = True
 
    def __init__(self, TOKEN, NAME):
        super(ManageBot, self).__init__()
        self.TOKEN = TOKEN
        self.NAME=NAME
        self.bot = telegram.Bot(self.TOKEN)
        
        try:
            self.bot.setWebhook("https://{}.herokuapp.com/{}".format(self.NAME, self.TOKEN))
        except:
            raise RuntimeError("Failed to set the webhook")
 
        self.update_queue = Queue()
        self.dp = Dispatcher(self.bot, self.update_queue, use_context=True)
 
        self.dp.add_handler(CommandHandler("start", GenericComm.start))
        self.dp.add_handler(CommandHandler("test", AdmComm.test))
        self.dp.add_handler(MessageHandler(Filters.text, GenericComm.echo))
        
    
        
    @cherrypy.tools.json_in()
    def POST(self, *args, **kwargs):
        update = cherrypy.request.json
        update = telegram.Update.de_json(update, self.bot)
        self.dp.process_update(update)
        print(update)
              
    
if __name__ == '__main__':
    
    TOKEN = config.token
    NAME = config.nameapp
    
    PORT = os.environ.get('PORT')
 
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    cherrypy.config.update({'server.socket_host': '0.0.0.0', })
    cherrypy.config.update({'server.socket_port': int(PORT), })
    cherrypy.tree.mount(Website(), "/", {})
    cherrypy.tree.mount(ManageBot(TOKEN, NAME),"/{}".format(TOKEN),{'/': {'request.dispatch': 
    cherrypy.dispatch.MethodDispatcher()}})
    cherrypy.engine.start()
    
    print("Bot started")