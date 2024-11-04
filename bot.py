import telebot
import os, random
bot = telebot.TeleBot('--------------Bot Teg----------------')

@bot.message_handler(commands=['start'])
def send_meme(message):
    bot.send_message(message.chat.id, 'Send /hello ')                                                               
                                                                                                                    
@bot.message_handler(commands=['hello'])                                                                            
def start_command(message):                                                                                         
    bot.send_message(message.chat.id, "Hi! I'm MessageBot. How are you? (/fine)")


@bot.message_handler(commands=["fine"])
def start_command(message):
    bot.send_message(message.chat.id, "Good! Nice to meet you!")


bot.polling()

