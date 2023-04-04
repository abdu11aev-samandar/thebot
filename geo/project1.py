from telegram.ext import CommandHandler
import time
from telegram import Update, ReplyKeyboardMarkup, Bot
from telegram.ext import Updater, CallbackContext, CallbackQueryHandler, Filters, MessageHandler

TOKEN = '1534785417:AAGl3BrUhAzn_rtkoEsVVWYJwCmAeXtAdp4'
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

ask_reply_markup = ReplyKeyboardMarkup([['Random cat']], resize_keyboard=True)
chat_id = 858948298  # замените на свое значение, подробнее ниже
bot = Bot("1534785417:AAGl3BrUhAzn_rtkoEsVVWYJwCmAeXtAdp4")


def send_random_cat(update: Update, context: CallbackContext) -> None:
    url = f'https://cataas.com/cat?t=${time.time()}'
    bot.send_photo(chat_id, url)


def summa(update, context):
    s = update.message.text.split(' ')
    if len(s) != 3:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='No command argument')
    else:

        a = int(s[1])
        b = int(s[2])
        c = a + b
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=c)


def kopaytma(update, context):
    s = update.message.text.split(' ')
    if len(s) != 3:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Xatolik")
    else:
        a = int(s[1])
        b = int(s[2])
        d = a * b
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=d)


def ekub(update, context):
    s = update.message.text.split(' ')
    if len(s) != 3:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='No command argument')
    else:
        M = int(s[1])
        N = int(s[2])
        while M != N:
            if M > N:
                M = M - N
            else:
                N = N - M
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=N)


def ekuk(update, context):
    s = update.message.text.split(' ')
    if len(s) != 3:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='No command argument')
    else:
        M = int(s[1])
        N = int(s[2])
        while M != N:
            if M > N:
                M = M - N
            else:
                N = N - M
    ekuk = (M * N) / N
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=ekuk)


def tub(update, context):
    s = update.message.text.split(' ')
    if len(s) != 2:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='No command argument')
    else:
        M = int(s[0])
        for num in range(M + 1):
            prime = True
            for i in range(2, num - 1):
                if num % i == 0:
                    prime = False
            if prime:
                context.bot.send_message(chat_id=update.effective_chat.id, text=num)


def main() -> None:
    updater = Updater("1534785417:AAGl3BrUhAzn_rtkoEsVVWYJwCmAeXtAdp4")

    kopaytma_handler = CommandHandler('kopaytma', kopaytma)
    dispatcher.add_handler(kopaytma_handler)

    summ_handler = CommandHandler('summa', summa)
    dispatcher.add_handler(summ_handler)

    ekub_handler = CommandHandler('ekub', ekub)
    dispatcher.add_handler(ekub_handler)

    ekuk_handler = CommandHandler('ekuk', ekuk)
    dispatcher.add_handler(ekuk_handler)

    tub_handler = CommandHandler('tub', tub)
    dispatcher.add_handler(tub_handler)

    updater.dispatcher.add_handler(CallbackQueryHandler(send_random_cat, pattern='^send_random_cat'))
    updater.dispatcher.add_handler(
        MessageHandler(Filters.update.message & Filters.text('Random cat'), send_random_cat))

    updater.start_polling()
    print('Started')
    updater.idle()


if __name__ == "__main__":
    main()
