from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from menu import *


def qwect2(message: object, tekUser: object) -> object:
    if tekUser == -1:
        Kepper.NewChat(message.chat.id)
        tekUser = Kepper.find(message)
    key = types.InlineKeyboardMarkup()
    but_2 = types.InlineKeyboardButton(text="Відміна",  callback_data="НахерМыло")
    key.add(but_2)
    Qwestion2 = ''
    if tekUser.NumQw < 4:
        tekUser.enter_mode = 1
        if tekUser.NumQw1 == 1:
            tekUser.enter_email_name = 1
            Qwestion2 = 'Ваше ім`я:'
        elif tekUser.NumQw1 == 2:
            tekUser.enter_email_phone = 1
            Qwestion2 = 'Ваше телефон:'
        elif tekUser.NumQw1 == 3:
            tekUser.enter_email_letter = 1
            Qwestion2 = 'Ваше повідомлення:'

    tekUser.NumQw1 = tekUser.NumQw1 + 1
    tekUser.Last_message = bot.send_message(message.chat.id, Qwestion2, reply_markup=key)

def send_email_(message, tekUser, message1):
    main_menu(message, tekUser, 'Ваше сообщение отправлено')

def send_email(message, tekUser, message1):
    msg = MIMEMultipart()
#    message = 'Test message'
    password = 'IH4WECuyj0km'

    msg['From'] = 'bot@beloesuhoe.com.ua'
    msg['To'] = 'Infochatbot@beloesuhoe.com.ua'
    #    msg['To'] = 'bratslav1776@gmail.com'
    msg['Subject'] = message.from_user.username

    message_ = 'Клиент: ' + tekUser.email_name + '\n'
    message_ = message_ +  'Телефон: ' + tekUser.email_phone + '\n'
    message_ = message_ +  'Пользователь telegram: ' + message.from_user.username + '\n\n\n'
    message_ = message_ + 'Сообщение: ' + tekUser.email_letter

    msg.attach(MIMEText(message_, 'plain'))

    server = smtplib.SMTP('mx1.mirohost.net:25')

    server.starttls()

    server.login(msg['From'], password)

    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    main_menu(message, tekUser, 'Ваше сообщение отправлено')