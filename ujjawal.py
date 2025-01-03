import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen_command():
    try:
        with sr.Microphone() as source:
            print('Listening for commands...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hey assistant' in command:
                command = command.replace('hey assistant', '')
                print(command)
    except:
        pass
    return command


def execute_command():
    command = listen_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        speak('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('The current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        try:
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)
        except wikipedia.exceptions.DisambiguationError:
            speak('There are multiple people with that name. Can you be more specific?')
    elif 'date' in command:
        speak('Sorry, I can’t tell you the date right now.')
    elif 'are you single' in command:
        speak('I am happily married to the internet.')
    elif 'tell me a joke' in command:
        speak(pyjokes.get_joke())
    else:
        speak('Sorry, I didn’t quite catch that. Can you say it again?')


while True:
    execute_command()
