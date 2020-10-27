import config
import telebot
from aiohttp import web
import ssl


WEBHOOK_HOST = 'botclover.herokuapp.com'
WEBHOOK_LISTEN = "0.0.0.0"
WEBHOOK_PORT = 8443

API_TOKEN = config.token
WEBHOOK_URL_BASE = "https://{}:{}".format(WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(API_TOKEN)

bot = telebot.TeleBot(API_TOKEN)

app = web.Application()

async def handle(request):
    if request.match_info.get("token") == bot.token:
        request_body_dict = await request.json()
        update = telebot.types.Update.de_json(request_body_dict)
        bot.process_new_updates([update])
        return web.Response()
    else:
        return web.Response(status=403)

app.router.add_post("/{token}/", handle)

help_string = []
help_string.append("*Some bot* - just a bot.\n\n")
help_string.append("/start - greetings\n")
help_string.append("/help - shows this help")


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, "привет")

@bot.message_handler(commands=["help"])
def send_help(message):
    bot.send_message(message.chat.id, "".join(help_string), parse_mode="Markdown")


context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain()

web.run_app(
    app,
    host=WEBHOOK_LISTEN,
    port=WEBHOOK_PORT,
    ssl_context=context,
)
