#varun no need to debug the program
import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("mam i am pystant mr. varun's virtual assistant mam mr. varun has gone to drink water mam i request you to please wait for them")       

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
          
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('groupoffunnykids@gmail.com', 'mranand2005')
    server.sendmail(takecommand() and speak("tell the email which you want to send email"), to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.in")   

        elif 'open arthava puranik' in query:
            webbrowser.open("youtube.com/arthavapuranik")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open padhle' in query:
            webbrowser.open("padhle.in")

        elif 'about you' in query:
            speak("i am pystant your virtual assistant i am programmed by varundeep singh")

        elif 'email' in query:
            webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
        elif 'google' in query:
            speak('Searching google...')
            query = query.replace("google", "")
            results = webbrowser.search(query, sentences=2)
            speak("According to google")
            print(results)
            speak(results)
            
        elif 'duo' in query:
            webbrowser.open('https://duo.google.com/?web')
        elif ("thank") in query:
            speak("your welcome sir,i am feeling very pleased to help you")
        elif 'meet my uncle' in query:
            speak("hello chachu how are you")
        elif ("tell") in query:
            speak("sorry paji menu samaj nahi aaya")
        elif ("google") in query:
            num_page = 3
            search_results = google.search(query, num_page)
            for result in search_results:
                speak(result.description)
        elif ("teacher") in query:
            speak("mam i am pystant mr. varun's virtual assistant mam mr. varun has gone to drink water mam i request you to please wait")
input()
