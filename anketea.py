from bot import bot  # Импортируем объект бота
from telebot import types
import requests
import sys

from config import *
from menu import *
from users import *

import urllib.request
import urllib.parse
from urllib.error import HTTPError


def record_profil(message, tekUser):
    try:
        url = 'http://185.80.232.179:8090/FB570E97-40C5-4690-9037-94E20BC0BC88/new_dcard'
        res = requests.get(url)
        tree = ET.ElementTree(ET.fromstring(res.text))
        root = tree.getroot()

        error_code = root[0][0].text

        if error_code != '0':
            print('Ошибка получения новой карточки')
            bot.send_message(message.from_user.id, 'Помилка отримання даних...')
        else:
            sum = 0
            for child in root:
                if child.tag == 'Results':
                    for child1 in child:
                        if child1.tag == 'ResultQuery':
                            readl = 0
                            for child2 in child1:
                                if child2.tag == 'DCARDID':
                                    tekUser.new_karta_id = child2.text
                                if child2.tag == 'CLNTID':
                                    tekUser.new_client_id = child2.text
                                if child2.tag == 'DCARDCODE':
                                    tekUser.new_karta = child2.text
                                    tekUser.karta = child2.text
            print('new_karta_id ', tekUser.new_karta_id)
            print('new_client_id ', tekUser.new_client_id)
            print('new_karta ', tekUser.new_karta)
