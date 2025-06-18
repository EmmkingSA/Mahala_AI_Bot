import telebot

BOT_TOKEN = "PASTE-YOUR-BOT-TOKEN-HERE"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your Mahala AI Assistant 🤖. How can I help you today?")

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    bot.reply_to(message, "Got it! I'm working on your request...")

bot.polling()
