from bot import bot # Импортируем объект бота
from telebot import types
import requests

from config import *
from sms import *
from menu import *
import barcode
from barcode.writer import ImageWriter
import xml.etree.ElementTree as ET
import random
import math

def avtorSMS(message, tekUser):
    if tekUser == -1:
        Kepper.NewChat(message.chat.id)
        tekUser = Kepper.find(message)
    key = types.InlineKeyboardMarkup()
    but_2 = types.InlineKeyboardButton(text="Відміна",  callback_data="Нахер3")
    key.add(but_2)
    print("SMS")
    # Запускаем смс
    x = round(random.uniform(0, 99))
    #           try:
    send_sms(message.text, x)
    tekUser.sms_kod = str(x)
    bot.send_message(message.from_user.id,
                     'На введений номер телефону було відправлено СМС с кодом підтверждння. Введить код підтверждення: (' + str(
                         x) + ')', reply_markup=key)
    tekUser.enter_mode = 1
    tekUser.enter_sms = 1

def wronans(message, tekUser):
    if tekUser == -1:
        Kepper.NewChat(message.chat.id)
        tekUser = Kepper.find(message)
    tekUser.Last_message = bot.send_message(message.from_user.id, 'Не той код. Авторизація не пройдена')
    menu(message, tekUser)

def ChoiseCard(message, tekUser):
    if tekUser == -1:
        Kepper.NewChat(message.chat.id)
        tekUser = Kepper.find(message)
    key = types.InlineKeyboardMarkup()
    for Card in tekUser.Cards:
        #        print(Card)
        but = types.InlineKeyboardButton(text=Card[2], callback_data=Card[2])
        key.add(but)
    tekUser.Last_message = bot.send_message(message.chat.id, "Оберить картку", reply_markup=key)

def get_client(message, tekUser):
    Found = 0
    url = 'http://185.80.232.179:8090/FB570E97-40C5-4690-9037-94E20BC0BC88/clnt?dcardcode=' + tekUser.phone_nuber
#    print('get_client')
    res1 = requests.get(url)

    filename1 = pth + str(tekUser.chat_id) + '1.xml'
    f1 = open(filename1, 'w')
    f1.write(res1.text)
#   print(res1.text)

#    return

    tree = ET.ElementTree(ET.fromstring(res1.text))
    root = tree.getroot()

    error_code1 = root[0][0].text

#    print('ErrorCode =  ', error_code1)
    if error_code1 != '0':
        print('Ошибка получения данных о клиенте')
        tekUser.Last_message = bot.send_message(message.from_user.id, 'Помилка отримання даних...')
    else:
        for child in root:
            if child.tag == 'Results':
                for child1 in child:
                    if child1.tag == 'ResultQuery':
                        Found = 1
                        for child2 in child1:
                            if child2.tag == 'CLNTNAME':
                                full_name = child2.text
                            if child2.tag == 'CLNTBIRTHDAY':
                                s = child2.text
                                print(s)
                                yr = s[0:4]
                                mn = s[4:6]
                                dy = s[6:8]
                            if child2.tag == 'LOCKED':
                                lc = child2.text
#        print('full_name', full_name)
#        print('lc', lc)
        if lc == '0':
            tekUser.name = full_name
            tekUser.full_name = full_name
#            print(dy,mn,yr)
            s = dy
            if mn == '01':
                s = s + ' января ' + yr
            elif mn == '02':
                s = s + ' февраля ' + yr
            elif mn == '03':
                s = s + ' марта ' + yr
            elif mn == '04':
                s = s + ' апреля ' + yr
            elif mn == '05':
                s = s + ' мая ' + yr
            elif mn == '06':
                s = s + ' июня ' + yr
            elif mn == '07':
                s = s + ' июля ' + yr
            elif mn == '08':
                s = s + ' августа ' + yr
            elif mn == '09':
                s = s + ' сентября ' + yr
            elif mn == '10':
                s = s + ' октября ' + yr
            elif mn == '11':
                s = s + ' ноября ' + yr
            elif mn == '12':
                s = s + ' дкаюря ' + yr
            print(s)
            tekUser.birth_date = s
        else:
            tekUser.full_name = ''
            tekUser.birth_date = ''

    url = 'http://185.80.232.179:8090/FB570E97-40C5-4690-9037-94E20BC0BC88/clntformproperty?dcardcode=' + tekUser.phone_nuber
    res1 = requests.get(url)
