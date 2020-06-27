from bot import bot  # Импортируем объект бота
from telebot import types
import requests

from config import *
from menu import *
from users import *

def record_profil(message, tekUser):
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
        print('new_karta_id ', tekUser.new_karta_id)
        print('new_client_id ', tekUser.new_client_id)
        print('new_karta ', tekUser.new_karta)
#        tekUser.Last_message = tekUser.Last_message = bot.send_message(message.chat.id, 'Баланс бонусов ' + sum)


def finish(message: object, tekUser: object) -> object:
    if tekUser == -1:
        Kepper.NewChat(message.chat.id)
        tekUser = Kepper.find(message)
    print('Finih')
    record_profil(message, tekUser)
    ShowProfil(message, tekUser)
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
    tekUser.Last_message = bot.send_message(message.chat.id, 'Стать (Жінка/Чоловік):', reply_markup=key)


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
            Qwestion = 'Стать (Жінка/Чоловік):'
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
            Qwestion = 'Електроний адрес:'
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
                                if readl == 1:
                                    s = child2.text
                                    k = s.find(',')
                                    sum = s[0:k]
#        print(int(sum)/100)
        tekUser.Last_message = tekUser.Last_message = bot.send_message(message.chat.id, 'Баланс бонусов ' + sum)
        AfterAvtor(message, tekUser)