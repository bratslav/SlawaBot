TOKEN = '1288551964:AAHF1VIJvu8JJhs4vnNC4vV9d9J3jQAh2Fg'

TIMEZONE = 'Europe/Kiev'
TIMEZONE_COMMON_NAME = 'Kiev'

BotName = 'WhiteDryBot'
pth = 'c:\\SlawaBot\\'

class User(object):
    def __init__(self, chat_id):
        self.chat_id = chat_id  # Это ID чата
        self.Last_message = 0
        self.enter_mode = 0
        self.enter_number = 0
        self.enter_pol = 0
        self.enter_fam = 0
        self.enter_im = 0
        self.enter_jn = 0
        self.enter_dr = 0
        self.enter_ob = 0
        self.enter_rn = 0
        self.enter_gr = 0
        self.enter_tl = 0
        self.enter_em = 0
        self.enter_email_letter = 0
        self.enter_email_name = 0
        self.enter_email_phone = 0

        self.email_letter = ''
        self.email_name = ''
        self.email_phone = ''

        self.new_karta_id = ''
        self.new_client_id = ''
        self.new_karta = ''

        self.pol = ''
        self.fam = ''
        self.name = ''
        self.otch = ''
        self.birth_date = ''
        self.oblast = ''
        self.rajon = ''
        self.gorod = ''
        self.phone = ''
        self.email = ''

        self.enter_sms = 0
        self.phone_nuber = ''
        self.sms_kod = ''
        self.Cards = []
        self.NumQw = 0
        self.NumQw1 = 0
        self.client_id = -1
        self.karta_id = -1
        self.full_name = ''
        self.address = ''
        self.karta = ''

    def init_var(self):
        self.cur_pos = -1
        self.Last_message = 0
        self.enter_mode = 0
        self.enter_number = 0
        self.enter_sms = 0
        self.enter_pol = 0
        self.enter_fam = 0
        self.enter_im = 0
        self.enter_jn = 0
        self.enter_dr = 0
        self.enter_ob = 0
        self.enter_rn = 0
        self.enter_gr = 0
        self.enter_tl = 0
        self.enter_em = 0
        self.enter_letter = 0
        self.enter_email_name = 0
        self.enter_email_phone = 0

        self.email_letter = ''
        self.email_name = ''
        self.email_phone = ''


        self.pol = ''
        self.fam = ''
        self.name = ''
        self.otch = ''
        self.birth_date = ''
        self.oblast = ''
        self.rajon = ''
        self.gorod = ''
        self.phone = ''
        self.email = ''

        self.phone_nuber = ''
        self.sms_kod = ''
        self.Cards = []
        self.NumQw = 0
        self.NumQw1 = 0
        self.client_id = -1
        self.karta_id = -1
        self.full_name = ''
        self.address = ''
        self.karta = ''


class MyKeeper(object):

    def __init__(self):
        self.myList = []

    def NewChat(self, chat_id):
        x = 0
        for c in self.myList:
            if c.chat_id == chat_id:
                x = 1
        if x == 0:
            a = User(chat_id)
            self.myList.append(a)

    def find(self,message):
        x = 0
        for c in self.myList:
            if c.chat_id == message.chat.id:
                x = 1
                return c
        return -1

    def init_chat(self,a):
        for c in self.myList:
            if c == a:
                c.init_var()

global Kepper
