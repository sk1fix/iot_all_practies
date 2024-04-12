import tkinter as tk


class MainWindow(tk.Frame):
    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0)
        self.principal = tk.DoubleVar()
        self.rate = tk.DoubleVar()
        self.years = tk.IntVar()
        self.amount = tk.StringVar()

        principalLabel = tk.Label(self, text="Principal:")
        principalLabel.grid(row=0, column=0, sticky=tk.W)

        self.principalScale = tk.Scale(self, from_=0, to=10000, resolution=0.01, orient=tk.HORIZONTAL,
                                       variable=self.principal, command=self.updateUi)
        self.principalScale.grid(row=0, column=1)

        rateLabel = tk.Label(self, text="Rate (%):")
        rateLabel.grid(row=1, column=0, sticky=tk.W)

        self.rateScale = tk.Scale(self, from_=0, to=100, resolution=0.01, orient=tk.HORIZONTAL, variable=self.rate,
                                  command=self.updateUi)
        self.rateScale.grid(row=1, column=1)

        yearsLabel = tk.Label(self, text="Years:")
        yearsLabel.grid(row=2, column=0, sticky=tk.W)

        self.yearsScale = tk.Scale(self, from_=0, to=50, orient=tk.HORIZONTAL, variable=self.years,
                                   command=self.updateUi)
        self.yearsScale.grid(row=2, column=1)

        amountLabel = tk.Label(self, text="Amount:")
        amountLabel.grid(row=3, column=0, sticky=tk.W)

        self.actualAmountLabel = tk.Label(self, textvariable=self.amount, relief=tk.SUNKEN, anchor=tk.E)
        self.actualAmountLabel.grid(row=3, column=1, sticky=tk.W + tk.E)

        # Обновление UI
        self.updateUi()

        self.parent.bind("<Escape>", self.quit)

    def updateUi(self, *ignore):
        p = self.principal.get()
        r = self.rate.get()
        y = self.years.get()
        amount = round(p * (1 + r / 100) ** y, 2)
        self.amount.set(f"${amount}")

    def quit(self, event=None):
        self.parent.destroy()


def increase_years():
    main_window.years.set(main_window.years.get() + 1)


def decrease_years():
    main_window.years.set(main_window.years.get() - 1)


root = tk.Tk()
root.title("Integerst")
main_window = MainWindow(root)

menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Increase Years", command=increase_years)
menu.add_command(label="Decrease Years", command=decrease_years)
menu.add_separator()
menu.add_command(label="Quit", command=root.destroy)


def popup(event):
    menu.post(event.x_root, event.y_root)


root.bind("<Button-3>", popup)  # При щелчке правой кнопкой мыши вызывается контекстное меню

root.mainloop()