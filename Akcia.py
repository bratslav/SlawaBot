from bot import bot # Импортируем объект бота
from telebot import types
from ftplib import FTP
import os
import datetime

from config import *
from menu import *

def get_url():
    Url = '/wp-content/uploads/'
    yr = datetime.date.today().strftime("%Y")
    mn = datetime.date.today().strftime("%m")
    Url = Url+yr+'/'+mn+'/'
    print(Url)
    return Url

def Akcii(message, tekUser):
    try:
        ftp = FTP('vs1960.mirohost.net')
        ftp.login('itteam', '1ShRHAgk0EEU')
        ftp.cwd(get_url())
        filenames = ftp.nlst()
        kolfiles = 0
        filenames.sort()
        for filename in filenames:
            if len(filename) == 5:
                s = filename[2:5]
                print(s)
                if s == 'png':
                    host_file = os.path.join(pth, filename)
                    try:
                        with open(host_file, 'wb') as local_file:
                            kolfiles = kolfiles + 1
                            ftp.retrbinary('RETR ' + filename, local_file.write)
                    except ftplib.error_perm:
                        print('Ошибка')
                        pass
                    bot.send_photo(message.chat.id, open(host_file,'rb'), '.')
        if kolfiles == 0:
            tekUser.Last_message = bot.send_message(message.chat.id, 'Акцій немає ')
        ftp.close()
        main_menu(message, tekUser, 'Діючі акції')
    except:
        print("Нет доступа к FTP")
        tekUser.Last_message = bot.send_message(message.chat.id, 'Нет доступа к FTP ')