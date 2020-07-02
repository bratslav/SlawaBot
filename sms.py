import urllib.request
import urllib.parse

def b_phone(phone):
    str_phone = ''
    p = []
    p = list(phone)
    p1 = []
    if p[0] == '+':
        p = p[1:]
    for c in p:
        if c == ' ':
            continue
        if c == '(':
            continue
        if c == ')':
            continue
        if c == '-':
            continue
        p1.append(c)

    str_phone = ''.join(p1)

    if len(str_phone) == 10:
        str_phone ='38'+str_phone
    return str_phone

def send_sms(phone, x):
    login = "info@beer-market.com.ua"
    password = "Beer2017Beer"
    msg_id = "123456"

    text_message = 'Ваш код ' + str(x)

    phone_sms = b_phone(phone)
    #     phone_sms = phone
    print(phone_sms)
    send_sms = '''<?xml version="1.0" encoding="UTF-8"?>
        <SMS>
        <operations>
        <operation>SEND</operation>
        </operations>
        <authentification>
        <username>%s</username>
        <password>%s</password>
        </authentification>
        <message>
        <sender>SMS</sender>
        <text>%s </text>
        </message>
        <numbers>
        <number messageID="%s">%s</number>
        </numbers>
        </SMS>''' % (login, password, text_message, msg_id, phone_sms)

    senddata = [('XML', send_sms)]
    senddata = urllib.parse.urlencode(senddata)
    path = 'http://api.myatompark.com/members/sms/xml.php'
    req = urllib.request.Request(path, senddata)
    req.add_header("Content-type", "application/x-www-form-urlencoded")
    req.data = req.data.encode('utf-8')
    result = urllib.request.urlopen(req).read()
