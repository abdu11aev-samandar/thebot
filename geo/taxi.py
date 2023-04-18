import telebot
import random

# Telegram bot tokenini o'zgartiring
TOKEN = "1534785417:AAGl3BrUhAzn_rtkoEsVVWYJwCmAeXtAdp4"
bot = telebot.TeleBot(TOKEN)

# Telefon raqamini saqlash uchun global o'zgaruvchilar
phone_number = ""
location = ""


# Telefon raqamini olish uchun tugma
@bot.message_handler(commands=['start'])
def send_phone_number(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = telebot.types.KeyboardButton(text="Telefon raqamni yuborish", request_contact=True)
    keyboard.add(button)
    bot.send_message(chat_id=message.chat.id, text="Telefon raqamingizni yuboring:", reply_markup=keyboard)


# Telefon raqamini qabul qilish uchun handler
@bot.message_handler(content_types=['contact'])
def get_phone_number(message):
    global phone_number
    phone_number = message.contact.phone_number
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = telebot.types.KeyboardButton(text="Hozir qayerdaman?", request_location=True)
    keyboard.add(button)
    bot.send_message(chat_id=message.chat.id, text="Hozir qayerda ekanligingizni belgilang:", reply_markup=keyboard)


# Geolokatsiyani qabul qilish uchun handler
@bot.message_handler(content_types=['location'])
def get_location(message):
    global location
    location = "{}, {}".format(message.location.latitude, message.location.longitude)
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = telebot.types.KeyboardButton(text="Qayerga borayapman?", request_location=True)
    keyboard.add(button)
    car_number = generate_car_number()
    bot.send_message(chat_id=message.chat.id, text="Sizning mashina raqamingiz: {}".format(car_number),
                     reply_markup=keyboard)


# Random mashina raqamini generatsiya qilish uchun funksiya
def generate_car_number():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    car_number = "".join(random.choice(letters + numbers) for _ in range(3))
    car_number += " "
    car_number += "".join(random.choice(letters + numbers) for _ in range(3))
    car_number += " "
    car_number += "".join(random.choice(letters + numbers) for _ in range(3))
    return car_number


# Botni ishga tushirish
bot.polling(none_stop=True)
