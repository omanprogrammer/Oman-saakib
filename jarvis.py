import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am JARVIS . please tell me how may i help you")    

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...")
        r.pause_threshold = 1
        audio=r.listen(source)


    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

if __name__ == "__main__":
    wishme()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open rubicon song' in query:
            webbrowser.open("https://www.youtube.com/watch?v=zIvKigQ9cVY")
        elif 'open animal song' in query:
            webbrowser.open("https://www.youtube.com/watch?v=zqGW6x_5N0k")
        elif 'open check kar song' in query:
            webbrowser.open("https://www.youtube.com/watch?v=oHiO01lEbc4")
        elif 'open chat Gpt' in query:
            webbrowser.open("https://chat.openai.com/")
        elif 'open Google' in query:
            webbrowser.open("google.com")
        elif 'open my Github account' in query:
            webbrowser.open("https://github.com/omanprogrammer/CodingwithOman")   
