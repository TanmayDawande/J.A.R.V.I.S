import sys

try:
    import speech_recognition as sr
    import pyttsx3
    import os
    import pyjokes
    import subprocess
    import pyautogui
    import time
    import wikipedia as wikipedia
    import pywhatkit
    import datetime
    import webbrowser
    import random
    from PyDictionary import PyDictionary
    import speedtest
    import requests
    from bs4 import BeautifulSoup
    import psutil
except:
    print('Import Error Occurred')
    sys.exit()

print('Version 0.0.1')
print('Creator:Tanmay Sunil Dawande')

speech = sr.Recognizer()

try:
    engine = pyttsx3.init()
except ImportError:
    print('Request driver is not found')
except RuntimeError:
    print('Driver failed to initialize')

voices = engine.getProperty('voices')
newVoiceRate = 195
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', newVoiceRate)


def wish():
    hour = int(datetime.datetime.now().hour)
    tt = str(time.strftime("%I:%M %p"))
    if 0 <= hour <= 12:
        speak_text_cmd(f'Good Morning, its {tt}.')
    elif 12 <= hour <= 18:
        speak_text_cmd(f'Good Afternoon, its {tt}.')
    else:
        speak_text_cmd(f'Good Evening, its {tt}.')

    speak_text_cmd('Jarvis here. How may i help you?')


def speak_text_cmd(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def read_voice_cmd():
    voice_text = ''
    print('Listening...')

    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source, duration=1)
        audio = speech.listen(source)

    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        print('Network Error.')
    return voice_text


