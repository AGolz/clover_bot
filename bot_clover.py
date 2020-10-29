import logging
import os
from queue import Queue

import cherrypy
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher

import cost


class Website(object):
    @cherrypy.expose
    def index(self):
        return """<H1>Hi! Look for me in telegram @Padraig_clover_bot ;)</H1>"""


@cherrypy.tools.json_in()
def POST():
    update = cherrypy.request.json
    update = telegram.Update.de_json(update, updater)
    dp.process_update(update)


def dispatch_error(error, update):
    cherrypy.log('Error occurred - {}'.format(error))


def start(update, context):
    update.effective_message.reply_text('Ку')


def echo(update, context):
    update.effective_message.reply_text(update.effective_message.text)


TOKEN = cost.token
NAME = cost.nameapp
PORT = os.environ.get('PORT', 8443)
bot = telegram.Bot(TOKEN)

try:
    bot.setWebhook('https://{}.herokuapp.com/{}'.format(NAME, TOKEN))
except:
    raise RuntimeError('Failed to set the webhook')

updater = Updater(TOKEN, use_context=True)
update_queue = Queue()

dp = Dispatcher(updater, update_queue)

dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

dp.add_error_handler(dispatch_error)


def main():
    exposed = True


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    cherrypy.config.update({'server.socket_host': '0.0.0.0', })
    cherrypy.config.update({'server.socket_port': int(PORT), })
    cherrypy.tree.mount(Website(), "/")
    cherrypy.tree.mount(main(), "/{}".format(TOKEN),
                        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}})
    cherrypy.engine.start()