import speech_recognition as sr
#pip install SpeechRecognition
#python -m pip install pyaudio
if __name__ == "__main__":
    r = sr.Recognizer()
    print("Por favor, hable")
    with sr.Microphone() as source:
        audio_data = r.record(source,duration=5)
        print("Reconociendo...")
        text = r.recognize_google(audio_data)
        print(text)
        if text=="Tijeras":
            print("Le ganas al papel")
