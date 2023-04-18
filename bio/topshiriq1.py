from telebot import TeleBot, types

token = "1534785417:AAGl3BrUhAzn_rtkoEsVVWYJwCmAeXtAdp4"
mybot = TeleBot(token)


@mybot.message_handler(commands=['raspisaniya'])
def jadval(message):
    file = open("img.png", "rb")
    mybot.send_photo(message.chat.id, file, "bu raspisaniya")


mybot.polling()
