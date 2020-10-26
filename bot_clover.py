import telebot
import cherrypy
import config
import os

WEBHOOK_HOST = 'botclover.herokuapp.com'
WEBHOOK_PORT = 8443
WEBHOOK_LISTEN = '0.0.0.0'

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (config.token)

BOT_MAILBOX = 'https://botclover.herokuapp.com'

print('connecting_tg')

bot = telebot.TeleBot(config.token)

print('bot started')

class WebhookServer(object):
    @cherrypy.expose
    def WEBHOOK_HOST(self):
        if 'content-length' in cherrypy.request.headers and 'content-type' in cherrypy.request.headers and  cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            requests.post(BOT_MAILBOX, data=json_string)
            return ''
        
        else:
            raise cherrypy.HTTPError(403)
            



@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    print('request')
    bot.reply_to(message, message.text)

bot.remove_webhook()

bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH)
print(bot.set_webhook)

cherrypy.config.update({
    'server.socket_host': WEBHOOK_LISTEN,
    'server.socket_port': WEBHOOK_PORT
})

cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/': {}})

