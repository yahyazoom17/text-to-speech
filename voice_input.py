import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()

try:
    with sr.Microphone() as source:
            print("Ask me anything!")
            recorded_audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(recorded_audio)
                print(command)
            except:
                print("Error!")
except Exception as error:
        print(error)
finally:
        exit()