from typing import Dict
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from telegram.ext import ContextTypes, Application, CommandHandler, ConversationHandler, MessageHandler, filters

INFO_TURI, INFO_YOZISH, INFO_BOSHQA, LOKATSIYA, KONTAKT = range(5)

reply_markup = ReplyKeyboardMarkup([
    ['F.I.Sh', 'Yoshi'],
    ['Telefon', 'Lokatsiya'],
    ["Boshqa ma'lumot"],
    ["/tugat"]],
    one_time_keyboard=True
)


def format_str(user_data: Dict[str, str]) -> str:
    facts = [f"{key} - {value}" for key, value in user_data.items()]
    return "\n".join(facts).join(["\n", "\n"])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Hush kelibsiz, quyidagi tugmalardan birini bosing", reply_markup=reply_markup)
    return INFO_TURI


async def info_tanlandi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = update.message.text
    context.user_data['info_turi'] = text
    await update.message.reply_text("Endi ma'lumotni kiriting")
    return INFO_YOZISH


async def lokatsiya_tanlandi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = update.message.text
    context.user_data['info_turi'] = text
    await update.message.reply_text("Lokatsiyangizni yuboring")
    return LOKATSIYA


async def telefon_tanlandi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = update.message.text
    context.user_data['info_turi'] = text
    await update.message.reply_text("Kontaktingizni yuborish uchun pastdagi tugmani bosing",
                                    reply_markup=ReplyKeyboardMarkup([[KeyboardButton('Kontakt ulashish',
                                                                                      request_contact=True)]]))
    return KONTAKT


async def info_saqlash(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    info_turi = context.user_data['info_turi']
    text = update.message.text
    context.user_data[info_turi] = text
    del context.user_data['info_turi']
    await update.message.reply_text(f"Ma'lumotlar saqlandi \n {format_str(context.user_data)}",
                                    reply_markup=reply_markup)
    return INFO_TURI


async def lokatsiya_saqlash(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = update.message.location
    context.user_data['long'] = text.longitude
    context.user_data['lati'] = text.latitude
    del context.user_data['info_turi']
    await update.message.reply_text(f"Ma'lumotlar saqlandi \n {format_str(context.user_data)}",
                                    reply_markup=reply_markup)
    return INFO_TURI


async def kontakt_saqlash(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = update.message.contact
    context.user_data['telefon'] = text.phone_number
    del context.user_data['info_turi']
    await update.message.reply_text(f"Ma'lumotlar saqlandi \n {format_str(context.user_data)}",
                                    reply_markup=reply_markup)
    return INFO_TURI


async def boshqa_malumot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Dastlab ma'lumot turini yozing")
    return INFO_BOSHQA


async def tugat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Suhbat tugatildi \n {format_str(context.user_data)}",
                                    reply_markup=ReplyKeyboardRemove())
    context.user_data.clear()
    return ConversationHandler.END


def main():
    application = Application.builder().token('1534785417:AAGl3BrUhAzn_rtkoEsVVWYJwCmAeXtAdp4').build()

    conversational_handler = ConversationHandler(

        entry_points=[CommandHandler('start', start)],

        states={
            INFO_TURI: [
                MessageHandler(filters.Regex("^F.I.Sh|Yoshi$"), info_tanlandi),
                MessageHandler(filters.Regex("^Lokatsiya$"), lokatsiya_tanlandi),
                MessageHandler(filters.Regex("^Telefon"), telefon_tanlandi),
                MessageHandler(filters.Regex("^Boshqa ma'lumot$"), boshqa_malumot)
            ],

            INFO_YOZISH: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, info_saqlash)
            ],

            INFO_BOSHQA: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, info_tanlandi)
            ],

            LOKATSIYA: [
                MessageHandler(filters.LOCATION, lokatsiya_saqlash)
            ],

            KONTAKT: [
                MessageHandler(filters.CONTACT, kontakt_saqlash)
            ]
        },

        fallbacks=[CommandHandler('tugat', tugat)]
    )

    application.add_handler(conversational_handler)
    application.run_polling()


if __name__ == '__main__':
    main()