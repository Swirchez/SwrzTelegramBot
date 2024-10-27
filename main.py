import telebot
from telebot.types import ReactionTypeEmoji, InlineKeyboardButton, InlineKeyboardMarkup
import os
import random
import requests
API_TOKEN = "<api_token>"
bot = telebot.TeleBot('7976398571:AAF1maIY7bVLPR4Frct9YQSM7a8sqroAdUg')
facts = ['Собрать мусор на пляже или в парке и правильно его утилизировать.',
          'Сделать компост из органических отходов.', 'Убрать дом и правильно все утилизировать.',
          'Посадить растение на балконе или во дворе.',
          'Принять участие в акции по очистке речек, озер или лесов.',
          'Поддержать инициативы по защите природных территорий и животных.',
          'Провести экологический день, в котором все действия будут направлены на сохранение природы и ее богатства.']

@bot.message_handler(commands=["fact"])
def fact(message):
    fax = random.choice(facts)
    bot.send_message(message.chat.id, "Что можно сделать для уменьшения загрязнений окружающей среды:")
    bot.send_message(message.chat.id, fax)

def generate_keys():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('1', callback_data='1'),
                InlineKeyboardButton('2', callback_data='2'))
        
    return keyboard
@bot.message_handler(commands=['facts'])
def send_c(message):
    bot.send_message(message.chat.id, 'Вот допольнительные советы для уменьшения загрзений в окружающей среде:', reply_markup=generate_keys())
@bot.callback_query_handler(func= lambda call: True)
def answer(call):
    if call.data == '1':
        bot.send_message(call.message.chat.id, 'Стараться чаще пользоваться велосипедом или общестенным транспортом.')
    elif call.data == '2':
        bot.send_message(call.message.chat.id, 'Сортировать мусор по категориям.')

bot.infinity_polling()
