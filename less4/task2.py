from tkinter import *
import tkinter as tk

room = Tk()
room.title()
room.geometry("250x200")


for i in range(2):
    for j in range(2):
        if i==j==0:
            lbl=Label(text="hello word",background="red")
            lbl.grid(row=i,column=j)
            continue
        if i==j==1:
            lbl=Label(text="мое имя тейп а фамилия на бабках",background="red")
            lbl.grid(row=i,column=j)
            continue
        lbl=Label(background="red")
        lbl.grid(row=i,column=j)

room.mainloop()