#           tekUser.Last_message = tekUser.Last_message = bot.send_message(message.chat.id, 'Баланс бонусов ' + sum)
    except:
        e = sys.exc_info()[1]
        print('Ошибка получения карты ')
        print(e.args[0])
        tekUser.Last_message = tekUser.Last_message = bot.send_message(message.chat.id, 'Ошибка регистрации новой карты')
        menu(message, tekUser)

    try:
        cln_id = tekUser.new_client_id
        gr_id = 7
        cln_name = tekUser.fam + ' ' + tekUser.name + ' ' + tekUser.otch
        data_br = tekUser.birth_date

        br_data = data_br[6:10] + data_br[3:5] + data_br[0:2] + '000000'

        send_req = '''<?xml version="1.0" encoding="UTF-8"?>
            <Tables>
            <CLNT>
            <CLNTID>%s</CLNTID>
            <CLNTGRPID>7</CLNTGRPID>
            <CLNTNAME>%s</CLNTNAME>
            <CLNTBIRTHDAY>%s</CLNTBIRTHDAY>
            <LOCKED>0</LOCKED>
            <DELFLAG>0</DELFLAG>
            <UPDATENUM>0</UPDATENUM>
            </CLNT>
            </Tables>''' % (cln_id, cln_name, br_data)
        print(send_req)
        senddata = [('XML', send_req)]
        senddata = urllib.parse.urlencode(senddata)
        path = 'http://185.80.232.179:8090/5BC0F616-93ED-4E58-ACE5-37A1577C6A07/SaveTables?CallID=1&SystemID=1'
        # req = urllib.request.Request(path, senddata)
        req = urllib.request.Request(path, send_req)

        req.add_header("Content-type", "application/x-www-form-urlencoded")
        req.data = req.data.encode('utf-8')
        result = urllib.request.urlopen(req)
        print(result.status)
    except:
        e = sys.exc_info()[1]
        print('Ошибка записи клиента ')
        print(e.args[0])
        tekUser.Last_message = tekUser.Last_message = bot.send_message(message.chat.id,'Ошибка записи нового клиента')
        menu(message, tekUser)

    try:
        send_req = '''<?xml version="1.0" encoding="UTF-8"?>
            <Tables>
            <CLNTFORMPROPERTY>
            <CLNTID>%s</CLNTID>
            <CLNTFORMID>1</CLNTFORMID>
            <CLNTFORMITEMID>1</CLNTFORMITEMID>
            <CLNTPROPERTYVAL>%s</CLNTPROPERTYVAL>
            <DELFLAG>0</DELFLAG>
            <UPDATENUM>0</UPDATENUM>
            </CLNTFORMPROPERTY>
            <CLNTFORMPROPERTY>
            <CLNTID>%s</CLNTID>
            <CLNTFORMID>1</CLNTFORMID>
            <CLNTFORMITEMID>2</CLNTFORMITEMID>
            <CLNTPROPERTYVAL>%s</CLNTPROPERTYVAL>
            <DELFLAG>0</DELFLAG>
            <UPDATENUM>0</UPDATENUM>
            </CLNTFORMPROPERTY>
            <CLNTFORMPROPERTY>
            <CLNTID>%s</CLNTID>
            <CLNTFORMID>1</CLNTFORMID>
            <CLNTFORMITEMID>3</CLNTFORMITEMID>
            <CLNTPROPERTYVAL>%s</CLNTPROPERTYVAL>
            <DELFLAG>0</DELFLAG>
            <UPDATENUM>0</UPDATENUM>
            </CLNTFORMPROPERTY>
            <CLNTFORMPROPERTY>
            <CLNTID>%s</CLNTID>
            <CLNTFORMID>1</CLNTFORMID>
            <CLNTFORMITEMID>4</CLNTFORMITEMID>
            <CLNTPROPERTYVAL>%s</CLNTPROPERTYVAL>
            <DELFLAG>0</DELFLAG>
            <UPDATENUM>0</UPDATENUM>
            </CLNTFORMPROPERTY>
            <CLNTFORMPROPERTY>
            <CLNTID>%s</CLNTID>
            <CLNTFORMID>1</CLNTFORMID>
            <CLNTFORMITEMID>5</CLNTFORMITEMID>
            <CLNTPROPERTYVAL>%s</CLNTPROPERTYVAL>
            <DELFLAG>0</DELFLAG>
            <UPDATENUM>0</UPDATENUM>
            </CLNTFORMPROPERTY>
            <CLNTFORMPROPERTY>
            <CLNTID>%s</CLNTID>
            <CLNTFORMID>1</CLNTFORMID>
            <CLNTFORMITEMID>6</CLNTFORMITEMID>
            <CLNTPROPERTYVAL>%s</CLNTPROPERTYVAL>
            <DELFLAG>0</DELFLAG>
            <UPDATENUM>0</UPDATENUM>
            </CLNTFORMPROPERTY>
            <CLNTFORMPROPERTY>
            <CLNTID>%s</CLNTID>
            <CLNTFORMID>1</CLNTFORMID>
            <CLNTFORMITEMID>7</CLNTFORMITEMID>
            <CLNTPROPERTYVAL>%s</CLNTPROPERTYVAL>
            <DELFLAG>0</DELFLAG>
            <UPDATENUM>0</UPDATENUM>
            </CLNTFORMPROPERTY>
            <CLNTFORMPROPERTY>
            <CLNTID>%s</CLNTID>
            <CLNTFORMID>1</CLNTFORMID>
            <CLNTFORMITEMID>8</CLNTFORMITEMID>
            <CLNTPROPERTYVAL>%s</CLNTPROPERTYVAL>
            <DELFLAG>0</DELFLAG>
            <UPDATENUM>0</UPDATENUM>
            </CLNTFORMPROPERTY>
            <CLNTFORMPROPERTY>
            <CLNTID>%s</CLNTID>
            <CLNTFORMID>1</CLNTFORMID>
            <CLNTFORMITEMID>9</CLNTFORMITEMID>
            <CLNTPROPERTYVAL>%s</CLNTPROPERTYVAL>
            <DELFLAG>0</DELFLAG>
            <UPDATENUM>0</UPDATENUM>
            </CLNTFORMPROPERTY>
            <CLNTFORMPROPERTY>
            <CLNTID>%s</CLNTID>
            <CLNTFORMID>1</CLNTFORMID>
            <CLNTFORMITEMID>10</CLNTFORMITEMID>
            <CLNTPROPERTYVAL>%s</CLNTPROPERTYVAL>
            <DELFLAG>0</DELFLAG>
            <UPDATENUM>0</UPDATENUM>
            </CLNTFORMPROPERTY>
            </Tables>''' % (tekUser.new_client_id,tekUser.pol,
                            tekUser.new_client_id,tekUser.fam,
                            tekUser.new_client_id,tekUser.name,
                            tekUser.new_client_id,tekUser.otch,
                            tekUser.new_client_id,br_data,
                            tekUser.new_client_id,tekUser.oblast,
                            tekUser.new_client_id,tekUser.rajon,
                            tekUser.new_client_id,tekUser.gorod,
                            tekUser.new_client_id,tekUser.phone,
                            tekUser.new_client_id,tekUser.email
                            )
        print(tekUser.phone_nuber)
        print(send_req)

        path = 'http://185.80.232.179:8090/5BC0F616-93ED-4E58-ACE5-37A1577C6A07/SaveTables?CallID=1&SystemID=1'
        req = urllib.request.Request(path, send_req)

        req.add_header("Content-type", "application/x-www-form-urlencoded")
        req.data = req.data.encode('utf-8')
        result = urllib.request.urlopen(req)
        print("Запись анкеты, статус: ", result.status)
    except:
        e = sys.exc_info()[1]
        print('Ошибка записи анкеты клиента ')
        print(e.args[0])
        tekUser.Last_message = tekUser.Last_message = bot.send_message(message.chat.id,'Ошибка записи анкеты клиента ')
        menu(message, tekUser)

    try:
        print('Запись новой карты')
        cln_id = tekUser.new_client_id
        karta = get_num(tekUser.phone,'-')
        send_req = '''<?xml version="1.0" encoding="UTF-8"?>
            <Tables>
            <DCARD>
            <CLNTID>%s</CLNTID>
            <DCARDID>%s</DCARDID>
            <DCARDCODE>%s</DCARDCODE>
            <DCARDNAME>%s</DCARDNAME>
            <ISPAYMENT>0</ISPAYMENT>
            <PINCODE>0</PINCODE>
            <LOCKED>0</LOCKED>
            <DELFLAG>0</DELFLAG>
            <UPDATENUM>0</UPDATENUM>
            </DCARD>
            </Tables>''' % (cln_id, cln_id, karta, karta)
        print(send_req)

        path = 'http://185.80.232.179:8090/5BC0F616-93ED-4E58-ACE5-37A1577C6A07/SaveTables?CallID=1&SystemID=1'
        req = urllib.request.Request(path, send_req)

        req.add_header("Content-type", "application/x-www-form-urlencoded")
        req.data = req.data.encode('utf-8')
        result = urllib.request.urlopen(req)
        print("Запись новой карты, статус: ", result.status)
    except:
        e = sys.exc_info()[1]
        print('Ошибка записи новой карты ')
        print(e.args[0])
        tekUser.Last_message = tekUser.Last_message = bot.send_message(message.chat.id,'Ошибка записи новой карты ')
        menu(message, tekUser)


    ShowProfil(message, tekUser)

