import telebot
from transliterate import translit

bot = telebot.TeleBot("6173903669:AAHBYYw22WMFKOFPygpZBFAWGE0plPIXb6I")


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Salom! Menga kirill harflari bilan yozing va men ularni lotinchaga aylantiraman.")


@bot.message_handler(func=lambda message: True)
def transliterate_message(message):
    text = message.text
    transliterated_text = translit(text, 'ru', reversed=True)
    bot.reply_to(message, transliterated_text)



bot.polling()