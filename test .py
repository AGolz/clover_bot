import telebot
import config
import time

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['test']) 

def messages_test(message):
    if message.chat.id != config.admin:
        bot.send_message(message.chat.id, text='ты не админ')
        return
        
    else:
        bot.send_message(config.admin, text='давай файл')
        
        @bot.message_handler(content_types=['audio'])
        def handle_docs_document(message):
            audio_id = message.audio.file_id
            file_info = bot.get_file(audio_id)
            bot.send_message(config.admin, file_info.file_id, reply_to_message_id=file_info.file_id)
           
    
    time.sleep(3)
    



if __name__ == '__main__':
    bot.infinity_polling()