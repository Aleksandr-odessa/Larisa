from datetime import datetime


HELLO = {
    'morning': "Доброе утро",
    'day': "Добрый день",
    'evning': "Добрый вечер",
    'night': "Доброй ночи, полуночник"
}


def hello_time():
    curent_time = datetime.now()
    if curent_time.hour > 6 and curent_time.hour < 12:
        hello_day = HELLO['morning']
    elif curent_time.hour > 17 and curent_time.hour <= 23:
        hello_day = HELLO['evning']
    elif curent_time.hour >= 00 and curent_time.hour <= 6:
        hello_day = HELLO['night']
    else:
        hello_day = HELLO['day']
    return(hello_day)
