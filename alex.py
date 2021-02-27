import speech_recognition as sr 
import pyttsx3 as sp
import pywhatkit as kit 
import wikipedia as wiki
from datetime import datetime

class Alex():
    def __init__(self, text):
        self.text = text
        self.listener = sr.Recognizer()
        self.engine = sp.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        self.engine.setProperty('rate', 130)
        self.time = datetime.now()
        wiki.set_lang("es") 
        self.stop_actions = [' parar', ' para', ' deten', ' detente', ' termina', ' finaliza', ' stop']

    def current_date(self,date):
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

    def talking_alex(self,text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listening(self, text):
        try:
            with sr.Microphone() as source:
                text += 'Escuchando...\n'
                self.text.setText(text)
                voice = self.listener.listen(source)
                voice_command = self.listener.recognize_google(voice, language="es-MX")
                voice_command = voice_command.lower()
                if 'alex' in voice_command:
                    voice_command = voice_command.replace('alex','')
        except:
            pass
        return voice_command

    def virtual_assist(self, text):
        command = self.listening(text)
        if 'reproduce' in command:
            music = command.replace('reproduce', '')
            text += 'Reproduciendo ' + music + ' en Youtube\n'
            self.text.setText(text)
            self.talking_alex('Reproduciendo ' + music + ' en Youtube')
            kit.playonyt(music)

        elif 'google' in command:
            word = command.replace('busca en google', '')
            text += 'Buscando en google ' + word + '\n'
            self.text.setText(text)
            self.talking_alex('Buscando en google ' + word )
            kit.search(word)

        elif 'wikipedia' in command: 
            word = command.replace('busca en wikipedia', '')
            text += 'Buscando en wikipedia ' + word + '\n'
            self.text.setText(text)
            self.talking_alex('Buscando en wikipedia ' + word )
            summ = wiki.summary(word, sentences=4)
            if summ == '':
                text += 'No encontre la definición\n'
                self.text.setText(text)
                self.talking_alex('No encontre la definición')
            else:
                text += 'La definición es la siguiente: ' + str(summ) + '\n'
                self.text.setText(text)
                self.talking_alex('La definición es la siguiente: ' + summ)

        elif 'hora' in command:
            hora = self.time.time().strftime('%I:%M %p')
            text += 'Son las: ' + hora + '\n'
            self.text.setText(text)
            self.talking_alex('Son las: ' + hora)

        elif 'día' in command:
            fecha = self.current_date(self.time)
            text += 'Hoy es: ' + fecha + '\n'
            self.text.setText(text)
            self.talking_alex('Hoy es: ' + fecha)

        elif command in self.stop_actions:
            text += 'Deteniendo el servicio de Alex'
            self.text.setText(text)
            self.talking_alex('Deteniendo el servicio de Alex')
            exit()
        elif 'como estas' in command:
            text += 'Estoy muy bien, gracias por preguntarlo'
            self.text.setText(text)
            self.talking_alex('Estoy muy bien, gracias por preguntarlo')
        elif 'hola' in command:
            text += 'Hola, espero que estes bien, ten un lindo día.'
            self.text.setText(text)
            self.talking_alex('Hola, espero que estes bien, ten un lindo día.')
        else:
            text += 'No entendi tu petición\n'
            self.text.setText(text)
            self.talking_alex('No entendi tu petición')