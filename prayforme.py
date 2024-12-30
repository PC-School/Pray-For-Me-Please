#main
import telebot
from telebot import types

user_data = {}

bot = telebot.TeleBot('7916731915:AAHZxwTk_wDzb7vbmOhylKg8rVnjuZ2KF0Y')
#/main

#start
@bot.message_handler(commands=['start'])
def check(message):
	btn = types.InlineKeyboardMarkup()
	btn.row(types.InlineKeyboardButton("Подписаться на канал", callback_data='subscribe', url=f"https://t.me/PrayForMePleaseChannel"), types.InlineKeyboardButton("Проверить подписку на канал", callback_data='checksubscribe'))
	bot.send_message(message.chat.id, '<b>Мир вам!\n\nНа связи Молитвенный Бот, который является частью проекта "Pray For Me Please!". Поэтому, перед использованием, прошу подписаться на канал "Pray For Me Please!" 👼</b>', parse_mode='HTML', reply_markup=btn)

def start(message):
	btn = types.InlineKeyboardMarkup()
	btn.row(types.InlineKeyboardButton("Молитва", callback_data='prayer'), types.InlineKeyboardButton("Свидетельство", callback_data='testimony'))
	btn.row(types.InlineKeyboardButton("История покаяния", callback_data='repentance'), types.InlineKeyboardButton("Исповедь", callback_data='confession'))
	bot.send_message(message.chat.id, '<b>Мир вам! 👼\n\nЕсли есть молитвенная нужда, нажмите на кнопку "Молитва" или напишите <code>/молитва</code> или /prayer\n\nЕсли хотите поделиться свидетельством, нажмите на кнопку "Свидетельство" или напишите <code>/свидетельство</code> или /testimony\n\nЕсли хотите рассказать историю о том, как вы пришли к Богу и покаялись, нажмите на кнопку "История покаяния" или напишите <code>/историяпокаяния</code> или /storyrepentance\n\nЕсли хотите исповедовать свой грех, нажмите на кнопку "Исповедь" или напишите <code>/исповедь</code> или /confession</b>', parse_mode='HTML', reply_markup=btn)
	bot.send_message(message.chat.id, '<b>ЕСЛИ ВЫ ЗАМЕТИЛИ КАКОЙ-ТО БАГ ИЛИ ВОЗНИКЛИ ТРУДНОСТИ, ПИШИТЕ @alonagd17</b>', parse_mode='HTML')
#/start

#need
@bot.message_handler(commands=['молитва', 'prayer'])
def asknameprayer(message):
	bot.send_message(message.chat.id, '<b>Имя человека, за которого нужно помолиться: </b>', parse_mode='HTML')
	bot.register_next_step_handler(message, need)

def need(message):
	name = message.text.strip()
	user_data[message.chat.id] = {'name': name}
	bot.send_message(message.chat.id, '<b>Напишите нужду. Если же вы хотите, чтобы просто упоминали в молитвах или не хотите называть нужду, то поставьте "-"</b>', parse_mode='HTML')
	bot.register_next_step_handler(message, send_need)

def send_need(message):
	need = message.text.strip()
	name = user_data.get(message.chat.id, {}).get('name', 'Не указано')
	bot.send_message(message.chat.id, '<b>Ваша нужда записана, вы можете увидеть её <a href="https://t.me/PrayForMePleaseChannel">В МОЛИТВЕННОМ КАНАЛЕ</a> 👼. А так же вы можете помолиться за других, как сказано:</b> \n\n<blockquote>Признавайтесь друг пред другом в проступках и молитесь друг за друга, чтобы исцелиться: много может усиленная молитва праведного.\n\nПослание Иакова 5:16</blockquote>', parse_mode='HTML', disable_web_page_preview=True)
	bot.send_message(-1002278314632, f"<b>Молитвенная нужда:\n\nИмя: </b><i>{name}</i>\n\n<b>Нужда: </b><i>{need}</i>", parse_mode='HTML')
#/need

#testimony
@bot.message_handler(commands=['свидетельство', 'testimony'])
def asknametestimony(message):
	bot.send_message(message.chat.id, '<b>Имя человека, о котором это свидетельство: </b>', parse_mode='HTML')
	bot.register_next_step_handler(message, testimony)

def testimony(message):
	name = message.text.strip()
	user_data[message.chat.id] = {'name': name}
	bot.send_message(message.chat.id, '<b>Опишите свидетельство как можно подробнее</b>', parse_mode='HTML')
	bot.register_next_step_handler(message, send_testimony)

