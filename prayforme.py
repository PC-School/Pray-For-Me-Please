import telebot
from telebot import types
import sqlite3

user_data = {}

bot = telebot.TeleBot('7428507460:AAG-wGHPbIGYqvC0LS97Z9Tq4DTn6qHkaP8')

@bot.message_handler(commands=['start'])
def askname(message):
	bot.send_message(message.chat.id, "<b>Мир вам! Как вас зовут?</b>", parse_mode='HTML')
	bot.register_next_step_handler(message, start)

def start(message):
	btn = types.InlineKeyboardMarkup()
	user_data[message.chat.id] = {"name": message.text.strip()}
	btn.add(types.InlineKeyboardButton("Помолитесь за меня", callback_data = 'prayer'))
	btn.add(types.InlineKeyboardButton("Хочу поделиться свидетельством", callback_data = 'testimony'))
	bot.send_message(message.chat.id, '<b>Если есть молитвенная нужда, нажмите на кнопку "Помолитесь за меня" или напишите <code>/молитва</code> или /prayer\n\nЕсли хотите поделиться свидетельством, нажмите на кнопку "Хочу поделиться свидетельством" или напишите <code>/свидетельство</code> или /testimony</b>', parse_mode='HTML', reply_markup=btn)
	bot.send_message(message.chat.id, '<b>ЕСЛИ ВЫ ЗАМЕТИЛИ КАКОЙ-ТО БАГ, ПРИ НАПИСАНИИ ИЛИ ПУБЛИКАЦИИ НУЖДЫ ИЛИ СВИДЕТЕЛЬСТВА, ПИШИТЕ @alonagd17</b>', parse_mode='HTML')

@bot.message_handler(commands=['молитва', 'prayer'])
def need(message):
	bot.send_message(message.chat.id, '<b>Напишите свою нужду, если вы хотите, чтобы за вас просто помолились или не хотите называть нужду, то поставьте "-"</b>', parse_mode='HTML')
	bot.register_next_step_handler(message, send_need)

def send_need(message):
	name = user_data.get(message.chat.id, {}).get("name", "Не указано")
	need = message.text.strip()

	info = f"Молитвенная нужда:\n\nИмя: {name}\nНужда: {need}"
	bot.send_message(message.chat.id, info)
	bot.send_message(message.chat.id, '<b>Ваша нужда записана, вы можете увидеть её <a href="https://t.me/PrayForMePleaseChannel">тут</a>. А так же вы можете помолиться за других, как сказано:</b> \n\n<blockquote>Признавайтесь друг пред другом в проступках и молитесь друг за друга, чтобы исцелиться: много может усиленная молитва праведного.\n\nПослание Иакова 5:16</blockquote>', parse_mode='HTML', disable_web_page_preview=True)
	bot.send_message(-1002278314632, info)

@bot.message_handler(commands=['свидетельство', 'testimony'])
def testimony(message):
	bot.send_message(message.chat.id, '<b>Опишите своё свидетельство как можно подробнее</b>', parse_mode='HTML')
	bot.register_next_step_handler(message, send_testimony)

def send_testimony(message):
	name = user_data.get(message.chat.id, {}).get("name", "Не указано")
	need = message.text.strip()

	info = f"Свидетельство:\n\nИмя: {name}\nСвидетельство: {need}"
	bot.send_message(message.chat.id, info)
	bot.send_message(message.chat.id, '<b>Ваше свидетельство записано, вы можете увидеть его <a href="https://t.me/PrayForMePleaseChannel">тут</a>. А так же вы можете помолиться за других, как сказано:</b> \n\n<blockquote>Признавайтесь друг пред другом в проступках и молитесь друг за друга, чтобы исцелиться: много может усиленная молитва праведного.\n\nПослание Иакова 5:16</blockquote>', parse_mode='HTML', disable_web_page_preview=True)
	bot.send_message(-1002278314632, info)


@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
	if callback.data == "prayer":
		need(callback.message)
	elif callback.data == "testimony":
		msg = bot.send_message(callback.message.chat.id, "<b>Напишите своё имя</b>", parse_mode='HTML')
		testimony(callback.message)

bot.polling(none_stop=True)