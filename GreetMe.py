import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)  
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning... jay shri krishna...")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon...jay shri krishna...")
    else:
        speak("Good Evening...jay shri krishna...")
    speak("Please tell me, what do you want me to do?..")