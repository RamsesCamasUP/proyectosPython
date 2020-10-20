import sounddevice
from scipy.io.wavfile import write
import os
#pip install scipy
#pip install sounddevice
if __name__ =="__main__":
    fs = 44100
    second = 10
    print("Grabando")
    record_voice = sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
    sounddevice.wait()
    write("grabacion.mp3",fs,record_voice)
    os.system("start grabacion.mp3")