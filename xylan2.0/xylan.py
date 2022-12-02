import random
import datetime
import pyttsx3  
import gnewsclient
import wikipedia
import speech_recognition as sr
import webbrowser
import pyjokes
import playsound as ps
from tkinter import *
import pyautogui
import os
import time

#pass xylan2121

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour< 12:
        a = "Good morning sir", "Good morning master", "Hello sir Good Morning", "O, Good morning sir", "O, good morning sir", "Wow! Welcome back sir sir"
        speak(random.choice(a))
    elif hour>= 12 and hour< 18:
        b = "Good Afternoon sir", "Good Afternoon master", "Hello sir Good Afternoon", "O, Good Afternoon sir", "O, good Afternoon sir", "Wow! Welcome back sir"   
        speak(random.choice(b))
    else:
        
        c = "Good Evening sir", "Good Evening master", "Hello sir Good Evening", "O, Good Evening sir", "O, good Evening sir", "Wow! Welcome back sir sir"
        speak(random.choice(c))
wishMe()
wel = "Online and ready sir "

speak(random.choice(wel))
ps.playsound("startup.mp3")







def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)

    try:
        print("....")
        query = r.recognize_google(audio, language = 'en-in')
    except Exception as e:
        print(e)
        speak("Try to say again")
        return "None"
    return query

if __name__ == '__main__':
    while True:
        query  = takeCommand().lower()
        print(query)
        
        if 'wikipedia' in query:
            speak("Searching on wiki")
            try:
                query = query.replace("Wikipedia", "")
                results = wikipedia.summary(query, sentences = 2)
                
                speak("so, wikipedia says")
                speak(results)
                
            except:
                speak("Not available on wikipedia")


        if 'stop' in query or 'over' in query or 'bye' in query or 'quit' in query or 'see you' in query or 'go' in query:
                o = "bye sir", "ok bye sir", "see you again sir", "bye bye", "As your wish sir","As your wish, but I dont want to go sir!"
                speak(random.choice(o))
                break        
        

        elif "launch" in query:   

                    query = query.replace("launch","")
                    query = query.replace("Xylan","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter") 
                      
        elif 'open google' in query or 'search on google' in query or 'type on google' in query:
            ak = "what should i search?", "please say the words you want to search for", "what would you like to search sir?", "I am typing, say what you want to search on google?"
            speak(random.choice(ak))
            h = takeCommand().lower()
            webbrowser.open(f"https://www.bing.com/search?q={h}")
            

        elif 'open youtube' in query or 'play youtube' in query or 'play a video' in query or 'search on youtube' in query:
            dg = 'what should i search on youtube', 'what would you like to search on youtube', 'say the words you like to search on youtube'
            speak(random.choice(dg))
            x = takeCommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={x}")
            
         
        elif 'open web browser' in query or 'open a new tab of browser' in query or 'open a web browser' in query:
            
            webbrowser.open("www.goolge.com")
            
        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open(f"https://www.bing.com/search?q={query}")
            speak("As your wish sir")


        elif 'time ' in query :
            time = datetime.now()

            currenttime = strftime('%H:%M:%S')

            speak(currenttime)
            print(currenttime)
        elif 'date' in query:
            currentdate = datetime.date.today()
            print(currentdate) 
            speak(currentdate)


        elif 'joke' in query:
            speak(pyjokes.get_joke())
   
            
            

        elif 'shutdown' in query or 'shut down' in query:
            speak("Do you really want to shutdown the system sir?")
            ch = takeCommand()
            if "yes" in ch:
                
                os.system("shutdown /s /t 1")
            else:
                speak("ok sir")
        elif "play music" in query:
            speak("tell me the song name!")
            p = takeCommand()
            webbrowser.open(f"https://soundcloud.com/search?q={p}")
        elif "play" in query:
            query = query.replace("play", "")
            speak("Ok sir opening your desired song!")
            webbrowser.open(f"https://soundcloud.com/search?q={query}")    
        elif 'who are you' in query or "give me your introduction" in query:
            speak("Wait, i am introducing myself. My name is Xenon, I am an Assistant made by python progarmming, i can do many works like playing music, opening progarms, opening youtube, searching on web and many more")
        elif "who am i" in query:
            jh = "if you are speaking then, definately you are a human", "You are sir", "You are a human", "I cant identify peoples with their vocies, may be you are sir or anybody with relation of sir"
            speak(random.choice(jh))
        elif 'hello' in query:
            gf = "O hello sir", "Hi sir", "I am here for your help sir!", "hello sir", "I was surfing the web, and gethering information, how can i help?", "Online and ready"
            speak(random.choice(gf))


        elif ' open drive' in query:
            speak("opening drive")
            webbrowser.open("https://drive.google.com")

        elif ' open instagram' in query :
            speak("opening instagram")
            webbrowser.open("https://www.instagram.com")   

        elif ' open facebook' in query :
            speak("opening facebook")
            webbrowser.open("https://www.facebook.com") 


        elif 'open earth ' in query :
            webbrowser.open("https://earth.google.com/")    
        