# --------- DOCS 
# In the first place create chat_ids.txt

import telebot

TOKEN = '6366196039:AAGyDNxMDbFYo09RhgJmOcfojbIrOKbSU6s'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])

def send_welcome(message):
	chat_id = message.chat.id
	first_name = message.from_user.first_name
	bot.send_message(chat_id, f"Hello! <b>{first_name}</b>\nYour chat ID is: <b>{chat_id}</b>\nType something to start messaging.\n\n Bot built by @Xusanboy_Tursunov", parse_mode='HTML')
	with open('chat_ids.txt', 'r+') as f:
		chat_ids = f.read().splitlines()
		if str(chat_id) not in chat_ids:
			f.write(str(chat_id) + '\n')

def send_message_to_all(message_text):
    try:
        with open('chat_ids.txt', 'r') as f:
            chat_ids = f.read().splitlines()
    except FileNotFoundError:
         print('Not Found chat_ids.txt')

    for chat_id in chat_ids:
        try:
            bot.send_message(chat_id, message_text, parse_mode='HTML')
        except Exception as e:
            print(f"Failed to send message to chat ID {chat_id}. Error: {e}")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    send_message_to_all(f"User <b>{message.from_user.first_name}</b> [@{message.from_user.username}] said: <i>{message.text}</i>")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()