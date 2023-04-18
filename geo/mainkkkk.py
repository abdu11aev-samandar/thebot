import random
import telebot

TOKEN = '1534785417:AAGl3BrUhAzn_rtkoEsVVWYJwCmAeXtAdp4'
bot = telebot.TeleBot(TOKEN)

questions_list = []

# Test savollarini fayldan o'qish
with open("test_questions.txt", "r", encoding="utf-8") as f:
    content = f.read()

content = content.strip().split("\n\n")

for question in content:
    question = question.split("\n")
    question_text = question[0]
    option1 = question[1].split(") ")[1]
    option2 = question[2].split(") ")[1]
    option3 = question[3].split(") ")[1]
    option4 = question[4].split(") ")[1]
    answer = question[5].split(": ")[1]
    questions_list.append({
        "question": question_text,
        "option1": option1,
        "option2": option2,
        "option3": option3,
        "option4": option4,
        "answer": answer,
        "answered": False,
        "user_answer": ""
    })


# Test savollaridan tasodifiy birini olish
def get_random_question():
    unanswered_questions = [q for q in questions_list if not q["answered"]]
    if len(unanswered_questions) > 0:
        return random.choice(unanswered_questions)
    else:
        return None


# Test natijalarini saqlash
def save_answer(user_id, question, answer):
    for q in questions_list:
        if q["question"] == question:
            q["answered"] = True
            q["user_answer"] = answer
    bot.send_message(user_id, "Javobingiz qabul qilindi!")


# Test yakunlandi deb xabar berish
def end_message(message):
    bot.send_message(message.chat.id, "Test yakunlandi!")
    score = 0
    for q in questions_list:
        if q["answered"] == True:
            if q["user_answer"].lower() == q["answer"].lower():
                score += 1
    bot.send_message(message.chat.id, f"Sizning baholangiz: {score}/{len(questions_list)}")


# Foydalanuvchi javobini tekshirish
def check_answer(message, question):
    user_answer = message.text.lower()
    if user_answer == question["answer"].lower():
        bot.send_message(message.chat.id, "To'g'ri!")
    else:
        bot.send_message(message.chat.id, f"Noto'g'ri. To'g'ri javob {question['answer']}")
    save_answer(message.chat.id, question["question"], user_answer)
    if len(questions_list) > 0:
        question = get_random_question()
        if question is not None:
            sent_question = bot.send_message(
                message.chat.id,
                f"{question['question']}\n\nA) {question['option1']}\nB) {question['option2']}\nC) {question['option3']}\nD) {question['option4']}"
            )
            bot.register_next_step_handler(sent_question, check_answer, question)
        else:
            end_message(message)
    else:
        end_message(message)


# Testni boshlash
@bot.message_handler(commands=['start'])
def start(message):
    if question is not None:
        sent_question = bot.send_message(
            message.chat.id,
            f"{question['question']}\n\nA) {question['option1']}\nB) {question['option2']}\nC) {question['option3']}\nD) {question['option4']}"
        )
        bot.register_next_step_handler(sent_question, check_answer, question)
    else:
        bot.send_message(message.chat.id, "Testga savol qo'shilmagan. Iltimos, administratorga murojaat qiling.")


# Botni ishga tushirish

bot.polling(none_stop=True)
