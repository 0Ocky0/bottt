import telebot
import random
from telebot import types

# 5849232589:AAFRIjVtOzw54sQHO957xTDAxThM7N_Uouc
global if_funt_add
if_funt_add = 0
bot = telebot.TeleBot("5849232589:AAFRIjVtOzw54sQHO957xTDAxThM7N_Uouc")
mas = []
chis = 42


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Я бот гадалка")


@bot.message_handler(commands=['добавь слово'])
def send_welcome(message):
    bot.reply_to(message, "Я жду, пиши слово")


@bot.message_handler(commands=['add'])
def get_words_info(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_dobav = types.InlineKeyboardButton(text='добавь слово', callback_data='dobav')
    item_uberi = types.InlineKeyboardButton(text='убери последнее слово', callback_data='uberi')
    item_packazi = types.InlineKeyboardButton(text='покажи слова', callback_data='pakazi')
    markup_inline.add(item_uberi, item_dobav, item_packazi)
    bot.send_message(message.chat.id, 'чего ты хочешь??', reply_markup=markup_inline)



@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    global if_funt_add
    if call.data == "dobav":
        bot.send_message(call.message.chat.id, 'пиши слово')
        if_funt_add = 1
    elif call.data == "uberi":
        bot.send_message(call.message.chat.id, 'удолил последнее')
        mas.pop(len(mas) - 1)
    elif call.data == "pakazi":
        anss = ''
        if len(mas) == 0:
            anss = 'пусто'
        for el in mas:
            anss += el.text + '\n'
        bot.send_message(call.message.chat.id, anss)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    global if_funt_add
    if(if_funt_add == 1):
        mas.append(message)
        bot.reply_to(message, 'добавил')
        if_funt_add = 0
    else:
        bot.reply_to(message, 'подожди и нажми на кнопку еще раз')


bot.polling()
