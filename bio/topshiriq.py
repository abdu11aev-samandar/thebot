from telebot import TeleBot, types

token = "1534785417:AAGl3BrUhAzn_rtkoEsVVWYJwCmAeXtAdp4"
mybot = TeleBot(token)


@mybot.message_handler(commands=["start"])
def send(message):
    my_id = message.chat.id
    tugmalar = types.ReplyKeyboardMarkup(True)
    tugma1 = types.KeyboardButton("Telefon 📞", request_contact=True)
    tugmalar.add(tugma1)
    mybot.send_message(my_id, "Ma'lumot laringizni jo'nating 👇", reply_markup=tugmalar)


@mybot.message_handler(content_types=["contact"])
def sticker(message):
    my_id = message.chat.id
    mybot.forward_message("694558718", my_id, message.id)


mybot.polling()
