import speech_recognition as sr
from gtts import gTTS
import os


if __name__ == "__main__":
    r = sr.Recognizer()
    print("Por favor, hable")
    with sr.Microphone() as source:
        audio_data = r.record(source,duration=5)
        print("Reconociendo...")
        text = r.recognize_google(audio_data)
        print(text)
        
    language = 'en'
    tts = gTTS(text=text,lang=language, slow=False)
    tts.save('hello.mp3')
    os.system("start hello.mp3")

