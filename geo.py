from telebot import types
from bot import bot  # Импортируем объект бота
import folium
from math import *
from config import *



coordinates = [[50.432353, 30.450253,'Антонова, 43'],
               [50.447568,30.515399,'Ахматової Анни, 22'],
               [50.407002,30.624320,'Ахматової Анни, 34'],
               [50.411168,30.641039,'Ахматової Анни, 5'],
               [50.512454,30.601209,' Бальзака, 42/20'],
               [50.435482,30.476975,'Богданівська, 7в'],
               [50.357680,30.911804,'Бориспіль, вул. Київський шлях, 17'],
               [50.516432,30.784004,'Бровари, вул. Київська, 243а'],
               [50.445264,30.624533,'Будівельників, 4'],
               [50.31570, 30.11563, 'Буча, вул. Склозаводська, 3'],
               [50.520298,30.450708,'Вишгородська, 56/2'],
               [50.389103,30.365573,'Вишневе, Лесі Українки, 74'],
               [50.381816,30.379874,'Вишневе, Першотравнева, 22/27'],
               [50.428008,30.429281,'Відрадний 16'],
               [50.448944,30.433082,'Гарматна, 20'],
               [50.439959,30.417194,'Героїв Севастополя, 24/2'],
               [50.433982,30.422396,'Героїв Севастополя, 35а'],
               [50.526648,30.515788,'Магазин ""Біле Сухе"" Героїв Сталінграду, 65Б'],
               [50.254037,30.326597,'Магазин ""Біле Сухе"", Глеваха, Вокзальна, 45'],
               [50.391480,30.628302,'Магазин ""Біле Сухе"", Гмирі, 14а'],
               [50.452146,30.385574,'Магазин ""Біле Сухе"", Градинська, 9'],
               [50.522011,30.612110,'Магазин ""Біле Сухе"", Данькевича, 14'],
               [50.407758,30.613477,'Магазин ""Біле Сухе"", Дніпровська набережна, 19а'],
               [50.416565,30.636170,'Магазин ""Біле Сухе"", Драгоманова, 1а'],
               [50.418880,30.633702,'Магазин ""Біле Сухе"", Драгоманова, 2'],
               [50.406794,30.637682,'Магазин ""Біле Сухе"", Драгоманова, 38а'],
               [50.442844,30.599316,'Магазин ""Біле Сухе"", Ентузіастів, 37а'],
               [50.435882,30.600986,'Магазин ""Біле Сухе"", Ентузіастів, 7'],
               [50.453909,30.486407,'Магазин ""Біле Сухе"", Златоустівська, 52'],
               [50.517356,30.242614,'Магазин ""Біле Сухе"", Ірпінь, Антонова Авіаконструктора б. 8д, прим. 4'],
               [50.437839,30.456671,'Магазин ""Біле Сухе"", Іскрівська, 7'],
               [50.225007,30.225501,'Магазин ""Біле Сухе"", Калинівка, Залізнична, 48'],
               [50.401506,30.623541,'Магазин ""Біле Сухе"", Княжий Затон, 11'],
               [50.422675,30.379807,'Магазин ""Біле Сухе"", Кольцова, 14б'],
               [50.451859,30.377180,'Магазин ""Біле Сухе"", Котельникова, 33а'],
               [50.459478,30.371748,'Магазин ""Біле Сухе"", Краснова, 17'],
               [50.487272,30.602137,'Магазин ""Біле Сухе"", Курнатовського, 15'],
               [50.438521,30.410423,'Магазин ""Біле Сухе"", бул. Вацлава Гавела 51/16'],
               [50.427820,30.417250,'Магазин ""Біле Сухе"", бул. Вацлава Гавела, 79'],
               [50.428683,30.377159,'Магазин ""Біле Сухе"", Леся Курбаса, 12а'],
               [50.424344,30.463310,'Магазин ""Біле Сухе"", Лобановского, 7/2'],
               [50.431931,30.375761,'Магазин ""Біле Сухе"", Лобачевського, 7'],
               [50.386417,30.465931,'Магазин ""Біле Сухе"", Ломоносова Михайла, 48'],
               [50.391612,30.480053,'Магазин ""Біле Сухе"", М. Максимовича, 3-д'],
               [50.505126,30.489083,'Магазин ""Біле Сухе"", Малиновського, 4в'],
               [50.458391,30.612232,'Магазин ""Біле Сухе"", Малишка, 5'],
               [50.500366,30.592202,'Магазин ""Біле Сухе"", Маяковського, 4є'],
               [50.455182,30.587973,'Магазин ""Біле Сухе"", Микільсько-Слобідська, 6/2"'],
               [50.473860,30.631156,'Магазин ""Біле Сухе"", Мілютенка, 20'],
               [50.426592,30.446099,'Магазин ""Біле Сухе"", Новгородська, 5'],
               [46.588960,30.794785,'Магазин ""Біле Сухе"", Одеса, вул. Добровольського, 112/1'],
               [46.594145,30.803324,'Магазин ""Біле Сухе"", Одеса, вул. Добровольського, 129'],
               [46.416928,30.718666,'Магазин ""Біле Сухе"", Одеса, вул. Інглезі, 3/2'],
               [50.433185,30.319851,'Магазин ""Біле Сухе"", Петропавлівська Борщагівка, вул. Львівська, 1а'],
               [50.517277,30.463591,'Магазин ""Біле Сухе"", Полярна, 8'],
               [50.424647,30.473023,'Магазин ""Біле Сухе"", Преображенська, 15'],
               [50.421709,30.476423,"Магазин ""Біле Сухе"", Преображенська, 22/9"],
               [50.492713,30.520578,"Магазин ""Біле Сухе"", Приозерна, 2а"],
               [50.511721,30.429933,"Магазин ""Біле Сухе"", Світлицького, 30/20"],
               [50.398686,30.385056,"Магазин ""Біле Сухе"", Софіївська Борщагівка, Толстого, 102"],
               [50.400266,30.623616,"Магазин ""Біле Сухе"", Срібнокільська, 14a"],
               [50.477229,30.449604,"Магазин ""Біле Сухе"", Теліги, 31/1"],
               [50.472828,30.446908,"Магазин ""Біле Сухе"", Теліги, 17"],
               [50.432569,30.377540,"Магазин ""Біле Сухе"", Тулузи, 11"],
               [50.475575,30.398585,"Магазин ""Біле Сухе"", Туполєва, 16"],
               [50.407090,30.616926,"Магазин ""Біле Сухе"", Урлівська 11а"],
               [50.401674,30.533641,"Магазин ""Біле Сухе"", Феодосійська, 2л"],
               [50.422657,30.650894,"Магазин ""Біле Сухе"", Харківське шосе, 49"],
               [50.524195,30.610605,"Магазин ""Біле Сухе"", Цвєтаєвої Марини, 18/78"],
               [50.393538,30.618228,"Магазин ""Біле Сухе"", Чавдар, 24"],
               [51.513225,31.321899,"Магазин ""Біле Сухе"", Чернігів, вул. Рокосовського, 41"],
               [50.458019,30.592370,"Магазин ""Біле Сухе"", Шептицького, 24"],
               [50.423984,30.665766,"Магазин ""Біле Сухе"", Вереснева, 26/28"],
               [50.519806,30.608914,"Магазин ""Біле Сухе"", Бальзака, 66"],
               [51.509727,31.330006,"Магазин ""Біле Сухе"", Чернігів, вул. Рокосовського, 12"],
               [50.454525,30.629732,"Магазин ""Біле Сухе"", Ю. Поправки, 4/39а"],
               [46.434328,30.719666,"Магазин ""Біле Сухе"", Одеса, Космонавтів, 14"],
               [46.573223,30.781187,"Магазин ""Біле Сухе"", Одеса, Добровольського, 82"],
               [46.438975,30.750429,"Магазин ""Біле Сухе"", Одеса, Черняховського, 12"],
               [46.456326,30.759110,"Магазин ""Біле Сухе"", Одеса, Мукачевський пер., 6/1"],
               [50.442267,30.430698,"Магазин ""Біле Сухе"", Гарматна, 40"],
               [50.447801,30.590411,"Магазин ""Біле Сухе"", Р. Окипної, 10"],
               [51.517021,31.280366,"Магазин ""Біле Сухе"", Чернігів, Льотна, 8а"],
               [50.403824,30.361013,"Магазин ""Біле Сухе"", Софіївська Борщагівка, Горького, 5б"],
               [50.392351,30.496371,"Магазин ""Біле Сухе"", Дубініна, 12/12"],
               [46.439859,30.707654,"Магазин ""Біле Сухе"", Одеса, Філатова, 51"],
               [50.358485,30.941444,"Магазин ""Біле Сухе"", Бориспіль, вул. Київський шлях, 47"]]

