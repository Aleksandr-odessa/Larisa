import pyttsx3

TATIANA = '''HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Tatiana'''

# инициализация 
engine = pyttsx3.init()
# подключение движка
voices = engine.getProperty('voices')
# выбор голоса
engine.setProperty('voice', TATIANA)
# выбор скорости
engine.setProperty('rate', 130)


def speak(text):
    engine.say(text)
    # запуск 
    engine.runAndWait()