def get_num(phone, sybol):
    if phone[0:3] == '+38':
        s = phone[3:]
    else:
        s = phone
    try:
        while s.index(sybol, 0, len(s)) > 0:
            x = len(s)
            i = s.index(sybol, 0, x)

            s1 = s[0:i] + s[i + 1:x]
            s = s1
    except ValueError:
        return s
    else:
        return 'Ошибка извлечения номера'

def finish(message: object, tekUser: object) -> object:
    if tekUser == -1:
        Kepper.NewChat(message.chat.id)
        tekUser = Kepper.find(message)
    print('Finish')
    run_record(message, tekUser)
    #    record_profil(message, tekUser)
    #    ShowProfil(message, tekUser)
#    menu(message,tekUser)

def me_jo(message: object, tekUser: object) -> object:
    if tekUser == -1:
        Kepper.NewChat(message.chat.id)
        tekUser = Kepper.find(message)
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Ч",  callback_data="Ме")
    but_2 = types.InlineKeyboardButton(text="Ж",  callback_data="Жо")
    key.add(but_1, but_2)
    tekUser.NumQw = 2
    tekUser.enter_pol = 0
    tekUser.enter_fam = 1
    tekUser.enter_mode = 1;
    tekUser.Last_message = bot.send_message(message.chat.id, 'Стать (Чоловік/Жінка):', reply_markup=key)


