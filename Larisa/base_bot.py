from datetime import datetime
from dictionary import hello_time
from sys import exit
# from voice import speak
import webbrowser


NAME = 'Анфиса'

base_search = ["мульт", "книжку", "сказку", "врем", "музык", "три кота", "стоп" , "откр"]

dialog_text = {
     'what_to_do': 'Что я могу для тебя сделать?',
     'i_can': 'Я могу включить для тебя мультфильм, почитать книжку, включить музыку, открывать сайты',
     'i_not_understand': 'я не понимаю что нужно сделать, повторите',
}


def what_time():
    print(f'сейчас {datetime.now().strftime("%H:%M")}')


def want_cartoon():
    print('выбран мультик')


def want_book():
    print('выбрана книга, сказка')


def want_music():
    print('выбрана музыка')


def stop():
    # speak('пока, до новых встречь')
    print('пока, до новых встречь')
    exit(0)


def search(string_dialog):
    for i in base_search:
        if string_dialog.find(i) > -1:
            rez_scan = i
    return(rez_scan)


def open_webpage(webpage):
    www = 'http://'+webpage
    webbrowser.open(www)


var_dialog = {
    base_search[3]: what_time,
    base_search[0]: want_cartoon,
    base_search[1]: want_book,
    base_search[2]: want_book,
    base_search[4]: want_music,
    base_search[5]: want_cartoon,
    base_search[6]: stop,
    base_search[7]: open_webpage,
}


def hello():
    # speak(hello_time() + '. ' + 'Меня зовут ' + NAME + '.  А как  тебя зовут?')
    # user_name = input()
    # speak('Очень приятно,  ' + user_name + '!')
    # speak(dialog_text['what_to_do'])
    # speak(dialog_text['i_can'])

    print(hello_time() + '. ' + 'Меня зовут ' + NAME + '.  А как  тебя зовут?')
    user_name = input()
    print('Очень приятно,  ' + user_name + '!')
    print(dialog_text['what_to_do'])
    print(dialog_text['i_can'])


def talk():
    input_talk = input()
    try:
        rez_search = search(input_talk)
        print(rez_search)
        print(input_talk)
    except UnboundLocalError:
        print(dialog_text['i_not_understand'])
    else:
        var_dialog.get(rez_search)()


if __name__ == "__main__":
    hello()
    talk()
    while exit != 'стоп':
        # speak(' могу я еще чем то помочь')
        print(' могу я еще чем то помочь')
        talk()
