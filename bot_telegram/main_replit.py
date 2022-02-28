import os
import teleBot

API_KEY = os.getenv('5141763004:AAHv0lLKh0RhkysUuK_jQ5DznInK5YLENDI')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(command=['Oi Polis'])
def oipolis(message):
    bot.reply_to(message,"Oi polis!!!!")

bot.polling|()