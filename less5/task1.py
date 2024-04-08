import tkinter as tk
from tkinter import filedialog


class FileSelectWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Выбор файла CSV")
        self.koord = []
        self.selected_file = None

        self.select_button = tk.Button(
            self, text="Выбрать файл", command=self.select_file)
        self.select_button.pack(pady=20)

        self.open_button = tk.Button(
            self, text="Визуализация", state=tk.DISABLED, command=self.open_file)
        self.open_button.pack(pady=10)

    def select_file(self):
        self.selected_file = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv")])
        if self.selected_file:
            self.open_button.config(state=tk.NORMAL)

    def open_file(self):
        if self.selected_file:

            for row in self.selected_file:
                self.koord+=[int(row[0]), int(row[1]),int(row[2])]
            self.withdraw()
            second_window = SecondWindow(self)
            second_window.mainloop()


class SecondWindow(tk.Tk):
    def __init__(self, parent):
        super().__init__()
        self.title('Визуализация точек')
        self.parent = parent

        self.open_button = tk.Button(
            self, text="Построить эпюру", state=tk.DISABLED, command=self.open_file)
        self.open_button.pack(pady=10)


if __name__ == "__main__":
    app = FileSelectWindow()
    app.mainloop()
