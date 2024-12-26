import telebot
from telebot import types
import sqlite3

user_data = {}

bot = telebot.TeleBot('7428507460:AAG-wGHPbIGYqvC0LS97Z9Tq4DTn6qHkaP8')

@bot.message_handler(commands=['start'])
def start(message):
	conn = sqlite3.connect('needs.sql')
	conn1 = sqlite3.connect('testimony.sql')
	cursor = conn.cursor()
	cursor.execute('CREATE TABLE IF NOT EXISTS needs (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, need TEXT NOT NULL)')
	cursor.execute('CREATE TABLE IF NOT EXISTS testimony (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, testimony TEXT NOT NULL)')
	conn.commit()
	conn1.commit()
	cursor.close()
	conn.close()
	conn1.close()

	btn = types.InlineKeyboardMarkup()
	btn.add(types.InlineKeyboardButton("Помолитесь за меня", callback_data = 'prayer'))
	btn.add(types.InlineKeyboardButton("Хочу поделиться свидетельством", callback_data = 'testimony'))
	bot.send_message(message.chat.id, '<b>Мир вам! Если есть молитвенная нужда, нажмите на кнопку "Помолитесь за меня" или напишите <code>/молитва</code> или /prayer\nЕсли хотите поделиться свидетельством, нажмите на кнопку "Хочу поделиться свидетельством" или напишите <code>/свидетельство</code> или /testimony</b>', parse_mode='HTML', reply_markup=btn)
	bot.send_message(message.chat.id, '<b>ЕСЛИ ВЫ ЗАМЕТИЛИ КАКОЙ-ТО БАГ, ПРИ НАПИСАНИИ ИЛИ ПУБЛИКАЦИИ НУЖДЫ ИЛИ СВИДЕТЕЛЬСТВА, ПИШИТЕ @alonagd17</b>', parse_mode='HTML', reply_markup=btn)

@bot.message_handler(commands=['молитва', 'prayer'])
def askname(message):
	bot.send_message(message.chat.id, "<b>Напишите своё имя</b>", parse_mode='HTML')
	bot.register_next_step_handler(message, need)

def need(message):
	user_data[message.chat.id] = {"name": message.text.strip()}
	bot.send_message(message.chat.id, '<b>Напишите свою нужду, если вы хотите, чтобы за вас просто помолились или не хотите называть нужду, то поставьте "-"</b>', parse_mode='HTML')
	bot.register_next_step_handler(message, database)

def database_need(message):
	need = message.text.strip()

	if message.chat.id in user_data and "name" in user_data[message.chat.id]:
		name = user_data[message.chat.id]["name"]
	else:
		name = "Не указано"

	conn = sqlite3.connect('needs.sql')
	cursor = conn.cursor()
	cursor.execute('INSERT INTO needs (name, need) VALUES (?, ?)', (name, need))
	conn.commit()

	cursor.execute('SELECT * FROM needs WHERE id = (SELECT MAX(id) FROM needs)')
	result = cursor.fetchone()

	info = f"Имя: {result[1]}\nНужда: {result[2]}"
	bot.send_message(message.chat.id, info)
	bot.send_message(message.chat.id, '<b>Ваша нужда записана, вы можете увидеть её <a href="https://t.me/PrayForMePleaseChannel">тут</a>. А так же вы можете помолиться за других, как сказано:</b> \n\n<blockquote>Признавайтесь друг пред другом в проступках и молитесь друг за друга, чтобы исцелиться: много может усиленная молитва праведного.\n\nПослание Иакова 5:16</blockquote>', parse_mode='HTML', disable_web_page_preview=True)
	channel_message = f"Молитвенная нужда:\n\nИмя: {result[1]}\nНужда: {result[2]}"
	bot.send_message(-1002278314632, channel_message)
	cursor.close()
	conn.close()

@bot.message_handler(commands=['testimony', 'свидетельство'])
def askname(message):
	bot.send_message(message.chat.id, "<b>Напишите своё имя</b>", parse_mode='HTML')
	bot.register_next_step_handler(message, testimony)

def testimony(message):
	user_data[message.chat.id] = {"name": message.text.strip()}
	bot.send_message(message.chat.id, '<b>Опишите своё свидетельство как можно подробнее</b>', parse_mode='HTML')
	bot.register_next_step_handler(message, database)

def database_testimony(message):
	testimony = message.text.strip()

	if message.chat.id in user_data and "name" in user_data[message.chat.id]:
		name = user_data[message.chat.id]["name"]
	else:
		name = "Не указано"

	conn1 = sqlite3.connect('testimony.sql')
	cursor = conn.cursor()
	cursor.execute('INSERT INTO testimony (name, testimony) VALUES (?, ?)', (name, testimony))
	conn.commit()

	cursor.execute('SELECT * FROM testimony WHERE id = (SELECT MAX(id) FROM testimony)')
	result = cursor.fetchone()

	info = f"Имя: {result[1]}\nНужда: {result[2]}"
	bot.send_message(message.chat.id, info)
	bot.send_message(message.chat.id, '<b>Ваше свидетельство записано, вы можете увидеть его <a href="https://t.me/PrayForMePleaseChannel">тут</a>. А так же вы можете помолиться за других, как сказано:</b> \n\n<blockquote>Признавайтесь друг пред другом в проступках и молитесь друг за друга, чтобы исцелиться: много может усиленная молитва праведного.\n\nПослание Иакова 5:16</blockquote>', parse_mode='HTML', disable_web_page_preview=True)
	channel_message = f"Свидетельство:\n\nИмя: {result[1]}\nСвидетельство: {result[2]}"
	bot.send_message(-1002278314632, channel_message)
	cursor.close()
	conn.close()


@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
	if callback.data == "prayer":
		msg = bot.send_message(callback.message.chat.id, "<b>Напишите своё имя</b>", parse_mode='HTML')
		bot.register_next_step_handler(msg, need)
	elif callback.data == "testimony":
		msg = bot.send_message(callback.message.chat.id, "<b>Напишите своё имя</b>", parse_mode='HTML')
		bot.register_next_step_handler(msg, testimony)

bot.polling(none_stop=True)