import telebot
from telebot import types
from random import randint as rnd


f_r = open(".env", "r")
variables = dict()
text = f_r.readlines()
for line in text:
	arr = line.rstrip().split('=')
	variables[arr[0]] = arr[1]

f_r.close()
token = variables['token']

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
	img = open("images/mem_button.jfif",'rb')
	markup = types.ReplyKeyboardMarkup()
	buttonPlay = types.InlineKeyboardButton('/play')
	markup.row(buttonPlay)	
	bot.send_photo(message.chat.id, img, caption='This is a bot to test your luck. Write /play to start playing')
	bot.send_message(message.chat.id, 'Press it!', reply_markup=markup)
	
@bot.message_handler(commands=['play'])
def play(message):
	img = open("images/matrix_pills.jfif",'rb')
	bot.send_photo(message.chat.id, img)
	markup = types.InlineKeyboardMarkup()
	buttonR = types.InlineKeyboardButton('Red', callback_data='r')
	buttonB = types.InlineKeyboardButton('Blue', callback_data='b')
	buttonStop = types.InlineKeyboardButton('Stop it!', callback_data='s')
	markup.row(buttonR, buttonB)
	markup.row(buttonStop)
	bot.send_message(message.chat.id, 'Choose the pill', reply_markup=markup)
	
	
@bot.callback_query_handler(func=lambda call: True)
def handle(call):
	if (call.data == 's'):
		bot.send_message(call.message.chat.id, 'Ok')
		bot.answer_callback_query(call.id)
	else:
		res = rnd(1, 2)
		if ((res == 1 and call.data == 'r') or (res == 2 and call.data == 'b')):
			img = open("images/gleb_right.webp",'rb')
			bot.send_photo(call.message.chat.id, img, caption='You were right!')
		else:
			img = open("images/gleb_wrong.webp",'rb')
			bot.send_photo(call.message.chat.id, img, caption='Try again')
		img = open("images/matrix_pills.jfif",'rb')
		bot.send_photo(call.message.chat.id, img)
		markup = types.InlineKeyboardMarkup()
		buttonR = types.InlineKeyboardButton('Red', callback_data='r')
		buttonB = types.InlineKeyboardButton('Blue', callback_data='b')
		buttonStop = types.InlineKeyboardButton('Stop it!', callback_data='s')
		markup.row(buttonR, buttonB)
		markup.row(buttonStop)
		bot.send_message(call.message.chat.id, 'Choose the pill', reply_markup=markup)
		bot.answer_callback_query(call.id)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, "Very interesting...")
	
bot.infinity_polling()
