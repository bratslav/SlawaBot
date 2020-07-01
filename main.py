from telebot import types
from bot import bot  # Импортируем объект бота

import requests


from config import *
from menu import *
from sms import *
from users import *
from my_email import *
from Akcia import *
from geo import *
from anketea import *

@bot.message_handler(content_types=['location'])
def handle_loc(message):
    tekUser = Kepper.find(message)
    if tekUser == -1:
        Kepper.NewChat(message.chat.id)
        tekUser = Kepper.find(message)
    s = requests.Session()
    s.get('https://api.telegram.org/bot{0}/deletemessage?message_id={1}&chat_id={2}'.format(TOKEN, message.message_id,message.chat.id))
    s.get('https://api.telegram.org/bot{0}/deletemessage?message_id={1}&chat_id={2}'.format(TOKEN, tekUser.Last_message.message_id,message.chat.id))
    geophone2(message, tekUser)




@bot.message_handler(commands=["start"])
def inline(message):
    tekUser = Kepper.find(message)
    if tekUser == -1:
        Kepper.NewChat(message.chat.id)
        tekUser = Kepper.find(message)
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Меню", callback_data="Меню")
    but_2 = types.InlineKeyboardButton(text="Акції", callback_data="Акции")
    but_22 = types.InlineKeyboardButton(text=" Реєстрація", callback_data="Логотип")
    but_3 = types.InlineKeyboardButton(text="Наш сайт", url="https://beloesuhoe.com.ua/")
    key.add(but_1, but_2, but_22,but_3)
    key_3 = types.InlineKeyboardMarkup()
    key_3.add(but_3)
#    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAIPbV7Q2Hy8VKowsa2XtFqd0MGAgkAnAAIEAANKy2YlI5qz2TO7-rUZBA')
#    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAIPbl7Q2U07KhAhcJJBKvbrWDRhAnz4AAIFAANKy2Yl_TTZUhVblp4ZBA')
    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAIPal7QsxOw5wJf1UwnmUGBQL9sexgRAAIDAANKy2YlSiKFGzUAAcOgGQQ')
    tekUser.Last_message = bot.send_message(message.chat.id, "Ласкаво просимо до нашого telegram bot", reply_markup=key)


