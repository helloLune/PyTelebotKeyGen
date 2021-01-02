from utils import keygen, log
from json import loads, dumps
import re

import telebot
from telebot.types import InlineKeyboardMarkup as inline, InlineKeyboardButton as btn

# bot id for tests @showkeygen_bot
bot = telebot.TeleBot(
	"1491925610:AAESZB3GGZBFQSI7iZXK55j0QZ9_wdJPQX0"
)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	btns = inline(row_width=2)
	btns.add(
		btn('🔗 from 10', callback_data='key_gen_10'),
		btn('🔗 from 15', callback_data='key_gen_15'),
		btn('🔗 from 20', callback_data='key_gen_20'),
		btn('🔗 from 25', callback_data='key_gen_25')
	)
	bot.reply_to(
		message, 
		"👋 Sup, i\'m keygen bot.\n"+
		"⚙️ I can generate key with any length.\n"+
		"📍 Choose length & enjoy:)",
		reply_markup=btns
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

log('bot started.')
bot.set_update_listener(
	lambda msgs: [
		log('[',msg.from_user.first_name,'] -', msg.text ) for msg in msgs
	]
)
bot.polling()