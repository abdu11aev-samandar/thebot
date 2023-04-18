from telebot import TeleBot, types

token = "5508317127:AAEk208nePb0CLy1bcePq1IUp5AS6dFfqzg"
mybot = TeleBot(token)


@mybot.message_handler(commands=['start'])
def begin(message):
    buttons = types.ReplyKeyboardMarkup(True)
    buttons.row("Sevara", "XShahlo", "RShahlo")
    buttons.row("Shoira", "Oygul", "Mavluda")
    mybot.send_message(858948298, "Qaysi qiz haqida ma'lumot kerak?", reply_markup=buttons)


@mybot.message_handler(content_types=['text'])
def matn(message):
    if message.text == "Sevara":
        mybot.reply_to(message, "911-19 guruh,kunduzgi ta'lim")
    elif message.text == "RShahlo":
        mybot.reply_to(message, "200-19 Guruh, sirtqi ta'lim")
    elif message.text == "XShahlo":
        mybot.reply_to(message, "200-19 Guruh, sirtqi ta'lim")
    elif message.text == "Shoira":
        mybot.reply_to(message, "200-19 Guruh, sirtqi ta'lim")
    elif message.text == "Oygul":
        mybot.reply_to(message, "200-19 Guruh, sirtqi ta'lim")
    elif message.text == "Mavluda":
        mybot.reply_to(message, "200-19 Guruh, sirtqi ta'lim")
    else:
        mybot.reply_to(message, "Bunday qiz yo'q beda, ket oynoqo!")


mybot.polling()
print('Started')
