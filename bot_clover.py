import logging
import ssl
import time
from telegram import Update
from telegram.ext import Updater

from aiohttp import web

import telebot
import config
import os

TOKEN = config.token
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)


bot = telebot.TeleBot(TOKEN)


bot = telebot.TeleBot(TOKEN)

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


updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook('https://botclover.herokuapp.com/' + TOKEN)
updater.idle()



