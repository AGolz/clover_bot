import requests  
import datetime

import config 

token = config.token 
class botHandler:
    def __init__(self, token = token):
        self.token = config.token
        self.apiURL = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset = None, timeout = 30):
        params = {'timeout':timeout, 'offset':offset}
        method = 'getUpdates'
        response = requests.get(self.apiURL + method, data=params)
        respJson = response.json()['result']
        return respJson

    def get_last_update(self):
        result = self.get_updates()
        if len(result) > 0:
            update_last = result[-1]
        else:
            update_last = result[len(result)]
        return update_last

    def get_chat_id(update):
        chat_id = update['message']['chat']['id']
        return chat_id

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        response = requests.post(self.apiURL + method, data=params)
        return response

def main():
    bot = botHandler(token)
    
    off_set_next = None
    bot.get_updates(off_set_next)
    
    last_update = bot.get_last_update()
    last_update_id = last_update['update_id']
    last_chat_id = last_update_id['message']['chat']['id']
    bot.send_message(last_chat_id, 'Ky')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
