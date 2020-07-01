from bot import bot # Импортируем объект бота
from telebot import types

from config import *

def main_menu(message,tekUser, text):
    if tekUser == -1:
        Kepper.NewChat(message.chat.id)
        tekUser = Kepper.find(message)
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Меню", callback_data="Меню")
    but_2 = types.InlineKeyboardButton(text="Акції", callback_data="Акции")
    but_22 = types.InlineKeyboardButton(text=" Реєстрація", callback_data="Логотип")
    but_3 = types.InlineKeyboardButton(text="Наш сайт", url="https://beloesuhoe.com.ua/")
    key.add(but_1, but_2, but_22, but_3)
    key_3 = types.InlineKeyboardMarkup()
    key_3.add(but_3)
    tekUser.Last_message = bot.send_message(message.chat.id, text, reply_markup=key)


def menu(message,tekUser):
    if tekUser == -1:
        Kepper.NewChat(message.chat.id)
        tekUser = Kepper.find(message)
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Авторізація",  callback_data="Автор")
    but_2 = types.InlineKeyboardButton(text="Геолокація", callback_data="Дополнительно")#,  request_location=True)
#    but_22 = types.InlineKeyboardButton(text="Магазини", callback_data="Магазини")
    but_22 = types.InlineKeyboardButton(text="Магазини", url="https://www.google.com.ua/maps/search/%D0%B1%D0%B5%D0%BB%D0%BE%D0%B5+%D1%81%D1%83%D1%85%D0%BE%D0%B5/@50.408259,30.434082,12.5z?hl=ru")
    but_3 = types.InlineKeyboardButton(text="Інше", callback_data="Другое")
    but_4 = types.InlineKeyboardButton(text="Назад", callback_data="Назад1")
    key.add(but_1, but_2, but_22, but_3,but_4)
    key_3 = types.InlineKeyboardMarkup()
    key_3.add(but_3)
    tekUser.Last_message = bot.send_message(message.chat.id, "Ласкаво просимо до нашого telegram bot", reply_markup=key)

def run_anketa(message: object, tekUser: object) -> object:
    if tekUser == -1:
        Kepper.NewChat(c.message.chat.id)
        tekUser = Kepper.find(c.message)
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Да",  callback_data="Да")
    but_2 = types.InlineKeyboardButton(text="Нет",  callback_data="Нет")
    key.add(but_1, but_2)
    tekUser.NumQw = 1
    tekUser.Last_message = bot.send_message(message.chat.id, "Для реєстрації потрібно заповнити анкету. Починаємо?", reply_markup=key)

def run_record(message: object, tekUser: object) -> object:
    if tekUser == -1:
        Kepper.NewChat(c.message.chat.id)
        tekUser = Kepper.find(c.message)
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Да",  callback_data="ДаЗапись")
    but_2 = types.InlineKeyboardButton(text="Нет",  callback_data="Нет")
    key.add(but_1, but_2)
    tekUser.NumQw = 1
    tekUser.Last_message = bot.send_message(message.chat.id, "Записати в базу даних?", reply_markup=key)


def AfterAvtor(message,tekUser):
    if tekUser == -1:
        Kepper.NewChat(message.chat.id)
        tekUser = Kepper.find(c.message)
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Профіль",  callback_data="Профль")
    but_2 = types.InlineKeyboardButton(text="Ваша картка", callback_data="ВашаКарта")
    but_3 = types.InlineKeyboardButton(text="Кол-во бонусов", callback_data="Бонусы")
    but_4 = types.InlineKeyboardButton(text="Назад", callback_data="Назад1")
    key.add(but_1, but_2, but_3, but_4)
    tekUser.Last_message = bot.send_message(message.chat.id, 'Вітаємо ' + tekUser.full_name, reply_markup=key)

def anather(message,tekUser):
    if tekUser == -1:
        Kepper.NewChat(message.chat.id)
        tekUser = Kepper.find(c.message)
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Вакансії",  url="https://rabota.ua/ua/company6438651")
    but_2 = types.InlineKeyboardButton(text="Зворотній зв'язок", callback_data="НаМыло")
    but_4 = types.InlineKeyboardButton(text="Назад", callback_data="Назад1")
    key.add(but_1, but_2, but_4)
    tekUser.Last_message = bot.send_message(message.chat.id, "Обери вариант:", reply_markup=key)
