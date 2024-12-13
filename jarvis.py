import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return(data)
        except sr.UnknownValueError:
            print(" Not Understand")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':


        while True :
            data1=sptext().lower()

            if "your name" in data1:
                name = "my name is jarvis"
                speechtx(name)

            elif "old are you" in data1:
                age = "i am two years old"
                speechtx(age)

            elif 'time' in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)

            elif 'github' in data1:
                webbrowser.open("https://github.com/nafeesayubi/Jarvis")
                speechtx(github)

            elif 'linkedin' in data1:
                webbrowser.open("www.linkedin.com/in/nafees-ayubi-498b86257")
                speechtx(linkedin)

            elif 'resume' in data1:
                webbrowser.open("https://drive.google.com/file/d/1vYF5Uoy28BCnO90rTHTKjiOpRuir14zL/view?usp=drive_link")
                speechtx(resume)

            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en", category="neutral")
                print(joke_1)
                speechtx(joke_1)

            elif "exit" in data1:
                speechtx("thank you")
                break

else:
    print("thanks")
