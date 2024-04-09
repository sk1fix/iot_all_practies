import tkinter as tk
from tkinter import filedialog
import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt


class FileSelectWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Выбор файла CSV")
        self.koord = []
        self.selected_file = None
        self.count = 0
        self.select_button = tk.Button(
            self, text="Выбрать файл", command=self.select_file)
        self.select_button.pack(pady=20)
        self.open_button = tk.Button(
            self, text="Визуализация", command=self.open_file)
        self.open_button.pack(pady=10)

    def select_file(self):
        self.selected_file = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv")])
        if self.selected_file:
            self.open_button.config(state=tk.NORMAL)

    def open_file(self):
        f = open(self.selected_file)
        if f:
            for row in f:
                row = row.split(',')
                if self.count == 0:
                    self.count += 1
                    continue
                if row[2][1].isdigit and row[2][:2]:
                    self.koord.append(
                        [int(row[0]), int(row[1]), int(row[2][:2])])
                elif row[2][:1]:
                    self.koord.append(
                        [int(row[0]), int(row[1]), int(row[2][:1])])
            self.withdraw()
            print(self.koord)
            second_window = SecondWindow(self, self.koord)
            second_window.mainloop()


class SecondWindow(tk.Tk):
    def __init__(self, parent, koord):
        super().__init__()
        self.title('Визуализация точек')
        self.parent = parent
        self.koord = koord
        self.canvas = tk.Canvas(self, width=600, height=600)
        self.canvas.pack()
        self.canvas.create_line(20, 580, 580, 580)
        self.canvas.create_line(20, 580, 20, 20)
        self.open_button = tk.Button(
            self, text="Построить эпюру", command=self.dalone)
        self.open_button.pack(pady=10)
        self.selected_points = []
        self.auto_points = []
        self.visual()

    def visual(self):
        for point in self.koord:
            colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF", "#FFA500", "#800080", "#008000", "#800000",
                      "#008080", "#000080", "#FF6347", "#7CFC00", "#00BFFF", "#FF69B4", "#FF4500", "#2E8B57", "#8A2BE2", "#4B0082",
                      "#FF1493", "#1E90FF", "#FFD700", "#00FF7F", "#9ACD32", "#8B008B", "#B22222", "#FF00FF", "#00FA9A", "#DAA520",
                      "#40E0D0", "#7B68EE"]
            x = point[0] * 28 + 20
            y = -point[1] * 28 + 580
            print(point[2])
            self.canvas.create_oval(
                x - 3, y - 3, x + 3, y + 3, fill=colors[point[2]-1])
            self.auto_points.append((x, y))
        self.canvas.bind("<Button-1>", self.select_point)

    def select_point(self, event):
        x, y = event.x, event.y
        self.selected_points.append((x, y))

        if len(self.selected_points) == 2:
            self.draw_line(self.selected_points[0], self.selected_points[1])
            self.split_line(self.selected_points[0], self.selected_points[1])

    def draw_line(self, start, end):
        self.canvas.create_line(
            start[0], start[1], end[0], end[1], fill="blue")

    def split_line(self, start, end):
        dx = (end[0] - start[0]) / 19
        dy = (end[1] - start[1]) / 19
        for i in range(1, 19):
            x = start[0] + i * dx
            y = start[1] + i * dy
            self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="green")

    def dalone(self):
        tri = Delaunay(np.array(self.auto_points))
        R_values = []
        for point in self.auto_points:
            simplex_index = tri.find_simplex(point)
            if simplex_index != -1:
                R = np.linalg.norm(
                    point - tri.points[tri.simplices[simplex_index]])
                R_values.append(R)
        self.plot_values(R_values)

    def plot_values(self, p_values):
        plt.figure()
        plt.plot(p_values, 'ro-')
        plt.xlabel('Индекс точки')
        plt.ylabel('Значение R')
        plt.title('График значений R')
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    app = FileSelectWindow()
    app.mainloop()
