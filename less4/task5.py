import tkinter as tk

def on_click(event):
    text=et.get()
    if event.widget.cget("text") == "=":
        try:
            result = eval(text)
            clear()
            et.insert(0, str(result))
        except:
            clear()
            et.insert(0, "Error")
    elif event.widget.cget("text") == "очистить":
        clear()
    else:
        et.insert(tk.END, event.widget.cget("text"))

def clear():
    et.delete(0,tk.END)

buttons=['0','1','2','3','4','5','6','7','8','9','+','-','*','/','=','очистить']

room = tk.Tk()
room.title('Calculator')

et=tk.Entry(room,width=30)
et.grid(row=0,column=0,columnspan=10)

for i in range(len(buttons)):
    but=tk.Button(room,text=buttons[i],width=10)
    but.grid(row=(i//3)+1,column=(i+3)%3)
    but.bind('<Button-1>', on_click)
room.mainloop()