@bot.callback_query_handler(func=lambda c: True)
def inlin(c):
    fa = 0
    tekUser = Kepper.find(c.message)
    if tekUser == -1:
        Kepper.NewChat(c.message.chat.id)
        tekUser = Kepper.find(c.message)
    # print(c.data)
    if c.data == "Меню":
        try:
            delete_last_message(c.message)
            menu(c.message, tekUser)
        except:
            menu(c.message, tekUser)
    elif c.data == "Назад1":
        delete_last_message(c.message)
        menu(c.message, tekUser)
    #        additional(c.message)
    elif c.data == "Автор":
        key = types.InlineKeyboardMarkup()
        but_2 = types.InlineKeyboardButton(text="Відміна", callback_data="Нахер2")
        key.add(but_2)
        print("Авторізація")
        tekUser.init_var()
        tekUser.enter_mode = 1
        tekUser.enter_number = 1
        bot.send_message(c.message.chat.id, 'Введить номер телефону ( 0ХХХХХХХХХ):', reply_markup=key)
    #        avtorizacia(c.message)
    elif c.data == "Профль":
        ShowProfil(c.message, tekUser)
    elif c.data == "ВашаКарта":
        if len(tekUser.karta) == 13:
            show_barcode(c.message, tekUser)
            drawing(c.message, tekUser)
            get_client(c.message, tekUser)
        #            AfterAvtor(c.message, tekUser)
        else:
            bot.send_message(c.message.chat.id, 'Неподходящий формат штрихкода: ' + tekUser.karta)
    elif c.data == "Дополнительно":
        geophone1(c.message, tekUser)
    elif c.data == "Другое":
        anather(c.message, tekUser)
    elif c.data == "НаМыло":
        print("На мыло")
        delete_last_message(c.message)
        tekUser.NumQw1 = 1
        qwect2(c.message, tekUser)
    elif c.data == "Акции":
        Akcii(c.message, tekUser)
    elif c.data == "Логотип":
        # Заполнение анкеты
        tekUser.new_karta_id = ''
        tekUser.new_client_id = ''
        tekUser.new_karta = ''

        delete_last_message(c.message)
        run_anketa(c.message, tekUser)
    elif c.data == "Да":
        print("Да")
        delete_last_message(c.message)
        qwect(c.message, tekUser)
    elif c.data == "Нет":
        print("Нет")
        delete_last_message(c.message)
        menu(c.message, tekUser)
    elif c.data == "ДаЗапись":
        print("Да запись")
        delete_last_message(c.message)
        record_profil(c.message, tekUser)
    elif c.data == "Ме":
        tekUser.pol = 'Чоловік'
        delete_last_message(c.message)
        qwect(c.message, tekUser)
    elif c.data == "Жо":
        tekUser.pol = 'Жінка'
        delete_last_message(c.message)
        qwect(c.message, tekUser)
    elif c.data == "Бонусы":
        print('Бонусы')
        try:
            delete_last_message(c.message)
            bonus(c.message, tekUser)
        except:
            bonus(c.message, tekUser)
    elif c.data == "НахерМыло":
        print("НахерМыло")
        tekUser.enter_mode = 0
        tekUser.enter_email_name = 0
        tekUser.enter_email_phone = 0
        try:
            delete_last_message(c.message)
            menu(c.message, tekUser)
        except:
            menu(c.message, tekUser)

    elif c.data == "Нахер":
        print("Нахер")
        tekUser.enter_mode = 0
        tekUser.enter_pol = 0
        tekUser.enter_fam = 0
        tekUser.enter_im = 0
        tekUser.enter_jn = 0
        tekUser.enter_dr = 0
        tekUser.enter_ob = 0
        tekUser.enter_rn = 0
        tekUser.enter_gr = 0
        tekUser.enter_tl = 0
        tekUser.enter_em = 0
        delete_last_message(c.message)
        menu(c.message, tekUser)
    elif c.data == "Нахер2":
        print("Нахер авторизацию")
        tekUser.enter_mode = 0
        tekUser.enter_number = 0
        try:
            delete_last_message(c.message)
            menu(c.message, tekUser)
        except:
            menu(c.message, tekUser)
    elif c.data == "Нахер3":
        print("Нахер sms")
        tekUser.enter_mode = 0
        tekUser.enter_sms = 0
        try:
            delete_last_message(c.message)
            menu(c.message, tekUser)
        except:
            menu(c.message, tekUser)
    else:
        for Card in tekUser.Cards:
            if c.data == Card[2]:
                print(Card[2])
                tekUser.karta_id = Card[0]
                tekUser.client_id = Card[1]
                tekUser.karta = Card[2]
                get_client(c.message, tekUser)
                AfterAvtor(c.message, tekUser)
#        handle_text_messages(c.message)


