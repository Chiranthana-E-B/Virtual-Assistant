from datetime import datetime
import webbrowser as web
import pywhatkit
import os
import pyttsx3
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from pyautogui import click
from time import sleep
from py1 import takeCommand



engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def GoogleMaps (place):
    Url_place="https://www.google.com/maps/place/" + str(place)

    web.open(url=Url_place)

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term

    web.open(result)
    speak("This is what i found for you")

    pywhatkit.playonyt (term)
    speak("This may also help")


def Note():
    os.startfile("C:\\WINDOWS\\system32\\notepad.exe")
    speak("what should i write?")
    takedown = takeCommand()
    write(takedown)
    speak("want to add anything else")
    take = takeCommand()
    if 'yes' in take:
        takee = takeCommand()
        write(takee)
    elif 'no' in take:
        speak('okay')

    press_and_release('ctrl + s')
    press('enter')
    speak("alright, what do you want to save it as")
    save = takeCommand()
    write(save)
    press('enter')
