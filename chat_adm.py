import config
import os
import telebot
import time

bot = telebot.TeleBot(config.token)


def check_admin(message):
    if message.chat.id != config.admin:
        bot.send_message(message.chat.id, text='Вы не админ!')
    

@bot.message_handler(commands=['add_photo']) 
def add_photo(message):
    if check_admin(message): return
        
    else:
        bot.send_message(config.admin, text='Кидай photo')
        @bot.message_handler(content_types=['photo'])
        
        def handle_docs_photo(message):
            photo_id = message.photo[-1].file_id
            file_info = bot.get_file(photo_id)
            bot.send_message(config.admin, file_info.file_id, reply_to_message_id=file_info.file_id)
            print(message.photo[0:])
           
    time.sleep(3)
    
    
@bot.message_handler(commands=['add_audio']) 
def add_audio(message):
    if check_admin(message): return
        
    else:
        bot.send_message(config.admin, text='Кидай audio')
        @bot.message_handler(content_types=['audio'])

        def handle_docs_audio(message):
            audio_id = message.audio.file_id
            file_info = bot.get_file(audio_id)
            bot.send_message(config.admin, file_info.file_id, reply_to_message_id=file_info.file_id)
        
             
    time.sleep(3)
    
@bot.message_handler(commands=['add_doc']) 
def add_doc(message):
    if check_admin(message): return
        
    else:
        bot.send_message(config.admin, text='Кидай файл')
        @bot.message_handler(content_types=['document'])

        def handle_docs_document(message):
            document_id = message.document.file_id
            file_info = bot.get_file(document_id)
            bot.send_message(config.admin, file_info.file_id, reply_to_message_id=file_info.file_id)
           
    time.sleep(3)



if __name__ == '__main__':
    bot.infinity_polling()