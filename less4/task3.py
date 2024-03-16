from tkinter import *
import tkinter as tk


def MyClick():
    lbl=Label(text="Нажата кнопка!", background="yellow",fg="blue")
    lbl.pack()

    
room = Tk()
room.title()
room.geometry("500x500")


btn=Button(text='Нажмите', command=MyClick)
btn.pack()

room.mainloop()