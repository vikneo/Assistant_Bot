import telebot
from telebot import types
from config import bot, mess_to_start, mess_to_help


@bot.message_handler(commands=['start'])
def start(message: types.Message) -> None:
    try:
        # user_id = select_user(user_id=message.chat.id)[0]
        bot.send_message(message.chat.id,
                         text=f'Рад тебя снова видеть <b>{message.from_user.first_name}</b> 😎\n'
                              f'Не знаешь с чего начать, жми <b>/help</b>', parse_mode='HTML')
    except Exception as e:
        bot.send_message(message.chat.id,
                         mess_to_start.format(message.from_user),
                         parse_mode='HTML')


@bot.message_handler(commands=['help'])
def helps(message: telebot.types.Message) -> None:
    try:
        # user_id = select_user(user_id=message.chat.id)[0]
        bot.send_message(message.chat.id, mess_to_help, parse_mode='HTML')
    except Exception as err:
        # logger.error(f"Пользователь не зарегистрирован. Описание: {err}")
        bot.send_message(message.chat.id, 'Для начало работы нажми /start')


@bot.message_handler(content_types=['text'])
def text(message: types.Message) -> None:
    bot.send_message(message.chat.id,
                     text='Скоро мы сможем и поговорить\n'
                          'а сейчас для помощи нажмите <b>/help</b>',
                     parse_mode='HTML'
                     )


bot.polling(none_stop=True)
