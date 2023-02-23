import telebot

bot = telebot.TeleBot("6078596663:AAH08rGemn_MWA89RYA-WNe_vWUS85iBh70")

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row("Hello", "Bye")

keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row("Date", "Time", "Weekday")

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Hi! Let's Start!")

@bot.message_handler(content_types=["text"])
def send_text(message):

    if message.text.lower() == "hello":
        bot.send_message(message.chat.id, "Hello!", reply_markup=keyboard1)
    elif message.text.lower() == "bye":
        bot.send_message(message.chat.id, "Bye!", reply_markup=keyboard1)
    elif message.text.lower() == "date":
        bot.send_message(message.chat.id, "2/9/23", reply_markup=keyboard2)
    elif message.text.lower() == "time":
        bot.send_message(message.chat.id, "8:40PM", reply_markup=keyboard2)
    elif message.text.lower() == "weekday":
        bot.send_message(message.chat.id, "Thursday", reply_markup=keyboard2)

bot.polling()

# LOCAL DEVELOPMENT
# 1. Open Something In Your Browser.