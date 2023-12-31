import pyttsx3
import os
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import winsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greeting():

    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 6:
        speak("Доброй ночи.")
    elif hour > 6 and hour <= 12:
        speak("Доброе утро.")
    elif hour > 12 and hour <= 18:
        speak("Добрый день.")
    else:
        speak("Добрый вечер.")

    speak("Я голосовой помошник - Пятница.")


def get_username():

    speak("Как я могу к тебе обращаться?")
    username = hear()

    while (username is None):
        speak("Прости, я тебя не расслышала.")
        username = hear()

    if username is not None:
        speak(f"Рада видеть тебя, {username}")

    return username


def hear():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        if awake_flag:
            winsound.PlaySound("*", winsound.SND_ALIAS)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='ru-ru')
        print(query)

    except Exception as e:
        print(e)
        return "None"

    return query


if __name__ == '__main__':

    os.system('cls')

    with sr.Microphone():

        awake_flag = True

        greeting()
        username = get_username()

        while True:

            command = hear()

            if 'пятница' in command:
                awake_flag = True

            if awake_flag:

                if command is not None:
                    command = command.lower()

                    if 'открой википедию' in command:

                        webbrowser.open("wikipedia.com")

                        speak("Что мне найти в википедии?")
                        ask = hear().lower()

                        wikipedia.set_lang("ru")
                        results = wikipedia.summary(ask, sentences=3)

                        speak("На википедии говориться")
                        speak(results)

                    elif 'открой youtube' in command:

                        speak("Открываю ютуб в твоём браузере:")
                        webbrowser.open("youtube.com")

                    elif 'открой google' in command:

                        speak("Открываю гугл в твоём браузере:")
                        webbrowser.open("google.com")

                    elif 'открой гитхаб' in command:

                        speak("Открываю гитхаб в твоём браузере:")
                        webbrowser.open("github.com")

                    elif 'открой браузер' in command:

                        path = r"C:\Program Files\Internet Explorer\iexplore.exe"
                        os.startfile(path)

                    elif 'сколько время' in command:

                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        speak(f"Сейчас {strTime}")

                    elif 'пока' in command:
                        speak("Услышимся в следующий раз")
                        awake_flag = False








