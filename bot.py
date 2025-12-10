import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("Profil"),
        KeyboardButton("Kaloriyani hisoblash"),
    )
    markup.add(
        KeyboardButton("Taom qo‘shish"),
        KeyboardButton("Statistika")
    )
    bot.reply_to(message, "Assalomu alaykum Janobim! Menyuni tayyorlab qo‘ydim.", reply_markup=markup)

bot.infinity_polling()
