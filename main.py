import telebot
from telebot.types import ReactionTypeEmoji, InlineKeyboardButton, InlineKeyboardMarkup
import os
import random
import requests
bot = telebot.TeleBot('ToKeN')
facts = ['Собрать мусор на пляже или в парке и правильно его утилизировать.',
          'Сделать компост из органических отходов.', 'Убрать дом и правильно все утилизировать.',
          'Посадить растение на балконе или во дворе.',
          'Принять участие в акции по очистке речек, озер или лесов.',
          'Поддержать инициативы по защите природных территорий и животных.',
          'Провести экологический день, в котором все действия будут направлены на сохранение природы и ее богатства.']
@bot.message_handler(commands=["start"])
def help_user(message):
    bot.send_message(message.chat.id, "Привет! Я бот который даёт советы о том как можно уменьшить загрязнения окружающей среды. Пиши команду /help - чтобы узнать все мои команды!")

@bot.message_handler(commands=["help"])
def help_user(message):
    bot.send_message(message.chat.id, "Команды: /fact - присылает один рандомный факт об экологии, /facts - присылает два дополнительных факта о экологии, /nquiz - присылает викторину о знаниях про экологию.")

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

@bot.message_handler(commands=["nquiz"])
def create_poll(message):
    bot.send_message(message.chat.id, "Квиз на знание экологии.")
    answer_options = ["Чтобы сохранить ресурсы для будущих поклений.", "Чтобы улучшить качество воздуха и воды.", "Чтобы защитить биоразнообразие.", "Чтобы предотвратить климатические изменения."]
    bot.send_poll(
        chat_id=message.chat.id,
        question="Зачем нужно заботиться об окружающей среде?",
        options=answer_options,
        type="quiz",
        correct_option_id=3,
        is_anonymous=False,
    )
    
bot.infinity_polling()