#    print(res1.text)
    tree = ET.ElementTree(ET.fromstring(res1.text))
    root = tree.getroot()

    error_code1 = root[0][0].text

    if error_code1 != '0':
        print('Ошибка получения данных о клиенте')
        tekUser.Last_message = bot.send_message(message.from_user.id, 'Помилка отримання даних...')
    else:
        for child in root:
            print(child.tag, child.text)
            if child.tag == 'Results':
                for child1 in child:
#                    print(child1.tag, child1.text)
                    if child1.tag == 'ResultQuery':
                        kind_of_data = 0
                        for child2 in child1:
 #                           print(child2.tag, child2.text)
                            if child2.tag == 'CLNTFORMITEMID':
                                # Строка анкеты
                                kind_of_data = child2.text
                            if child2.tag == 'CLNTPROPERTYVAL':
                                if kind_of_data == '1':
                                    tekUser.pol = child2.text
                                    #                                    print('Пол')
                                elif kind_of_data == '2':
                                    tekUser.fam = child2.text
                                    #                                    print('Фамилия')
                                elif kind_of_data == '3':
                                    tekUser.name = child2.text
                                    #                                    print('Имя')
                                elif kind_of_data == '4':
                                    tekUser.otch = child2.text
                                    #                                    print('Отчество')
                                elif kind_of_data == '5':
                                    s = child2.text
                                    yr = s[0:4]
                                    mn = s[4:6]
                                    dy = s[6:8]
                                    s = dy
                                    if mn == '01':
                                        s = s + ' января ' + yr
                                    elif mn == '02':
                                        s = s + ' февраля ' + yr
                                    elif mn == '03':
                                        s = s + ' марта ' + yr
                                    elif mn == '04':
                                        s = s + ' апреля ' + yr
                                    elif mn == '05':
                                        s = s + ' мая ' + yr
                                    elif mn == '06':
                                        s = s + ' июня ' + yr
                                    elif mn == '07':
                                        s = s + ' июля ' + yr
                                    elif mn == '08':
                                        s = s + ' августа ' + yr
                                    elif mn == '09':
                                        s = s + ' сентября ' + yr
                                    elif mn == '10':
                                        s = s + ' октября ' + yr
                                    elif mn == '11':
                                        s = s + ' ноября ' + yr
                                    elif mn == '12':
                                        s = s + ' дкаюря ' + yr
                                    #                                    print(s)
                                    tekUser.birth_date = s
                                    #                                    print('Дата рождения')
                                elif kind_of_data == '6':
                                    tekUser.oblast = child2.text
                                    #                                    print('Область')
                                elif kind_of_data == '7':
                                    tekUser.rajon = child2.text
                                    #                                    print('Район')
                                elif kind_of_data == '8':
                                    tekUser.gorod = child2.text
                                    #                                    print('Город')
                                elif kind_of_data == '9':
                                    tekUser.phone = child2.text
                                    #                                    print('Телефон')
                                elif kind_of_data == '10':
                                    tekUser.email = child2.text
                                    #                                    print('Емайл')


