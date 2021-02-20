import speech_recognition as sr 
import pyttsx3 as sp
import pywhatkit as kit 
import wikipedia as wiki
from datetime import datetime 

listener = sr.Recognizer()
engine = sp.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 125)
wiki.set_lang("es-419")  
time = datetime.now()

stop_actions = [' parar', ' para', ' deten', ' detente', ' termina', ' finaliza', ' stop']

def current_date(date):
    months = {'January': 'Enero', 'February': 'Febrero', 'March':'Marzo', 'April': 'Abril', 'May': 'Mayo', 
    'June': 'Junio', 'July': 'Julio', 'August':'Agosto', 'September':'Septiembre', 'October':'Octubre', 
    'November':'Noviembre', 'December':'Diciembre'}
    days = {'Monday':'Lunes', 'Tuesday': 'Martes' , 'Wednesday': 'Miercoles' , 'Thursday':'Jueves' , 
    'Friday': 'Viernes', 'Saturday': 'Sabado', 'Sunday':'Domingo'}
    month = months[date.date().strftime('%B')]
    day = days[date.date().strftime('%A')]
    day_num = date.day
    year = date.year
    full_date = "{} {} de {} del {}".format(day, day_num, month, year)
    return full_date

def talking_alex(text):
    engine.say(text)
    engine.runAndWait()

def listening():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            voice_command = listener.recognize_google(voice, language="es-MX")
            voice_command = voice_command.lower()
            if 'alex' in voice_command:
                voice_command = voice_command.replace('alex','')
    except:
        pass
    return voice_command

def virtual_assist():
    command = listening()
    if 'reproduce' in command:
        music = command.replace('reproduce', '')
        talking_alex('Reproduciendo ' + music + ' en Youtube')
        kit.playonyt(music)
    elif 'google' in command:
        word = command.replace('busca en google', '')
        talking_alex('Buscando en google ' + word )
        kit.search(word)
    elif 'wikipedia' in command:
        word = command.replace('busca en wikipedia', '')
        talking_alex('Buscando en wikipedia ' + word )
        summ = wiki.summary(word, sentences=3)
        talking_alex('La definición es la siguiente: ' + summ)
    elif 'hora' in command:
        hora = time.time().strftime('%I:%M %p')
        talking_alex('Son las: ' + hora)
    elif 'día' in command:
        fecha = current_date(time)
        talking_alex('Hoy es: ' + fecha)
    elif command in stop_actions:
        talking_alex('Deteniendo el servicio de Alex')
        exit()
    else:
        talking_alex('No entendi tu petición')
    
while True:
    virtual_assist()