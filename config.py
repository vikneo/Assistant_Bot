import os
from dotenv import load_dotenv
import telebot

load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

mess_to_start = ('Добро пожаловать! <b>{0.first_name}</b>.\n'
                 'Я карманный справочник!\n'
                 'Для просмотра команд нажмите <b>/help</b>')

mess_to_help = '<b>Краткая помощь по командам:</b>\n' \
               'Обещаю: - Скоро будет!'
# ' - <b>/low_price</b> - поиск отелей в городах по минимальным ценам\n' \
# ' - <b>/high_price</b> - поиск отелей в городах по максимальным ценам\n' \
# ' - <b>/best_deal</b> - поиск отелей в городах по диапазону цен\n' \
# ' - <b>/history</b> - история просмотренных результатов'
