import tkinter as tk
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class StockGraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Data Graph")
        self.figure = Figure(figsize=(8, 6), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, self.root)
        self.load_button = tk.Button(
            self.root, text="Load Data", command=self.load_data)
        self.load_button.pack()
        self.display_button = tk.Button(
            self.root, text="Display Graph", command=self.display_graph)
        self.display_button.pack()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.dates = []
        self.prices = []

    def load_data(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt")])
        self.dates = []
        self.prices = []
        count = 0
        with open(file_path, 'r') as file:
            for line in file:
                if count == 0:
                    count += 1
                    continue
                data = line.strip().split(',')
                self.dates.append(data[0])
                self.prices.append(float(data[5]))

    def display_graph(self):
        if not self.dates or not self.prices:
            return
        self.ax.clear()
        self.ax.plot(self.dates, self.prices, marker='o', color='b')
        self.ax.set_xlabel('Dates')
        self.ax.set_ylabel('Prices')
        self.ax.set_title('Stock Prices Over Time')
        self.figure.autofmt_xdate()
        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = StockGraphApp(root)
    root.mainloop()