def send_testimony(message):
	testimony = message.text.strip()
	name = user_data.get(message.chat.id, {}).get('name', 'Не указано')
	bot.send_message(message.chat.id, '<b>Ваше свидетельство записано, вы можете увидеть его <a href="https://t.me/PrayForMePleaseChannel">В МОЛИТВЕННОМ КАНАЛЕ</a> 👼. А так же вы можете помолиться за других, как сказано:</b> \n\n<blockquote>Признавайтесь друг пред другом в проступках и молитесь друг за друга, чтобы исцелиться: много может усиленная молитва праведного.\n\nПослание Иакова 5:16</blockquote>', parse_mode='HTML', disable_web_page_preview=True)
	bot.send_message(-1002278314632, f"<b>Свидетельство:\n\nИмя: </b><i>{name}</i>\n\n<b>Свидетельство: </b><i>{testimony}</i>", parse_mode='HTML')
#/testimony

#repentance
@bot.message_handler(commands=['историяпокаяния', 'storyrepentance'])
def asknamerepentance(message):
	bot.send_message(message.chat.id, '<b>Имя покаявшегося человека: </b>', parse_mode='HTML')
	bot.register_next_step_handler(message, repentance)

def repentance(message):
	name = message.text.strip()
	user_data[message.chat.id] = {'name': name}
	bot.send_message(message.chat.id, '<b>Опишите свою историю покаяния</b>', parse_mode='HTML')
	bot.register_next_step_handler(message, send_repentance)

def send_repentance(message):
	repentance = message.text.strip()
	name = user_data.get(message.chat.id, {}).get('name', 'Не указано')
	bot.send_message(message.chat.id, '<b>Ваша история записана, вы можете увидеть её <a href="https://t.me/PrayForMePleaseChannel">В МОЛИТВЕННОМ КАНАЛЕ</a> 👼. А так же вы можете помолиться за других, как сказано:</b> \n\n<blockquote>Признавайтесь друг пред другом в проступках и молитесь друг за друга, чтобы исцелиться: много может усиленная молитва праведного.\n\nПослание Иакова 5:16</blockquote>', parse_mode='HTML', disable_web_page_preview=True)
	bot.send_message(-1002278314632, f"<b>История покаяния:\n\nИмя: </b><i>{name}</i>\n\n<b>История: </b><i>{repentance}</i>", parse_mode='HTML')
#/repentance

#confession
@bot.message_handler(commands=['исповедь', 'confession'])
def asknameconfession(message):
	bot.send_message(message.chat.id, '<b>Имя человека, который исповедуется: </b>', parse_mode='HTML')
	bot.register_next_step_handler(message, confession)

def confession(message):
	name = message.text.strip()
	user_data[message.chat.id] = {'name': name}
	bot.send_message(message.chat.id, '<b>Опишите ваш грех</b>', parse_mode='HTML')
	bot.register_next_step_handler(message, send_confession)

def send_confession(message):
	confession = message.text.strip()
	name = user_data.get(message.chat.id, {}).get('name', 'Не указано')
	bot.send_message(message.chat.id, '<b>Ваша исповедь записана, вы можете увидеть её <a href="https://t.me/PrayForMePleaseChannel">В МОЛИТВЕННОМ КАНАЛЕ</a> 👼. А так же вы можете помолиться за других, как сказано:</b> \n\n<blockquote>Признавайтесь друг пред другом в проступках и молитесь друг за друга, чтобы исцелиться: много может усиленная молитва праведного.\n\nПослание Иакова 5:16</blockquote>', parse_mode='HTML', disable_web_page_preview=True)
	bot.send_message(-1002278314632, f"<b>Исповедание греха:\n\nИмя: </b><i>{name}</i>\n\n<b>Исповедь: </b><i>{confession}</i>", parse_mode='HTML')
#/confession

#buttons
@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
	if callback.data == "prayer":
		asknameprayer(callback.message)
	elif callback.data == "testimony":
		asknametestimony(callback.message)
	elif callback.data == "repentance":
		asknamerepentance(callback.message)
	elif callback.data == "confession":
		asknameconfession(callback.message)
	elif callback.data == "checksubscribe":
		status = bot.get_chat_member("@PrayForMePleaseChannel", callback.from_user.id).status
		if status in ['member', 'administrator', 'creator']:
			bot.send_message(callback.message.chat.id, "<b>Спасибо за подписку! Вы можете пользоваться ботом! 👼</b>", parse_mode='HTML')
			start(callback.message)
		else:
			bot.send_message(callback.message.chat.id, "<b>Для использования бота, пожалуйста, подпишитесь на канал! 👼</b>", parse_mode='HTML')
#/buttons

#infinity working
bot.polling(none_stop=True)
#/infinity working