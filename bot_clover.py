import logging
import os
from queue import Queue

import cherrypy
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher

import config 

class SimpleWebsite(object):
    @cherrypy.expose
    def index(self):
        return """<H1>Welcome!</H1>"""


class BotComm(object):
    exposed = True

    def __init__(self, TOKEN, NAME):
        super(BotComm, self).__init__()
        self.TOKEN = TOKEN
        self.NAME=NAME
        self.bot = telegram.Bot(self.TOKEN)
    
        try:
            self.bot.setWebhook('https://{}.herokuapp.com/{}'.format(self.NAME, self.TOKEN))
        except:
            raise RuntimeError('Failed to set the webhook')
        
        self.updater = Updater(TOKEN, use_context=True)

        self.update_queue = Queue()
        self.dp = Dispatcher(self.updater, self.update_queue)

        self.dp.add_handler(CommandHandler('start', self.start))
        self.dp.add_handler(MessageHandler(Filters.text & ~Filters.command, self.echo))
        self.dp.add_error_handler(self.dispatch_error)

    @cherrypy.tools.json_in()
    def POST(self, *args, **kwargs):
        update = cherrypy.request.json
        update = telegram.Update.de_json(update, self.bot)
        self.dp.process_update(update)

    def dispatch_error(self, error, update):
        cherrypy.log('Error occurred - {}'.format(error))

    def start(self, updater, update):
        update.effective_message.reply_text('Ку')


    def echo(self, updater, update):
        update.effective_message.reply_text(update.effective_message.text)


if __name__ == '__main__':
    
    TOKEN = config.token
    NAME = config.nameapp

    
    PORT = os.environ.get('PORT', 8443)

    
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    
    cherrypy.config.update({'server.socket_host': '0.0.0.0', })
    cherrypy.config.update({'server.socket_port': int(PORT), })
    cherrypy.tree.mount(SimpleWebsite(), "/")
    cherrypy.tree.mount(BotComm(TOKEN, NAME),
                        "/{}".format(TOKEN),
                        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})
    cherrypy.engine.start()