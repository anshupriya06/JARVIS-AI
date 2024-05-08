import pyttsx3
import speech_recognition 
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)  
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,3)
        
    try:
        print("Understanding...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def game_play():
    speak("Lets Play ROCK PAPER SCISSOR !!")
    print("LETS PLAYYYYYYYYYYY")
    i=0
    Me_score = 0
    Com_score = 0
    
    while(i<5):
        choose = ("rock","paper","scissor")
        com_choose = random.choice(choose)
        query = takeCommand().lower()
        if (query == "rock"):
            if (com_choose == "rock"):
                speak("ROCK")
                print(f"Score :- Me :- {Me_score} : Com :- {Com_score}")
           
            elif(com_choose == "paper"):
                speak("paper")
                Com_score += 1
                print(f"Score :- Me :- {Me_score} : Com :- {Com_score}")
                
            else:
                speak("Scissors")
                Me_score =+ 1
                print(f"Score :- Me :- {Me_score} : Com :- {Com_score}")
                
        elif (query == "paper"):
            if (com_choose == "rock"):
                speak("ROCK")
                Me_score += 1
                print(f"Score :- Me :- {Me_score} : Com :- {Com_score}")
            
            elif(com_choose == "paper"):
                speak("paper")
                print(f"Score :- Me :- {Me_score} : Com :- {Com_score}")
                
            else:
                speak("Scissors")
                Com_score =+ 1
                print(f"Score :- Me :- {Me_score} : Com :- {Com_score}")
        
        elif (query == "scissors" or query == "scissor"):
            if (com_choose == "rock"):
                speak("ROCK")
                Com_score += 1
                print(f"Score :- Me :- {Me_score} : Com :- {Com_score}")
            
            elif(com_choose == "paper"):
                speak("paper")
                Me_score += 1
                print(f"Score :- Me :- {Me_score} : Com :- {Com_score}")
                
            else:
                speak("Scissors")
                Me_score =+ 1
                print(f"Score :- Me :- {Me_score} : Com :- {Com_score}")
        
        i+=1
    
    
    print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")    
    