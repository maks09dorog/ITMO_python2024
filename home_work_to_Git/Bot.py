import telebot
import sqlite3
from telebot import types

# pip install pytelegrambotapi

# 7174942059:AAHZb10EMlOna3DSKqAO2NcYm25eATRAmC8

bot = telebot.TeleBot("7174942059:AAHZb10EMlOna3DSKqAO2NcYm25eATRAmC8")
name = None

@bot.message_handler(commands=['start'])
def start(message):
    # БД
    conn = sqlite3.connect('itproger.sql')
    # курсор
    cur = conn.cursor()
    # таблица
    cur.execute('CREATE TABLE IF NOT EXISTS users('
                'id int auto_increment primary key, '
              'name varchar(50), '
              'pass varchar(50))')
    # сохранение в таблицу
    conn.commit()
    # закрытие соединения
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет! Зарегистрируйтесь. Введите имя')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('itproger.sql')
    # курсор
    cur = conn.cursor()
    # добавление пользователя в таблицу
    cur.execute("INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, password))

        # сохранение в таблицу
    conn.commit()
    # закрытие соединения
    cur.close()
    conn.close()

    # кнопки
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, f'Пользователь {name} ! Зарегистрирован.', reply_markup=markup)

# кнопка список пользователей
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('itproger.sql')
    cur = conn.cursor()
    # выбираем все
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'Имя: {el[1]}, пароль: {el[2]}\n'


    # закрытие соединения
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)

bot.polling(non_stop=True)