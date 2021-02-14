import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

import smtplib
import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import winshell as winshell
import wolframalpha
from bs4 import BeautifulSoup
import os
from twilio.rest import Client

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.....')
            listener.pause_threshold = 1
            voice = listener.listen(source)
            command = ''
            try:
                print("Recognizing...")
                command = listener.recognize_google(voice, language='en-in')
                command = command.lower()
                if 'romeo' in command:
                    command = command.replace('romeo', '')
                    print(command)
                else:
                    pass
                # return command
            except:
                pass
                talk('Unable to Recognize your voice.')
            return command

    except Exception as e:
        print(e)
        # talk('some thing wrong')
def alarm():
    time=datetime.datetime.now().strftime('%I:%M:%p')
    hour = int(datetime.datetime.now().hour)
    command=take_command()
    if 6<= hour < 8:
        while True:
            if 'exit' in command:
                talk("you are so lazy sir")
                exit()
            else:
                talk(f'please wake up sir. now the time is{time}')
        
    
    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        talk("Good Morning Sir !")

    elif 12 <= hour < 18:
        talk("Good Afternoon Sir !")

    else:
        talk("Good Evening Sir !")

    name = "romeo 1.0"
    talk("I am your Assistant")
    talk(name)
    talk("Please tell me how may I help you")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('pranto.ahmed89@gmail.com', '*1l0A3#EmI-3#')
    server.sendmail('pranto.ahmed89@gmail.com', to, content)
    server.close()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email address', 'email password')
    server.sendmail('email address', to, content)
    server.close()


