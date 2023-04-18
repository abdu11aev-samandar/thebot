from telebot import TeleBot, types

token = "1534785417:AAGl3BrUhAzn_rtkoEsVVWYJwCmAeXtAdp4"
mybot = TeleBot(token)


@mybot.message_handler(content_types=["sticker"])
def sticker(message):
    my_id = message.chat.id
    mybot.copy_message(my_id, my_id, message.id)


@mybot.message_handler(commands=["sticker"])
def send(message):
    my_id = message.chat.id
    tugmalar = types.ReplyKeyboardMarkup(True)
    tugma1 = types.KeyboardButton("Telefon 📞", request_contact=True)
    tugma2 = types.KeyboardButton("Location 🚩", request_location=True)
    tugmalar.add(tugma1)
    tugmalar.add(tugma2)
    mybot.send_message(my_id, "Ma'lumot laringizni jo'nating 👇", reply_markup=tugmalar)


xat = 0


@mybot.message_handler(commands=["help"])
def habar(message):
    xat = mybot.send_message(message.chat.id, "Novvi garak?")
    mybot.register_next_step_handler(habar)


@mybot.message_handler(content_types=["text"])
def habar(message):
    d = ["salom", "nichik", "jollimo"]
    if message.text in d:
        mybot.edit_message_text("Donisholi uka", message.chat.id, xat.id)


mybot.polling()