def start():
    wish()
    while True:
        voice_note = read_voice_cmd().lower()
        print('Command : {}'.format(voice_note))
        greeting = ['Hola sir, whatsup ?', "Hello sir, pleasure to meet you", "hey sir", "hi, nice to meet you",
                    'bonjour', 'Ahoy-Ahoy', 'greetings, sir']
        farewell = ['bye sir, have a good day', 'farewell sir!', 'see you later!', 'come by again!', 'see you',
                    'goodbye sir !', 'adios', 'adieu', 'ciao']

        if 'hello' in voice_note or 'hey jarvis' in voice_note or 'hey my friend' in voice_note:
            speak_text_cmd(random.choice(greeting))
            continue
        if 'change your voice' in voice_note:
            speak_text_cmd('ok sir, changing my voice to male...')
            engine.setProperty('voice', voices[0].id)
            speak_text_cmd('here i am with a new voice')
        elif 'check the battery percentage' in voice_note:
            speak_text_cmd('ok sir')
            battery = psutil.sensors_battery()
            percent = battery.percent
            plugged = battery.power_plugged
            mode = 'plugged in' if plugged else 'not plugged in'
            if mode == 'plugged in':
                speak_text_cmd(f'sir the laptop has {percent} percent battery and is {mode}')
            elif mode == 'not plugged in':
                if percent >= 50:
                    speak_text_cmd(
                        f'sir the laptop has {percent} percent battery and is {mode}. i think you should plug it'
                        f' in after some time')
                if 50 > percent > 20:
                    speak_text_cmd(
                        f'sir the laptop has {percent} percent battery and is {mode}. i think you should plug it'
                        f' in after some time')
                if percent < 20:
                    speak_text_cmd(
                        f'warning! the laptop has {percent} percent battery and is {mode}. you should plug it now')
        elif 'bye' in voice_note or "pip pip" in voice_note:
            speak_text_cmd(random.choice(farewell))
            exit()
        elif 'how are you jarvis' in voice_note:
            speak_text_cmd('i am fine sir. How are you ?')
            myDemo = read_voice_cmd()
            myVoice = myDemo.lower()
            print('Command :' + myVoice)
            if 'i am fine' in myVoice:
                speak_text_cmd('that is good to know sir')
            elif 'i am not fine' in myVoice:
                speak_text_cmd('what happened sir')
                tanmay = speech.recognize_google(audio)
                print('listening....')
                if 'that is none of your business' in tanmay:
                    speak_text_cmd('ok sorry sir but you need to control your temper')
                    exit()
                elif 'i had some problems' in tanmay:
                    speak_text_cmd('ok sir, let me cheer you up by telling you a joke')
                    speak_text_cmd(pyjokes.get_joke())
        elif 'who made you' in voice_note or 'who created you' in voice_note or 'who is your god' in voice_note:
            speak_text_cmd('I, Jarvis, was created by Mr.Tanmay Dawande')
            continue
        elif 'test the wi-fi speed' in voice_note or 'what is my wi-fi speed' in voice_note:
            speed = speedtest.Speedtest()
            speak_text_cmd('Calculating download speed...')
            speak_text_cmd(f"Download speed: {'{:.2f}'.format(speed.download() / 1024 / 1024)} Mb per second")
            speak_text_cmd('Calculating upload speed...')
            speak_text_cmd(f"Upload speed is {'{:.2f}'.format(speed.upload() / 1024 / 1024)} Mb per second")
            continue
        elif 'set a timer for' in voice_note:
            condition = False
            a = voice_note.replace('set a timer for', "")
            if 'seconds' in voice_note:
                try:
                    m = int(a.replace('seconds', ''))
                    speak_text_cmd('setting a timer for' + a)
                    condition = True
                except:
                    speak_text_cmd('specify the seconds')
                    exit()
            elif 'second' in voice_note:
                try:
                    m = int(a.replace('second', ''))
                    speak_text_cmd('setting a timer for' + a)
                    condition = True
                except:
                    speak_text_cmd('specify the second')
                    exit()
            if 'minutes' in voice_note:
                try:
                    l = int(a.replace('minutes', ''))
                    condition = True
                    speak_text_cmd('setting a timer for' + a)
                    m = l * 60
                except:
                    speak_text_cmd('specify the minutes')
                    exit()
            elif 'minute' in voice_note:
                try:
                    l = int(a.replace('minute', ''))
                    condition = True
                    speak_text_cmd('setting a timer for' + a)
                    m = l * 60
                except:
                    speak_text_cmd('specify the minute')
                    exit()

            if 'hours' in voice_note:
                try:
                    l = int(a.replace('hours', ''))
                    condition = True
                    speak_text_cmd('setting a timer for' + a)
                    m = l * 60 * 60
                except:
                    speak_text_cmd('specify the hours')
                    exit()
            elif 'hour' in voice_note:
                try:
                    l = int(a.replace('hour', ''))
                    condition = True
                    speak_text_cmd('setting a timer for' + a)
                    m = l * 60 * 60
                except:
                    speak_text_cmd('specify the hour')
                    exit()
            if condition is False:
                speak_text_cmd('please say the command correctly')
                exit()
            elif condition is True:
                s = 0
                while s <= m:
                    time.sleep(1)
                    s += 1
                    print(s, "second")
                    if s == m + 1:
                        speak_text_cmd('timer done')
                        continue
            continue
        elif 'play' in voice_note:
            speak_text_cmd('playing' + (voice_note.replace('play', '')))
            song = (voice_note.replace('play', ''))
            pywhatkit.playonyt(song)
            time.sleep(5)
            continue
        elif 'search' in voice_note:
            query = voice_note.replace("search", "")
            webbrowser.open(query)
            time.sleep(5)
        elif 'please open' in voice_note:
            speak_text_cmd('Ok sir')
            d = voice_note.replace("please open", '')
            e = ('E:\\', d)
            subprocess.Popen(e)
            time.sleep(5)
            continue
        elif 'shutdown the PC' in voice_note:
            speak_text_cmd("Please confirm to shutdown the pc, initiate or decline")
            dawande = speech.recognize_google(audio)
            print('listening.....')
            if 'decline' in dawande:
                speak_text_cmd('shutdown protocol declined')
                exit(0)
                continue
            if 'initiate' in dawande:
                speak_text_cmd("Initiate shutdown sequence in three")
                time.sleep(1)
                speak_text_cmd("two")
                time.sleep(1)
                speak_text_cmd("one")
                time.sleep(1)
                os.system("sleep /s /t 1")
            else:
                speak_text_cmd('say a valid command')
                continue
        elif "where is" in voice_note:
            query = voice_note.replace("where is", "")
            location = query
            speak_text_cmd("User asked to Locate")
            speak_text_cmd(location)
            webbrowser.open("https://earth.google.com/web/search/" + location + "")
            time.sleep(5)
            continue
        elif 'open youtube' in voice_note:
            speak_text_cmd("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
            time.sleep(5)
            continue
        elif 'tell me a joke' in voice_note or 'amuse me' in voice_note or 'make me laugh' in voice_note:
            speak_text_cmd(pyjokes.get_joke())
            continue
        elif 'who' in voice_note or 'where' in voice_note or 'how' in voice_note:
            if 'how are you jarvis' in voice_note:
                speech = sr.Recognizer()
                with sr.Microphone() as source:
                    speak_text_cmd("i am fine sir, how are you ?")
                    print('Listening.....')
                    speech.adjust_for_ambient_noise(source, duration=1)
                    audio = speech.listen(source)
                my_string = speech.recognize_google(audio)
                print('Command :' + my_string)
                if 'I am fine' in my_string:
                    speak_text_cmd('that is good to know sir')
                elif 'I am not fine' in my_string:
                    speech = sr.Recognizer()
                    with sr.Microphone() as source:
                        speak_text_cmd("what happened sir ?")
                        print('Listening.....')
                        speech.adjust_for_ambient_noise(source, duration=1)
                        audio = speech.listen(source)
                    tanmay = speech.recognize_google(audio)
                    print('Command :' + my_string)
                    if 'that is none of your business' in tanmay:
                        speak_text_cmd('ok sorry sir but you need to control your temper')
                        exit()
                    elif 'i had some problems' in tanmay:
                        speak_text_cmd('ok sir, let me cheer you up by telling you a joke')
                        speak_text_cmd(pyjokes.get_joke())
            else:
                result = wikipedia.summary(voice_note, sentences=2)
                speak_text_cmd(result)
                continue
        elif 'what' in voice_note:
            if 'is the meaning' in voice_note:
                search = voice_note.replace('what is the meaning of', '')
                dictionary = PyDictionary(search)
                tanmay = dictionary.getMeanings()
                replace = str(tanmay).replace(',', ' or')
                print(replace)
                speak_text_cmd(str(replace))

            elif 'is the temperature in' in voice_note:
                ttt = voice_note.replace('what is the', '')
                url = f'https://www.google.com/search?q={ttt}'
                r = requests.get(url)
                data = BeautifulSoup(r.text, 'html.parser')
                temp = data.find('div', class_='BNeawe').text
                speak_text_cmd(f'current {ttt} is {temp}')
            else:
                result = wikipedia.summary(voice_note, sentences=2)
                print(result)
                speak_text_cmd(result)
        elif 'tell me the date' in voice_note:
            date_form = datetime.datetime.now().strftime("%d/%m/%Y")
            date = str(date_form)
            datem = datetime.datetime.strptime(date, "%d/%m/%Y")
            month = str(datem.month)
            day = str(datem.day)
            year = str(datem.year)
            datetime_object = datetime.datetime.strptime(month, "%m")
            month_name = datetime_object.strftime("%B")
            s = str(year)
            l = int(len(year) / 2)
            a, b = s[:l], s[l:]
            speak_text_cmd('The date is ' + day + 'th ' + month_name + ", " + a + b)
            continue
        elif 'open browser' in voice_note:
            speak_text_cmd('Opening sir')
            subprocess.call('C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe')
            time.sleep(5)
            continue
        elif 'join' in voice_note:
            meet_id = ""
            if 'join my geography meeting' in voice_note:
                meet_id = '2737902100'
            elif 'join my history meeting' in voice_note:
                meet_id = '3017601992'
            elif 'join my physics meeting' in voice_note:
                meet_id = '3967720797'
            elif 'join my chemistry meeting' in voice_note:
                meet_id = '3259556912'
            elif 'join my biology meeting' in voice_note:
                meet_id = '6204005550'
            elif 'join my maths meeting' in voice_note:
                meet_id = '4171660927'
            elif 'join my hindi meeting' in voice_note:
                meet_id = '3208554874'
            elif 'join my english lang meeting' in voice_note:
                meet_id = '7354476998'
            elif 'join my english lit meeting' in voice_note:
                meet_id = '7662757982'
            elif 'join my computer meeting' in voice_note:
                meet_id = '9394895993'
            elif meet_id == "":
                speak_text_cmd('give a valid command')
            speak_text_cmd('ok sir')
            subprocess.call('C:\\Users\\admin\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
            time.sleep(10)
            try:
                pyautogui.locateCenterOnScreen('join-button.png')
                pyautogui.moveTo('join-button.png')
                pyautogui.click()
                time.sleep(3)
                pyautogui.write(meet_id)
                time.sleep(3)
                pyautogui.locateCenterOnScreen('JB.png')
                pyautogui.moveTo('JB.png')
                pyautogui.click()
                time.sleep(3)
                pyautogui.write('PISPimpri')
                time.sleep(3)
                pyautogui.locateCenterOnScreen('JB2.png')
                pyautogui.moveTo('JB2.png')
                pyautogui.click()
            except:
                pyautogui.locateCenterOnScreen('home.png')
                pyautogui.locateCenterOnScreen('home.png')
                pyautogui.moveTo('home.png')
                pyautogui.click()
                time.sleep(3)
                pyautogui.locateCenterOnScreen('join-button.png')
                pyautogui.moveTo('join-button.png')
                pyautogui.click()
                time.sleep(3)
                pyautogui.write(meet_id)
                time.sleep(3)
                pyautogui.locateCenterOnScreen('JB.png')
                pyautogui.moveTo('JB.png')
                pyautogui.click()
                time.sleep(3)
                pyautogui.write('PISPimpri')
                time.sleep(3)
                pyautogui.locateCenterOnScreen('JB2.png')
                pyautogui.moveTo('JB2.png')
                pyautogui.click()
            continue


if __name__ == '__main__':
    start()