@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    print(message.text)
    tekUser = Kepper.find(message)
    if tekUser == -1:
        Kepper.NewChat(message.chat.id)
        tekUser = Kepper.find(message)
    if tekUser.enter_mode == 1:
        if tekUser.enter_number == 1:
            tekUser.enter_mode = 0
            tekUser.enter_number = 0
            tekUser.phone_nuber = message.text
            avtorSMS(message, tekUser)

        elif tekUser.enter_sms == 1:
            tekUser.enter_mode = 0
            tekUser.enter_sms_number = 0
            if message.text == tekUser.sms_kod:
                # tekUser.phone_nuber = message.text
                #            print(tekUser.phone_nuber)
                welcom_user(message, tekUser)
            else:
                wronans(message, tekUser)
        #        elif tekUser.enter_pol == 1: # Вводим пол
        #            tekUser.enter_mode = 0
        #            tekUser.enter_pol = 0
        #            tekUser.pol = message.text
        #            qwect(message,tekUser)
        elif tekUser.enter_fam == 1:  # Вводим фамилию
            tekUser.enter_mode = 0
            tekUser.enter_fam = 0
            tekUser.fam = message.text
            print('Пишем фамилию')
            delete_last_message(message)
            qwect(message, tekUser)
        elif tekUser.enter_im == 1:  # Вводим Имя
            tekUser.enter_mode = 0
            tekUser.enter_im = 0
            tekUser.name = message.text
            delete_last_message(message)
            qwect(message, tekUser)
        elif tekUser.enter_jn == 1:  # Вводим Отчество
            tekUser.enter_mode = 0
            tekUser.enter_jn = 0
            tekUser.otch = message.text
            tekUser.full_name = tekUser.fam + ' ' + tekUser.name + ' ' + tekUser.otch
            delete_last_message(message)
            qwect(message, tekUser)
        elif tekUser.enter_dr == 1:  # Вводим Дата рождения
            tekUser.enter_mode = 0
            tekUser.enter_dr = 0
            tekUser.birth_date = message.text
            delete_last_message(message)
            qwect(message, tekUser)
        elif tekUser.enter_ob == 1:  # Вводим Область
            tekUser.enter_mode = 0
            tekUser.enter_ob = 0
            tekUser.oblast = message.text
            delete_last_message(message)
            qwect(message, tekUser)
        elif tekUser.enter_rn == 1:  # Вводим Район
            tekUser.enter_mode = 0
            tekUser.enter_rn = 0
            tekUser.rajon = message.text
            delete_last_message(message)
            qwect(message, tekUser)
        elif tekUser.enter_gr == 1:  # Вводим город
            tekUser.enter_mode = 0
            tekUser.enter_gr = 0
            tekUser.gorod = message.text
            delete_last_message(message)
            qwect(message, tekUser)
        elif tekUser.enter_tl == 1:  # Вводим телефон
            tekUser.enter_mode = 0
            tekUser.enter_tl = 0
            tekUser.phone = message.text
            delete_last_message(message)
            qwect(message, tekUser)
        elif tekUser.enter_em == 1:  # Вводим Email
            tekUser.enter_mode = 0
            tekUser.enter_em = 0
            tekUser.email = message.text
            delete_last_message(message)
            finish(message, tekUser)
        elif tekUser.enter_email_name == 1:
            print('Имя для мэйла')
            tekUser.enter_mode = 0
            tekUser.enter_email_name = 0
            tekUser.email_name = message.text
            delete_last_message(message)
            qwect2(message, tekUser)
        elif tekUser.enter_email_phone == 1:
            print('Телефон для мэйла')
            tekUser.enter_mode = 0
            tekUser.enter_email_phone = 0
            tekUser.email_phone = message.text
            delete_last_message(message)
            qwect2(message, tekUser)
        elif tekUser.enter_email_letter == 1:
            print('Сообщение для мэйла')
            tekUser.enter_mode = 0
            tekUser.enter_email_letter = 0
            tekUser.email_letter = message.text
            text = ''
            send_email(message, tekUser, text)
    else:
        if message.text == 'Привет':
            bot.send_message(message.from_user.id, 'Привет')
        elif message.text == "Слава":
            bot.send_message(message.from_user.id, 'Привет Слава!')
        elif message.text == "назад":
            AfterAvtor(message, tekUser)
        else:
            bot.send_message(message.from_user.id, tekUser.chat_id)
#        bot.send_message(message.from_user.id, 'Не розумію. Напишить щось інше.')



@bot.message_handler(content_types=['document', 'audio', 'photo', 'sticker'])
def handle_document_audio(message):
    print(message)

def delete_last_message(message):
    tekUser = Kepper.find(message)

    s = requests.Session()
    s.get('https://api.telegram.org/bot{0}/deletemessage?message_id={1}&chat_id={2}'.format(TOKEN, message.message_id,message.chat.id))
    try:
        s.get('https://api.telegram.org/bot{0}/deletemessage?message_id={1}&chat_id={2}'.format(TOKEN, tekUser.Last_message.message_id,message.chat.id))
    except:
        print('Лажа')


def geophone(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    button_geo = types.KeyboardButton(text="Віправити геолокацію", request_location=True)
    button_nazad = types.KeyboardButton(text="назад", request_location=False)
    keyboard.add(button_geo, button_nazad)
    bot.send_message(message.chat.id,
                     "Обери вариант:",
                     reply_markup=keyboard)


if __name__ == '__main__':
    Kepper = MyKeeper()
    bot.polling(none_stop=True)