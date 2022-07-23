import django
django.setup()

import time
import telebot

from bot_settings import bot_token, chat_id


bot=telebot.TeleBot(bot_token)
    

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(chat_id, '''
Hello, I'm Porter Bot
Getting started
''')


if __name__ == '__main__':
    try:
       bot.polling(none_stop=True) 
    except Exception as e:
       print(e) 
       time.sleep(15)
