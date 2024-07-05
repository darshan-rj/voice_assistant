
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os
import sys
import pyaudio


# to give computer a voice to speak we use microsoft speech APi (sapi5)
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()   # help to commuincate with us

def wishme(datetime):
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 17:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("Hey comrade!, Jarvis here, how can I help you ?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        audio = r.record(source, duration=2)
        print("listening ...")
        audio = r.listen(source,timeout=5,phrase_time_limit=10)
        r.pause_threshold = 5
        i = r.recognize_google(audio)
    
    try:
        print("recognizing ...")
        query = r.recognize_google (audio, language="en-in")
    except Exception as e:
        print(e)
        speak("Say that again please ...")
        return "none"
    return query

if __name__ == "__main__":
    wishme(datetime)
    if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia ...... please wait for a while")
            results = wikipedia.summary(query, sentence = 2)
            speak ("according to wikipedia ")
            print(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open gmail' in query:
            speak("opening gmail")
            webbrowser.open("mail.google.com")
        elif 'open command prompt' in query:
            os.system("start cmd")
        elif 'open gdrive' or 'open drive' in query:
            speak("opening google drive")
            webbrowser.open("drive.google.com")
        elif 'open gmeet' or 'open google meet' in query:
            speak("opening google meet")
            webbrowser.open()
        elif 'open notepad' in query:
            speak("opening notepad")
            npath="C:/Windows/notepad.exe"
            os.startfile(npath)
        elif 'open gcalender' or 'open google calendar' in query:
            speak("opening google calender")
            webbrowser.open("calender.google.com")    
        elif 'open gclassroom' or 'open google classroom' in query:
            speak("opening google classroom")
            webbrowser.open("classroom.google.com")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'what is the time' or 'time' or 'what\'s the time' in query:
            speak("The time is")
            time = datetime.datetime.now().strftime
            speak(f"The time is {time}")

        elif 'no thanks' in query:
            speak("Thank You for using me, have a nice day")

sys.exit()