def Shops(message):
    new = 2
    Url = pth + "map1.html"
    map = folium.Map(location=[50.447, 30.524], zoom_start=12)

    # folium.Marker(location=[50.432353,30.450253], popup = "Google HQ", icon=folium.Icon(color = 'gray')).add_to(map)
    for coordinates in [[50.432353, 30.450253],
                        [50.447568, 30.515399]
                        ]:
        folium.Marker(location=coordinates, icon=folium.Icon(color='green')).add_to(map)

    map.save(Url)
    bot.send_message(message.chat.id, '.', url = 'https://drive.google.com/file/d/1O0q76Vzo97q6Y7Ag2IqKnEKb57H-EXXM/view?usp=sharing')
#    webbrowser.open(Url, new=new)


def geophone1(message,tekUser):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Показати на мапі найблищий магазин", request_location=True)
    keyboard.add(button_geo)
    tekUser.Last_message = bot.send_message(message.chat.id, "Показати на мапі найблищий магазин", reply_markup=keyboard)


def greatCircleDistance(lat1, lon1, lat2, lon2):
    def haversin(x):
        return sin(x / 2) ** 2

    return 2 * asin(sqrt(
        haversin(lat2 - lat1) +
        cos(lat1) * cos(lat2) * haversin(lon2 - lon1)))

def geophone2(message, tekUser):
    latitude = message.location.latitude
    longitude = message.location.longitude

#    print(longitude, latitude)

    min_rast = 1000
    min_ind = 0
    i = 0
    for coor in coordinates:
        lat = coor[0]
        lng = coor[1]
        rast = greatCircleDistance(latitude,longitude,lat,lng)
        if rast < min_rast:
            min_rast = rast
            min_ind = i
        i += 1
    print(min_rast, '    ', min_ind)

    bot.send_location(chat_id=message.chat.id, latitude=coordinates[min_ind][0], longitude=coordinates[min_ind][1])
    tekUser.Last_message = bot.send_message(message.chat.id, coordinates[min_ind][2])
