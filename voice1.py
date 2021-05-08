import speech_recognition as sr
import subprocess
import os

r = sr.Recognizer()
mic = sr.Microphone()

def say(text):
    subprocess.call(['say', text])

while True:
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            transcript = r.recognize_google(audio)
            print(transcript)
            if(transcript == "hello"):
                say("Hello Dhinesh!!!")
            elif(transcript == "how are you"):
                say("I'm doing good. Thanks. how are you?")
            elif(transcript.startswith("open")):                        
                print(transcript[5:])
                os.system('open /Applications/%s.app' %transcript[5:].replace(' ','\ '))
                #subprocess.run(['/Applications/%s.app' %transcript[5:].replace(' ','\ ')])
                say("I opened that application for you")
    except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")            