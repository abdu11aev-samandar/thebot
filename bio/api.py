# import requests
# from telebot import TeleBot, types
#
# token = "1534785417:AAGl3BrUhAzn_rtkoEsVVWYJwCmAeXtAdp4"
# mybot = TeleBot(token)
#
# api_key = "dbde4ebe736b6f7c3cee212a"
#
#
# @mybot.message_handler(commands=['start'])
# def begin(call):
#     user_id = call.chat.id
#     buttons = types.ReplyKeyboardMarkup(True)
#     buttons.row("USD", "RUB", "EUR")
#     mybot.send_message(user_id, "Kurs birligini tanlang 👇", reply_markup=buttons)
#
#
# @mybot.callback_query_handler(func=lambda call: True)
# def button_click(call):
#     user_id = call.message.chat.id
#     if call.data == "USD":
#         url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
#         response = requests.get(url)
#         d = response.json()
#         mybot.send_message(user_id, "test")
#     elif call.data == "RUB":
#         url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/RUB"
#         response = requests.get(url)
#         ma = response.json()["conversion_rates"]["UZS"]
#         mybot.send_message(user_id, "test")
#     elif call.data == "EUR":
#         url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/RUR"
#         response = requests.get(url)
#         d = response.json()
#         mybot.send_message(user_id, "test")
#
#
# mybot.polling()
# print('Started')


import requests
from telebot import TeleBot, types

TOKEN = "1534785417:AAGl3BrUhAzn_rtkoEsVVWYJwCmAeXtAdp4"
API_KEY = "dbde4ebe736b6f7c3cee212a"

bot = TeleBot(TOKEN)

button_usd = types.InlineKeyboardButton('USD', callback_data='USD')
button_rub = types.InlineKeyboardButton('RUB', callback_data='RUB')
button_eur = types.InlineKeyboardButton('EUR', callback_data='EUR')

keyboard = types.InlineKeyboardMarkup()
keyboard.add(button_usd)
keyboard.add(button_rub)
keyboard.add(button_eur)


@bot.callback_query_handler(func=lambda call: True)
def button_click(call):
    user_id = call.message.chat.id
    try:
        if call.data == "USD":
            url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
            response = requests.get(url)
            data = response.json()["conversion_rates"]["UZS"]
            bot.send_message(user_id, f"1 USD = {data:.2f} UZS")
        elif call.data == "RUB":
            url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/RUB"
            response = requests.get(url)
            data = response.json()["conversion_rates"]["UZS"]
            bot.send_message(user_id, f"1 RUB = {data:.2f} UZS")
        elif call.data == "EUR":
            url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/EUR"
            response = requests.get(url)
            data = response.json()["conversion_rates"]["UZS"]
            bot.send_message(user_id, f"1 EUR = {data:.2f} UZS")
    except Exception as e:
        bot.send_message(user_id, "Xatolik yuz berdi.")


bot.send_message(858948298, text='Kurs birligini tanlang 👇', reply_markup=keyboard)

bot.polling()
