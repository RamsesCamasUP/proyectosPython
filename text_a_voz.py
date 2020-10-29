from gtts import gTTS
import os
#pip install gTTS
if __name__ == "__main__":
    mi_texto = 'Saludos terricolas'
    language = 'es'
    nueva_voz = gTTS(text=mi_texto,lang=language, slow=False)
    nueva_voz.save('hola.mp3')
    os.system("start hola.mp3")
    