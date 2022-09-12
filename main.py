import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import pywhatkit
import smtplib
import yagmail
from keyboard import press
from keyboard import press_and_release
from keyboard import write
import webbrowser as web
from time import sleep
from pyautogui import click


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say (audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language="en-in")
        print(f"User said: {query}n")

    except Exception as e:
        print("Say that again please...")
        speak("Say that again please")
        return "None"
    return query





if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #Logic for executing tasks based on

        if 'open google' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H %M %p")
            print(strTime)
            speak("The time is (strTime) ")


        elif 'open code' in query:
            codepath = "D:\\Microsoft VS Code\Code.exe"
            os.startfile(codepath)


        elif 'open spotify' in query:
            spotpath = "C:\\Users\\User\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotpath)
            
        elif "open gmail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?tab = rm & ogbl#inbox")


        elif 'open epic games' in query:
            wpath = "D:\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe"
            os.startfile(wpath)


        elif 'date' in query:
            strdate = datetime.datetime.now().strftime("%b %d %Y")
            print(strdate)
            speak(f"The date is {strdate}")

        elif 'email' in query:
            speak("Who do you want to send it to?")
            reciever = "_@gmail.com"
            speak("what should i say?")
            message=takeCommand()
            sender = yagmail.SMTP("_@gmail.com")
            sender.send(to = reciever, subject = 'This is an automated mail', contents=message)

        elif 'remind me' in query:
            rememberMsg = query.replace("remind me", "")
            speak("You asked me to remind you that :" + rememberMsg)
            remember = open('data_txt', 'w')
            remember.write(rememberMsg)
            remember.close()

        elif 'what did you remember' in query:
            remember = open('data.txt', 'r')
            speak("You told me that " + remember.read())

        elif 'where is' in query:
            from features import GoogleMaps
            place = query.replace("where is", "")
            GoogleMaps(place)

        elif 'search youtube' in query:
            from features import YouTubeSearch
            music = query.replace('search youtube', '')
            YouTubeSearch(music)

        elif 'google' in query:
            import wikipedia as googleScrap
            query = query.replace('what is', '')
            query = query.replace('who is', '')
            query = query.replace('search', '')
            query = query.replace('what do you mean by', '')
            query = query.replace('how to', '')
            query = query.replace('how', '')
            speak("This is what i found")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query, 1)
                speak(result)

            except:
                speak("No speakable data available")

        elif 'new tab' in query:
            press_and_release('ctrl + t')

        elif 'close tab' in query:
            press_and_release('ctrl+w')

        elif 'new window' in query:
            press_and_release('ctrl + n')

        elif 'downloads' in query:
            press_and_release('ctrl + j')

        elif 'switch' in query:
            press_and_release('ctrl + Tab')

        elif 'incognito' in query:
            press_and_release('ctrl + Shift + n')

        elif 'close all' in query:
            press_and_release('Alt + F4')

        elif 'open' in query:
            name = query.replace("open", "")
            Name = str(name)
            if 'youtube' in Name:
                web.open("https://www.youtube.com/")
            elif 'amazon' in Name:
                web.open("https://www.amazon.in/ref=nav_logo")
            else:

                string_1 = "https://www." + Name + ".com"
                string_2 = string_1.replace("", "")
                web.open(string_2)

        elif 'pause' in query:
            press('space bar')

        elif 'play' in query:
            press('space bar')

        elif 'full screen' in query:
            press('f')

        elif 'change mode' in query:
            press('t')

        elif 'skip' in query:
            press('1')

        elif 'back' in query:
            press('j')

        elif 'increase speed' in query:
            press_and_release('Shift + >')

        elif 'decrease speed' in query:
            press_and_release('Shift + <')

        elif 'next' in query:
            press_and_release('shift + n')

        elif 'previous' in query:
            press_and_release('Shift+ p')

        elif "mute" in query:
            press('m')

        elif 'unmute' in query:
            press('m')

        elif 'captions' in query:
            press('c')

        elif 'miniplayer' in query:
            press('i')

        elif 'search' in query:
            click(x = 669, y = 166)

            speak('what should i search for')

            search = takeCommand()
            write(search)
            sleep(0.8)
            press('Enter')


        elif 'make a note' in query:
            from features import Note
            Note()

        elif 'close' in query:
            press_and_release('Alt+F4')

        elif 'my notepad' in query:
            os.startfile("D:\\jarvis\\Data\\Notepad")
            ask = takeCommand()
            os.startfile("D:\\jarvis\\Data\\Notepad\\" + ask + ".txt")

        elif 'my pc' in query:
            press_and_release('Windows + e')
            take = takeCommand()
            if 'data' in query:
                os.startfile("D:\\")
                dat = takeCommand()
                os.startfile("D:\\" + dat)
                da = takeCommand()
                os.startfile("D:\\GAMES" + da)
                
            elif 'os' in query:
                os.startfile("C:\\")
            elif 'downloads' in query:
                os.startfile("C:\\Users\\User\\Downloads")

        elif 'quit' in query:
            exit()
