from telegram.ext import CommandHandler
from telegram.ext import Updater

TOKEN = '1534785417:AAGl3BrUhAzn_rtkoEsVVWYJwCmAeXtAdp4'
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


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


def main() -> None:
    updater = Updater("1534785417:AAGl3BrUhAzn_rtkoEsVVWYJwCmAeXtAdp4")

    ekub_handler = CommandHandler('ekub', ekub)
    dispatcher.add_handler(ekub_handler)

    ekuk_handler = CommandHandler('ekuk', ekuk)
    dispatcher.add_handler(ekuk_handler)

    updater.start_polling()
    print('Started')
    updater.idle()


if __name__ == "__main__":
    main()
