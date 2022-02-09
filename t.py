from fileinput import close
import speech_recognition as sr
import pyttsx3
import os
from datetime import datetime
from fuzzywuzzy import fuzz
import random
import serial
import webbrowser
import sys
import time

lampochka = False
if lampochka == True:
    ArduinoSerial = serial.Serial("COM8", 9600)

engine = pyttsx3.init()
engine.say("Здраствуйте")
engine.runAndWait()


def noice():
    print('Слушаю...')
    engine = pyttsx3.init()
    engine.say("Слушаю")
    engine.runAndWait()

def open_chrome():
    engine = pyttsx3.init()
    engine.say("Хорошо, сейчас я открою браузер")
    engine.runAndWait()
    os.startfile(r'C:\Users\admin\AppData\Local\Programs\Opera GX\launcher.exe')



current_datetime = datetime.now()
def say_time():
    now = datetime.now()
    engine = pyttsx3.init()
    engine.say("   Сейчас на часах" +  str(now.hour) + "часов и" + str(now.minute) + "минут")
    engine.runAndWait()

def funy():
    a = random.randint(1, 4)
    if a == 1:
        engine = pyttsx3.init()
        engine.say("Ведь почти у всех же комнаты с прямоугольными углами, тогда почему роботы-пылесосы круглые?")
        engine.runAndWait()
    elif a == 2:
        engine = pyttsx3.init()
        engine.say("Робот отлично пылесосит и протирает пол, осталось прошить его, чтобы он в конце влажной уборки говорил: Куда по помытому?!")
        engine.runAndWait()
    elif a == 3:
        engine = pyttsx3.init()
        engine.say("Появился значит в зоне, черный сталкер")
        engine.runAndWait()
    elif a == 4:
        engine = pyttsx3.init()
        engine.say("А где можно справку с печатью получить, что я не робот, чтобы каждый раз не искать светофоры?")
        engine.runAndWait()
if lampochka == True:
    def on_bulb():
        engine = pyttsx3.init()
        engine.say("Включаю свет")
        engine.runAndWait()
        ArduinoSerial.write(b'1')

    def off_bulb():
        engine = pyttsx3.init()
        engine.say("Выключаю свет")
        engine.runAndWait()
        ArduinoSerial.write(b'0')
    
def youTube():
    webbrowser.open('https://www.youtube.com', new=1)
    engine = pyttsx3.init()
    engine.say("Открываю ютуб")
    engine.runAndWait()
    
def bye():
    engine = pyttsx3.init()
    engine.say("Хорошо, пока")
    engine.runAndWait()
    sys.exit()

def weathers():
    webbrowser.open('https://ua.sinoptik.ua/погода-лисянка', new=1)
    engine = pyttsx3.init()
    engine.say("Открываю погоду")
    engine.runAndWait()



while 1:
    r =sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        noice()
        audio = r.listen(source)



    query = r.recognize_google(audio, language='ru-RU')    

    ope = fuzz.ratio(query, 'открой браузер')
    if ope > 87:
        open_chrome()   
    times = fuzz.ratio(query, "время")
    if times > 50:
        say_time()       

    timess = fuzz.ratio(query, 'часов')
    if timess > 50:
        say_time()


    fun = fuzz.ratio(query, 'скажи анекдот')
    if fun > 65:
        funy()
    if lampochka == True:
        if query == 'Включи свет':
            on_bulb()
        elif query == 'Выключи свет':
            off_bulb()    
        
    yut = fuzz.ratio(query, 'YouTube')
    if yut > 54:
        youTube()

    weather = fuzz.ratio(query, 'Открой погоду')
    if weather > 65:
        weathers()  

    out = fuzz.ratio(query, 'Отдыхай')
    if out > 50:
        bye()
    pock = fuzz.ratio(query, 'Пока')
    if pock > 65:
        bye()
    
    
    if query == 'Закрой браузер' :
        os.system("TASKKILL /F /IM opera.exe")        
        engine = pyttsx3.init()
        engine.say("Закрываю браузер")
        engine.runAndWait()

    opradio = fuzz.ratio(query, 'Открой радио')
    if opradio > 90:
        engine = pyttsx3.init()
        engine.say("Открываю Радио")
        engine.runAndWait()
        os.startfile(r'C:\Program Files (x86)\PCRadio\PCRadio.exe')

    zakradio = fuzz.ratio(query, 'Закрой радио')
    if zakradio > 90:        
        engine = pyttsx3.init()
        engine.say("Закрываю радио")
        engine.runAndWait()
        os.system("TASKKILL /F /IM PCRadio.exe")

    
        
    
       

        