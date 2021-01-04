from utils import get_config

CONFIG = get_config() 


# Import & Init bot

import telebot
from telebot.types import InlineKeyboardMarkup as inline, InlineKeyboardButton as btn
bot = telebot.TeleBot(CONFIG['token'])


# Routing 

@bot.message_handler(commands=['start', 'help']) # Reaction for /start & /help commands
def send_welcome(message):
	bot.send_message(
		message.chat.id, 
		f"This is a '{message.text}' message"
	)

@bot.message_handler(func=lambda message: True)
def echo_all(message): # Repeats your message
	bot.reply_to(
		message, 
		message.text
	)

@bot.callback_query_handler(
	func=lambda call: re.match('key_gen', call.data)
)
def keygen_callback(call):
	*_, n = call.data.split('_')
	key = keygen(int(n))
	btns = inline().add(
		btn('Again', callback_data=call.data)
	)
	bot.answer_callback_query(call.id, 'Genering key...')
	bot.send_message(
		call.from_user.id,
		f"🔑 Your key: {key} ({n})",
		reply_markup=btns
	)