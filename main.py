from telebot import TeleBot
# bot = @scoval_bot
bot = TeleBot('5592490008:AAFPsZWjADKcFe124kZWJ2ESOPjhNl6dtIs')

@bot.message_handler(commands=['start'])
def start(message):
#    mess = f'Привет, <b>{message.from_user.first_name}<u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, '<b>Привет, сейчас тебя зарегистрируем! Введите ваше имя</b>',
                     parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "И тебе привет!", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID:{message.from_user.id}", parse_mode='html')
    elif message.text == "photo":
        photo = open('icon.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вау, какое фото!')


bot.polling(none_stop=True)






