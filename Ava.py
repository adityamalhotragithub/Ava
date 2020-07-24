import pyttsx3 #pip install -U pyttsx3==2.71
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from random import randint
import cv2
from chatbot import ChatBot



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id) # may be optional without this command play by defalt voice[0]

def AI(audio):
    engine.say(audio)
    engine.runAndWait()

def speak(audio):
	print(audio)
	AI(audio)

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
        
    else:
        speak("Good Evening!")   
    speak("I am Ava Sir. Please tell me how may I help you")  
    
     

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 500 #optional
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as ex:
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":

    Ava = ChatBot()

    wish()

    while True:
        query = takeCommand().lower()       
        k = cv2.waitKey(3)

        if 'wikipedia' in query:
            speak('Searching on Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia,")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            speak("playing music now sir")
            music_dir = 'D:\\Entertainment\\Videos' #give the path to music directory
            songs = os.listdir(music_dir)
            # print(len(songs))
            total = len(songs)
            for _ in range(1):
	            value = randint(1, total )#randomly chooses the song of all
	            print(value)
            os.startfile(os.path.join(music_dir, songs[value]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'quit' in query:# Quits when command "quit" said
        	speak('quitting now sir..')
        	break
        
        elif k == ord('q'):
        	break
        else:
            rply = Ava.reply(query)
            speak(rply)



        