def get_client_id(message, tekUser):
    Found = 0
    tekUser.Cards = []
    url = 'http://185.80.232.179:8090/FB570E97-40C5-4690-9037-94E20BC0BC88/dcard?dcardcode=' + tekUser.phone_nuber
    #    print(url)
    res = requests.get(url)
    filename = pth + str(tekUser.chat_id) + '.xml'
    f = open(filename, 'w')
    f.write(res.text)
    f.close()

    tree = ET.parse(filename)
    root = tree.getroot()

    ErrorCode = root[0][0].text

    print('ErrorCode =  ', ErrorCode)

    if ErrorCode != '0':
        print('Неизвестный номер телефона')
        tekUser.Last_message = bot.send_message(message.from_user.id, 'В базі даних не знайдено жодного запису, Такого номера телефону немає.')
    else:
        for child in root:
            if child.tag == 'Results':
                for child1 in child:
                    if child1.tag == 'ResultQuery':
                        Found = 1
                        s = []
                        for child2 in child1:
                            if child2.tag == 'DCARDID':
                                s.append(child2.text)
                            if child2.tag == 'CLNTID':
                                s.append(child2.text)
                            if child2.tag == 'DCARDCODE':
                                s.append(child2.text)
                            if child2.tag == 'LOCKED':
                                s.append(child2.text)
                        if s[3] == '0':
                            tekUser.Cards.append(s)
    #    s = tekUser.Cards[0]
    #    print(s[2])
    if Found == 1:
        if len(tekUser.Cards) > 1:
            s = tekUser.Cards[0]
            tekUser.client_id = s[1]
            ChoiseCard(message, tekUser)
        else:
            s = tekUser.Cards[0]
            tekUser.karta_id = s[0]
            tekUser.client_id = s[1]
            tekUser.karta = s[2]
            get_client(message, tekUser)
            AfterAvtor(message, tekUser)
    else:
        print('Неизвестный номер телефона')
        tekUser.Last_message = bot.send_message(message.from_user.id, 'В базі даних не знайдено жодного запису, Такого номера телефону немає.')
        menu(message, tekUser)


def welcom_user(message, tekUser):
    bot.send_message(message.from_user.id, 'Код подходит. Авторизація пройдена!!!')
    get_client_id(message, tekUser)


#    bot.send_message(message.from_user.id, 'Вітаємо ' + tekUser.full_name)
#    AfterAvtor(message, tekUser)


def ShowProfil(message, tekUser):
    bot.send_message(message.chat.id, 'Ваш профіль ')
    bot.send_message(message.chat.id, "Стать: " + tekUser.pol)
    bot.send_message(message.chat.id, "Прізвище: " + tekUser.fam)
    bot.send_message(message.chat.id, "I'мя: " + tekUser.name)
    bot.send_message(message.chat.id, "По батькові: " + tekUser.otch)
    bot.send_message(message.chat.id, "Повне і'мя: " + tekUser.fam + ' ' + tekUser.name  + ' ' + tekUser.otch)
    bot.send_message(message.chat.id, 'Номер телефону: ' + tekUser.phone_nuber + ' ' + tekUser.phone)
    if tekUser.birth_date == None:
        dataR = '-'
    else:
        dataR = tekUser.birth_date
    bot.send_message(message.chat.id, 'Дата народження: ' + dataR)
    if tekUser.address == '':
        textadr = '-'
    else:
        textadr = tekUser.address
    if tekUser.address == None:
        textadr = '-'
    else:
        textadr = tekUser.address
    textadr =   tekUser.oblast + ' обл., ' + tekUser.rajon + ' р-н, ' + tekUser.gorod
    bot.send_message(message.chat.id, 'Адреса: ' + textadr)
    if tekUser.email == '':
        textemail = '-'
    else:
        textemail = tekUser.email
    bot.send_message(message.chat.id, 'E''mail: ' + textemail)
    tekUser.Last_message = bot.send_message(message.chat.id, 'Номер картки: ' + tekUser.karta)
    AfterAvtor(message, tekUser)

def show_barcode(message, tekUser):
    barCodeImage = barcode.get('ean13', tekUser.karta, writer=ImageWriter())
    fullname = barCodeImage.save(pth+str(tekUser.chat_id))


def drawing(message, tekUser):
    im = open(pth + str(tekUser.chat_id) + '.png', 'rb').read()
    tekUser.Last_message = bot.send_photo(message.chat.id, im, 'Це ваша картка. Щоб використатися покажіть цей екран поперед оплати''')
    AfterAvtor(message, tekUser)