import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import random
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

name=''
def wishMe():
    global name
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
    speak("Please enter your name to continue..")
    name=input()       
    speak(f"Hello {name}!! I am Trinity, and I am your Basic digital assistant.")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:  
        speak("I am sorry, I lost you there.") 
        print("Say that again please...")  
        return "N"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('morpheusmadafaka@gmail.com', 'krrishsucks')
    server.sendmail('morpheusmadafaka@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    cont= True
    while cont:
        speak("How may I help you??")
        query = takeCommand().lower()
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                print("Sorry!! Your search couldn't be displayed. Please try again.")
                speak("Sorry!! Your search couldn't be displayed. Please try again.")
            #Note: In order the not display the warning you gotta go to the source code of wikipedia module and add an argument as shown in the warning you get when you run this code in your computer :P
        elif 'youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            time.sleep(4)

        elif 'google' in query:
            webbrowser.open("https://www.google.com/")
            time.sleep(4)

        elif 'stack overflow' in query:              
            webbrowser.open("https://stackoverflow.com/")
            time.sleep(4)   

        elif ('music' in query) or ('song' in query):
            music_dir = r'C:\Users\Rohan\OneDrive\Desktop\Trinity\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[random.randint(0,4)]))
            time.sleep(7)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H hours %M minutes")    
            strDate=datetime.datetime.now().strftime("%d %m %y")
            speak(f"{name}, the time is {strTime} of {strDate}")


        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rohan130801@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak(f"Sorry {name}. I am not able to send this email")
        elif 'notepad' in query:
            codePath = r'C:\WINDOWS\system32\notepad.exe'
            os.startfile(codePath)
            time.sleep(3)
        elif 'paint' in query:
            codePath=r'C:\WINDOWS\system32\mspaint.exe'
            os.startfile(codePath)
            time.sleep(3)
        
        elif 'about' in query:
            speak("Hello again!! I am Trinity, a Basic digital assistant. Created by Saanchita, Sanath and Rohan, as a part of their computer project. I can help you with basic tasks like... playing music, opening google, telling time, and many more which requires your energy... So just sit back, relax and tell me what to do!!")
        else:
            speak("Sorry!! your request was way beyond my capabilities for now.")
        speak("Would you like to continue??")
        ask= takeCommand().lower()
        if ('no' in ask)or('thank' in ask):
            speak("Sayounara!! Thanks for your time!!")
            cont= False    
