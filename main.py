import telebot
from telebot.types import Message
from datebase.core import init_db
from datebase.crud import add_tg_user, get_user_from_id, add_message, get_messages_by_user
from c import API_TOKEN


bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    user = get_user_from_id(message.from_user.id)
    if user:
        new_text = f'Привет! {user.first_name}, Ты был в первый раз {user.time_add}'
        bot.send_message(message.from_user.id, new_text)
        print(">>>>>>>>>>>>>>>", user)

    else:
        data = {
            'telegram_id': message.from_user.id,
            'username': message.from_user.username,
            'first_name': message.from_user.first_name
        }
        add_tg_user(data)
    bot.reply_to(message, 'Привет!')

@bot.message_handler(commands=['mess'])
def all_mess(message: Message):
    messages = get_messages_by_user(message.from_user.id)
    new_mess = [mess.tex_message for mess in messages]
    bot.send_message(message.from_user.id, '\n'.join(new_mess))




# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message: Message):
    add_message(message.text, message.from_user.id)
    bot.reply_to(message, f'Твоё сообщение {message.text}')



init_db()

bot.infinity_polling()

