from tkinter import *
import tkinter as tk


def MyClick():
    f= et.get()
    lbl=Label(text=f"Привет, {f}!", background="yellow",fg="blue")
    lbl.pack()

room = Tk()
room.title()
room.geometry("400x500")


et=Entry(text='Введите ваше имя: ',width=50, background="blue", fg='white', borderwidth=5)
et.insert(0,'Введите ваше имя: ')
et.pack()

btn=Button(text='Нажмите', command=MyClick)
btn.pack()

room.mainloop()