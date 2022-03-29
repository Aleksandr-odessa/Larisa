import speech_recognition as sr

#Настройка микрофона    
def command():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        #Бот ожидает нашего голоса
        print('Bot: ...')
        #Небольшая задержка в записи
        rec.pause_threshold = 1
        #Удаление фонового шума с записи
        rec.adjust_for_ambient_noise(source, duration=1)
        audio = rec.listen(source)
    try:
        #Распознание теста с помощью сервиса GOOGLE
        text = rec.recognize_google(audio, language="ru-RU").lower()
        #Вывод сказанного текста на экран
        print('Вы:  ' + text[0].upper() + text[1:])
            #Если не распознался тест из аудио
    except sr.UnknownValueError:
        text = 'Не понимаю. Повторите.'
        print('Bot: ' + text)
        talk(text)
        #Начинаем заново слушать
        text = command()
    return text

command()