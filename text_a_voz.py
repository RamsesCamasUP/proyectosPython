from gtts import gTTS
import os
#pip install gTTS
if __name__ == "__main__":
    my_text = "Hello World, this is an Artificial Intelligence"
    mi_texto = 'Hola Papá, te quiero mucho'
    language = 'es'
    tts = gTTS(text=mi_texto,lang=language, slow=False)
    tts.save('hello.mp3')
    os.system("start hello.mp3")
    