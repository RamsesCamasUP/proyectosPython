import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os, time
import pygame

pygame.init()
pygame.mixer.init()
sounda= pygame.mixer.Sound("r90s.mp3")

def createWidgets():
    lablel1 = Label(root,text="Ingrese la hora en hh:mm (horas:minutos) -")
    lablel1.grid(row=0,column=0, padx=5, pady=5)
    global entry1
    entry1 = Entry(root,width=15)
    entry1.grid(row=0,column=1)

    lable2 = Label(root,text="Ingrese su mensaje")
    lable2.grid(row=1,column=0, padx=5, pady=5)
    global entry2
    entry2 = Entry(root,width=15)
    entry2.grid(row=1,column=1)

    btn = Button(root,text="Ingresar",width=10,command=ingresar)
    btn.grid(row=2, column=1)
   

    global label3
    label3 = Label(root, text="")
    label3.grid(row=3,column=0)

def message1():
    global entry1, label3
    alarm_time_label = entry1.get()
    label3.config(text="Esperando la alarma")
    messagebox.showinfo("Alarma",f'La hora de alarma es: {alarm_time_label}')

def ingresar():
    global entry1,entry2,label3
    alarm_time = entry1.get()
    message1()
    alarm_message = entry2.get()
    current_time =time.strftime("%H:%M")
    print(f'La hora de alarma es : {alarm_time}')
    while alarm_time != current_time:
        current_time =time.strftime("%H:%M")
        time.sleep(1)
    else:
        print("Reproduciendo alarma...")
        sounda.play()
        btn2 = Button(root,text="Parar alarma",width=10,command=stop)
        btn2.grid(row=2, column=1)
        label3.config(text="Sonando alarma")
        messagebox.showinfo("Alarma",f'{alarm_message}')

def stop():
    sounda.stop()
    btn = Button(root,text="Ingresar",width=10,command=ingresar)
    btn.grid(row=2, column=1)


if __name__ =="__main__":
    root = tk.Tk()
    root.title("Alarma")
    root.geometry("400x200")

    createWidgets()
    
    root.mainloop()