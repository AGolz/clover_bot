import logging
import ssl

from aiohttp import web

import telebot
import os
import config


WEBHOOK_HOST = 'botclover.herokuapp.com'
WEBHOOK_LISTEN = "0.0.0.0"
WEBHOOK_PORT = int(os.environ['PORT']) 

API_TOKEN = config.token
WEBHOOK_URL_BASE = "https://{}:{}".format(WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(API_TOKEN)

bot = telebot.TeleBot(API_TOKEN)

app = web.Application()

async def handle(request):
    print("WEBHOOK")
    print(request)
    if request.match_info.get("token") == bot.token:
        request_body_dict = await request.json()
        update = telebot.types.Update.de_json(request_body_dict)
        bot.process_new_updates([update])
        return web.Response()
    else:
        return web.Response(status=403)

app.router.add_post("/{token}/", handle)



@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, 'привет')

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


bot.remove_webhook()

print("WEBHOOK SETTING "+WEBHOOK_URL_BASE+WEBHOOK_URL_PATH)
bot.set_webhook(url=WEBHOOK_URL_BASE+WEBHOOK_URL_PATH)
print("WEBHOOK SET")




web.run_app(
    app,
    host=WEBHOOK_LISTEN,
    port=WEBHOOK_PORT,
)