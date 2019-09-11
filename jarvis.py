"""
code by: Arijit panda
Language used: python
project name: Voice controlled assistant
"""
import pyttsx3 #Module to import python text to speech conversation.
import speech_recognition as sr
import datetime #Module to import date and time
import wikipedia #Module  to access wiki.
import webbrowser #Module to access webpages.
import os #Os module.


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    
    hour = int(datetime.datetime.now().hour)
    speak("Hello sir! How can I help you.")

def takecommand():
    #It will take command from me by microphone input and will return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()
        #Logic to execute tasks based on query
       
        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif  'gym' in query:
        	speak('You have back workout tomorrow sir.') 
        	speak('Have a look on back workout video on Youtube sir. Never Give up sir.')
        	webbrowser.open("https://www.youtube.com/watch?v=6oc4e1mxY7I")


        elif 'open youtube' in query:
            speak("Opening youtube sir")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening google sir")
            webbrowser.open("google.com")

        elif 'facebook account' in query:
            speak("Opening facebook for you sir.")
            webbrowser.open("https://www.facebook.com")

        elif 'play music'in query:
            speak("Playing music for you sir")
            music_dir = 'F:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open atom text editor' in query:
            speak("Opening atomtext editor for you sir")
            codePath = "C:\\Users\\lenovo\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\GitHub, Inc"
            os.startfile(codePath)

        elif 'stop' in query:
        	speak("shutting down sir. Have a Great time with you.")
        	exit()

        elif 'exit' in query:
        	speak("shutting down sir. Have a Great time with you.")
        	exit()

        elif 'quit' in query:
        	speak("shutting down sir. Have a Great time with you.")
        	exit()

