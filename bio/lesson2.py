# from telebot import TeleBot, types
#
# token = "5508317127:AAEk208nePb0CLy1bcePq1IUp5AS6dFfqzg"
# mybot = TeleBot(token)
#
#
# def hello(message):
#     return message.text == "Hi"
#
#
# @mybot.message_handler(content_types=['text'])
# def habar(message):
#     mybot.delete_message(message.chat.id, message.id)
#
#
# @mybot.message_handler(func=lambda message: message.text == "Hi")
# def hello(message):
#     mybot.reply_to(message, "Hi, how are you")
#
#
# @mybot.message_handler(commands=['Help'])
# def help(message):
#     buttons = types.InlineKeyboardMarkup()
#     button1 = types.InlineKeyboardButton("Instructions for the Girl", callback_data="Instructions")
#     button2 = types.InlineKeyboardButton("Instructions for all Girl", callback_data="AllInstructions")
#     buttons.add(button1)
#     buttons.add(button2)
#     mybot.send_message(message.chat.id, "What kind of help do you need?", reply_markup=buttons)
#
#
# @mybot.callback_query_handler(func=lambda call: True)
# def button_click(call):
#     user_id = call.message.chat.id
#     if call.data == "Instructions":
#         mybot.send_message(user_id, "Check the information")
#     elif call.data == "AllInstructions":
#         mybot.send_message(user_id, "Check all the informations")
#
#
# mybot.polling()
# print('Started')

from telebot import TeleBot
from telebot import types

bot = TeleBot("1534785417:AAGl3BrUhAzn_rtkoEsVVWYJwCmAeXtAdp4")
chat_id = 858948298

button_english = types.InlineKeyboardButton('English', callback_data='english')
button_russian = types.InlineKeyboardButton('Russian', callback_data='russian')
button_uzbek = types.InlineKeyboardButton('Uzbek', callback_data='uzbek')

keyboard = types.InlineKeyboardMarkup()
keyboard.add(button_english)
keyboard.add(button_russian)
keyboard.add(button_uzbek)


@bot.callback_query_handler(func=lambda call: True)
def button_click(call):
    user_id = call.message.chat.id
    if call.data == "english":
        bot.send_message(user_id, "Siz ingliz tilini tanladiz")
        bot.delete_message(user_id, call.message.id)
    elif call.data == "russian":
        bot.send_message(user_id, "Siz rus tilini tanladiz")
        bot.delete_message(user_id, call.message.id)
    elif call.data == "uzbek":
        bot.send_message(user_id, "Siz uzbek tilini tanladiz")
        bot.delete_message(user_id, call.message.id)


bot.send_message(chat_id, text='Tilni tanlang', reply_markup=keyboard)

bot.polling()
# print('Started')