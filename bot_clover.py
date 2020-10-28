import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

import config 

PORT = int(os.environ.get('PORT', '5000'))


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = config.token


def start(update, context):
    update.message.reply_text('привет')

def help(update, context):
    update.message.reply_text('на помощь')

def echo(update, context):
    update.message.reply_text(update.message.text)

def error(update, context):
    logger.warning('Update %s" caused error "%s"', update, context.error)

def main():
    updater = Updater(TOKEN, use_context=True)
    
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    
    dp.add_handler(MessageHandler(Filters.text, echo))
    
    dp.add_error_handler(error)

    updater.start_webhook(listen='0.0.0.0',
                          port=PORT,
                          url_path=TOKEN)
    updater.bot.set_webhook('https://botclover.herokuapp.com/' + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()