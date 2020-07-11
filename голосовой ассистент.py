import speech_recognition as sr
import os
import time
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import webbrowser as wb

opts = {
	"alias": ("кеша","кеш","инокентий","иннокентий","кешунь","кишунь","кяша","кэша"),
	"tbr": ("скажи","расскажи","покажи","сколько","произнеси", "открой"),
	"cmds": {
		"ctime": ("время", "времени"),
		"radio": ("Включи музыку","включи радио"),
		"stupid1": ("расскажи анекдот","рассмеши мени","пошути"),
		"shutdown": ("выключи комп","выключи компьютер","выкючение"),
		"youtube": ("ютуб","ютьюб", "youtube")
	}
}
#функции
def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()
 
def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
        print("[log] Распознано: " + voice)
   
        if voice.startswith(opts["alias"]):
            # обращаются к Кеше
            cmd = voice
 
            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()
           
            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()
           
            # распознаем и выполняем команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])
 
    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")
 
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():
 
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
   
    return RC
 
def execute_cmd(cmd):
    if cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
   
    elif cmd == 'radio':
        # воспроизвести радио
        os.startfile(r"C:\Users\Игорь\Downloads\muzlome_Klava_Koka_-_Pokinula_chat_68462517.mp3")
   
    elif cmd == 'stupid1':
        # рассказать анекдот
        speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")
    elif cmd == 'shutdown':
        # выключить комп
        os.system("shutdown /s /t 001")   
    elif cmd == 'youtube':
        # выключить комп
        wb.open("https://youtube.com")
    else:
        speak("Не понял")
 
# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index = 1)
 
with m as source:
    r.adjust_for_ambient_noise(source)
 
speak_engine = pyttsx3.init()
 
# Только если у вас установлены голоса для синтеза речи!
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[0].id)
 
# forced cmd test
speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")
 
speak("Добрый день, повелитель")
speak("Кеша слушает")

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1) # infinity loop