def qwect(message: object, tekUser: object) -> object:
    global Qwestion
    if tekUser == -1:
        Kepper.NewChat(message.chat.id)
        tekUser = Kepper.find(message)
    key = types.InlineKeyboardMarkup()
    but_2 = types.InlineKeyboardButton(text="Відміна",  callback_data="Нахер")
    key.add(but_2)
    if tekUser.NumQw < 11:
        tekUser.enter_mode = 1
        if tekUser.NumQw == 1:
            tekUser.enter_pol = 1
            Qwestion = 'Стать (Чоловік/Жінка):'
        elif tekUser.NumQw == 2:
            tekUser.enter_fam = 1
            Qwestion = 'Прізвище:'
        elif tekUser.NumQw == 3:
            tekUser.enter_im = 1
            Qwestion = 'Ім`я:'
        elif tekUser.NumQw == 4:
            tekUser.enter_jn = 1
            Qwestion = 'По батькові:'
        elif tekUser.NumQw == 5:
            tekUser.enter_dr = 1
            Qwestion = 'Дата народження (дд/мм/гггг):'
        elif tekUser.NumQw == 6:
            tekUser.enter_ob = 1
            Qwestion = 'Область:'
        elif tekUser.NumQw == 7:
            tekUser.enter_rn = 1
            Qwestion = 'Район:'
        elif tekUser.NumQw == 8:
            tekUser.enter_gr = 1
            Qwestion = 'Місто (селище, село):'
        elif tekUser.NumQw == 9:
            tekUser.enter_tl = 1
            Qwestion = 'Мобільний телефон +380NN-NNN-NN-NN:'
        else: #tekUser.NumQw == 10:
            tekUser.enter_em = 1
            Qwestion = 'Електронна адреса:'
    if tekUser.NumQw == 5:
        tekUser.NumQw = 8
    else:
        tekUser.NumQw = tekUser.NumQw + 1

    if tekUser.NumQw == 2:
        me_jo(message,tekUser)
    else:
        tekUser.Last_message = bot.send_message(message.chat.id, Qwestion, reply_markup=key)


def bonus(message, tekUser):
    url = 'http://185.80.232.179:8090/FB570E97-40C5-4690-9037-94E20BC0BC88/account_amount?dcardcode=' + tekUser.karta
    res = requests.get(url)
    tree = ET.ElementTree(ET.fromstring(res.text))
    root = tree.getroot()

    error_code = root[0][0].text

    if error_code != '0':
        print('Ошибка получения данных о клиенте')
        bot.send_message(message.from_user.id, 'Помилка отримання даних...')
    else:
        sum = 0
        for child in root:
            if child.tag == 'Results':
                for child1 in child:
                    if child1.tag == 'ResultQuery':
                        readl = 0
                        for child2 in child1:
                            if child2.tag == 'ACCOUNTTYPEID':
                                if child2.text == '2':
                                    readl = 1
                                else:
                                    readl = 0
                            if child2.tag == 'ACCOUNTSUM':
                                if readl == 0:
                                    s = child2.text
#                                    print(s)
                                    k = s.find(',')
                                    sum = s[0:k]
        bon = int(sum)/100
        print(bon)
        tekUser.Last_message = tekUser.Last_message = bot.send_message(message.chat.id, 'Баланс бонусов %s' % bon)
        AfterAvtor(message, tekUser)