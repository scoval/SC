from telebot import TeleBot
import telebot
import sqlite3

bot = telebot.TeleBot('6347964034:AAF19tipETd3ecArbcOQCG2s8e0-xgBh1ac')

# @SeCovalbot
# API = 6347964034:AAF19tipETd3ecArbcOQCG2s8e0-xgBh1ac

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('SeCovalbot.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрируем! Введите ваше имя')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    pass

bot.polling(none_stop=True)