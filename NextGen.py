import pyttsx3
from datetime import datetime
import speech_recognition as sr
import wikipedia
import sys
import webbrowser
import os
import cv2

import urllib.request
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)  
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am NextGen Voice Assistant. Please tell me how may i help you")
def takeCommand():
    #it take microphone as input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

        try:
            print("Recognize...")
            queary = r.recognize_google(audio ,language = 'en-in')
            print(f"user said: {queary}\n")

        except Exception as e:
            print(e)
            print("Say that again")
            speak("i did not understand that")
            speak("Please say it again")
            return "None"
        return queary

if __name__=='__main__':
    wishme()
    while True:
        queary = takeCommand().lower()
        #logic to execetue task based on queary
        if 'wikipedia' in queary:
            speak("Searching wikipedia...")
            queary=queary.replace("wikipedia","")
            results = wikipedia.summary(queary,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'how are you' in queary:
            speak("Naamaastee I’m well, thank you. ")
        elif "open youtube" in queary:
            speak("openning youtube...")
            webbrowser.open("youtube.com")
        elif "open google" in queary:
            speak("openning google....")
            webbrowser.open("google.com")
        elif ".com" in queary:
            speak("openning...")
            webbrowser.open("www."+queary)
        elif "shopping" in queary:
            speak("have a nice day at shopping")
            webbrowser.open("amazon.in")
        elif "time" in queary:
            strTime = datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir the time is {strTime}")
        elif "open camera" in queary:
            speak("Sure thing boss...")
            speak("openning...")
            cam = cv2.VideoCapture(0)# 0 mean first or primary camera
            img_counter = 0
            while True:
                ret,frame = cam.read()
                cv2.imshow('frame',frame)
                if not ret:
                    break
                k=cv2.waitKey(1)
                if k%256 == 27:
                    #ESC pressed
                    print("Escape...")
                    break
                elif k%256 ==32:
                    #Space pressed
                    img_name = "image_{}.png".format(img_counter)
                    cv2.imwrite(img_name,frame)
                    print("{} written".format(img_name))
                    img_counter += 1

            cam.release()
            cv2.destroyAllWindows()
        elif "news" in queary:
            speak("The Latest news are")
            main_url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=261f052e98904f878b63a9fec38a4f18"
            open_NDTV_page = requests.get(main_url).json()
            article = open_NDTV_page["articles"]
            results = []
            for ar in article:
                results.append(ar["title"])
            for i in range(len(results)):
                print(i + 1, results[i])
                speak(results[i])
            speak("These were the latest news. Thankyou")
        elif "exit" in queary:
            speak("well if you say so BYE....")
            break
        elif "NextGen" in  queary:
            speak("yeah i am listening...")
        elif " " in queary:
            new1 = 2
            tabUrl="https://www.google.com/search?sxsrf=ACYBGNSKdJccZBL0gtXb9-JS_vm_iuuclg%3A1582131636240&ei=tGlNXo-dDrKFmgehka2oDw&q="
            term = queary
            webbrowser.open(tabUrl+term,new=new1)
        elif "entertainment" in queary:
            speak("sure...")
            webbrowser.open("https://www.youtube.com/watch?v=0gosur3db5I")
        elif "game" in queary:
            webbrowser.open("https://hatchxr.com/@KashifKhan/penalty-Shoot?scene=scene1")