import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Im your Alexa')
engine.say('What can Do for you')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
try:
    with sr.Microphone() as source:
        print('Listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()

        if 'alexa' in command:
            print(command)
except:
    pass
return command