def run_romeo(time=None):
    clear = lambda: os.system('cls')
    # This Function will clean any
    # command before execution of this python file
    clear()
    command = take_command()
    print(command)
    name = "romeo 1.0"
    if 'play ' in command or 'playing ' in command:
        try:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        except Exception as e:
            print(e)
            talk(f"unable to find this {song}  in youtube")


    elif 'time' in command or 'what time is it ' in command:
        time = datetime.datetime.now().strftime('%I:%M:%p')  # I is the formate of the time and p is the am or pm
        print(time)
        talk('current time is ' + time)
    elif 'tell me about ' in command:
        try:
            person = command.replace('tell me about', '')
            info = wikipedia.summary(person, 2)
            # print(info)
            talk(f'according to wikipedia {info}')
        except Exception as e:
            print(e)
            talk(f"unable to find this  wikipedia{info} ")


    elif 'joke' in command:
        talk(' here you go')
        talk(pyjokes.get_joke())
    elif 'what is the date ' in command or 'date' in command:
        date = datetime.date.today()
        talk(date)

    elif '.com' in command or '.org' in command or '.net' in command or ' search' in command:
        try:
            web = command.replace('.com', '').replace('.org', '').replace('.net', '').replace('search', '').replace(
                'romeo', '')
            talk(web)
            print(web)
            # talk(command)
            webbrowser.open_new_tab(web)

            # webbrowser.open("youtube.com")
        except Exception as e:
            print(e)
            talk(f"unable to search {web} ")
    elif 'my audio music' in command or "start my audio music" in command:
        talk("why not sir ,Here you go with music")
        # music_dir = "G:\\Song"
        music_dir = "C:\\Users\\Public\\Music"
        songs = os.listdir(music_dir)
        print(songs)
        random = os.startfile(os.path.join(music_dir, songs[1]))

    elif 'how are you' in command:
        talk("I am fine, Thank you")
        talk("How are you, Sir")

    elif 'fine' in command or "good" in command:
        talk("It's good to know that your fine")

    elif "change my name to" in command:
        query = command.replace("change my name to", "")
        name = command

    elif "change name" in command:
        talk("What would you like to call me, Sir ")
        name = take_command()
        talk("Thanks for naming me")


    elif "who made you" in command or "who created you" in command:
        talk("it is greate to know you that I have been created by my boss.")
    elif "why you came to world" in command:
        talk("Thanks to my boss. further It's a secret ")

    elif 'open microsoft office' in command:
        talk("opening Power Point presentation")
        power = r"C:\\Program Files (x86)\\Microsoft Office\\Office15"
        os.startfile(power)
    elif 'what is love' in command or 'tell me about  love' in command:
        talk("It is 7th sense that destroy all other senses..it's a crazy things is not it my friend")

    elif "who are you" in command:
        talk(f"I am your virtual assistant {name}")


    elif "can you hear me" in command or "are you there" in command:
        talk('yes sir ,please tell me how can i help you ,do you need anything sir')

    elif 'open bluestack' in command:
        appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
        os.startfile(appli)
    elif 'empty recycle bin' in command:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        talk("Recycle Bin Recycled")

    elif "don't listen" in command or "stop listening" in command:
        try:
            talk("for how much time you want to stop jarvis from listening commands")
            a = int(take_command())
            time.sleep(a)
            print(a)
        except Exception:
            talk("i don't listen you ")
    elif "where is" in command or "romeo where is" in command or " romeo search where is" in command:
       try: 
            query = command.replace("where is", "").replace("romeo where is", " ").replace("romeo search where is", " ")
            location = query
            talk("User asked to Locate")
            talk(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")
       except Exception:
           talk('not found this place')

    elif "weather" in command:

        # Google Open weather website
        # to get API of Open weather
        api_key = "api key"
        # base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
        talk(" City name ")
        print("City name : ")
        city_name = take_command()
        # complete_url = base_url + "appid =" + api_key + "&q =" + city_name
        complete_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        response = requests.get(complete_url)
        x = response.json()

        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            print(" Temperature (in kelvin unit) = " + str(
                current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                current_pressure) + "\n humidity (in percentage) = " + str(
                current_humidiy) + "\n description = " + str(weather_description))
        else:
            talk(" City Not Found ")

    elif 'open code' in command:
        codePath = "/Applications/PyCharm CE.app"  # that's the code path.
        os.startfile(codePath)


    elif "calculate" in command or 'i want to know ' in command:

        try:
            # command = command.replace('calculate', '').replace('how to', '').replace('i want to know', '')
            query = command.replace('calculate', '').replace('i want to know', '')
            app_id = "Wolframalpha api id"
            # client = wolframalpha.Client(app_id)
            client = wolframalpha.Client('app_id')
            question = query
            res = client.query(question)
            answer = next(res.results).text
            print("The answer is " + answer)
            talk("The answer is " + answer)
        except Exception as e:
            print(e)
            talk('sorry sir i am not able to do this,please try again')

    elif "camera" in command or "take a photo" in command:
        try:
            ec.capture(0, "robo camera", "img.jpg")
        except Exception:
            talk('photos are not taken')

  

    elif 'email to gm' in command:
        try:

            talk('What is the subject?')

            subject = take_command()
            talk('What should I say in message?')

            message = take_command()
            content = 'Subject: {}\n\n{}'.format(subject, message)
            to = "golam.mahmud99@gmail.com"
            sendEmail(to, content)
            talk("Email has been sent!")
        except Exception as e:
            print(e)
            talk("Sorry my friend. I am not able to send this email")



    elif 'send a mail' in command:
        try:
            talk("What should I say?")
            content = take_command()
            talk("whome should i send")
            to = input()
            sendEmail(to, content)
            talk("Email has been sent !")
        except Exception as e:
            print(e)
            talk("I am not able to send this email")
    elif "write a note" in command:
        try:
            talk("What should i write, sir")
            note = take_command()
            file = open('jarvis.txt', 'w')
            talk("Sir, Should i include date and time")
            snfm = take_command()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        except Exception:
            talk('i am not able to write this note sir')

    # elif "what is" in command or "who is" in command:
    #
    #     # Use the same API key
    #     # that we have generated earlier
    #     client = wolframalpha.Client("API_ID")
    #     res = client.query(command)
    #
    #     try:
    #         print(next(res.results).text)
    #         talk(next(res.results).text)
    #     except StopIteration:
    #         print("No results")
    elif 'why are you answer so slow' in command or 'tell me why are you so slow' in command:
        talk('sir this is not my fault .your internet connection is so slow now')
    elif 'exit' in command:
        try:
            talk("Thanks for giving me your time")
            exit()
        except Exception as e:
            print(e)
            talk('i am not able to exit sir ..something doing wrong')

    elif 'what is the temperature in' in command:
        try:
            search=command.replace('what is the temperature in','')
            url = f'https://www.google.com/search?q={search}'
            r = requests.get(url)
            data = BeautifulSoup(r.text, 'html.parser')
            temp = data.find("div", class_='BNeawe').text
            talk(f'current {search} is {temp}')

        except Exception as e:
            print(e)
            talk('i am not able to find this place temperature ')
if __name__ == '__main__':
    wishMe()
    while True:
        run_romeo()
