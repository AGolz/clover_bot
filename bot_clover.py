import logging
import os
from queue import Queue

import cherrypy
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher

import config 

class Website(object):
    @cherrypy.expose
    def index(self):
        return """<H1>Hi! Look for me in telegram @Padraig_clover_bot ;)</H1>"""
    index.exposed = True
    
    
class Root_bot(object):
    exposed = True

    def __init__(self, TOKEN, NAME):
        super(Root_bot, self).__init__()
        self.TOKEN = TOKEN
        self.NAME=NAME
        self.bot = telegram.Bot(self.TOKEN)
        
        try:
            self.bot.setWebhook("https://{}.herokuapp.com/{}".format(self.NAME, self.TOKEN))
        except:
            raise RuntimeError("Failed to set the webhook")

        self.update_queue = Queue()
        self.dp = Dispatcher(self.bot, self.update_queue)

        self.dp.add_handler(CommandHandler("start", self._start))
        self.dp.add_handler(MessageHandler(Filters.text, self._echo))
        self.dp.add_error_handler(self._error)
        
    @cherrypy.tools.json_in()
    def POST(self, *args, **kwargs):
        update = cherrypy.request.json
        update = telegram.Update.de_json(update, self.bot)
        self.dp.process_update(update)
        
    def _start(self, bot, update):
        update.effective_message.reply_text("Ку")
            
    def _echo(self, update, bot):
        update.effective_message.reply_text(update.effective_message.text)
        
    def _error(self, error, update):
        cherrypy.log("Error occurred - {}".format(error))
        
    
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
    cherrypy.tree.mount(Root_bot(TOKEN, NAME),"/{}".format(TOKEN),{'/': {'request.dispatch': 
    cherrypy.dispatch.MethodDispatcher()}})
    cherrypy.engine.start()

    
    