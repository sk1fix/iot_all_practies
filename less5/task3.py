import tkinter as tk
import random
class Ball:
    def __init__(self, canvas, paddle):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill="red")
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos):
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
class Paddle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill="blue")
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
        self.canvas.bind_all("<KeyRelease-Left>", self.stop_paddle)
        self.canvas.bind_all("<KeyRelease-Right>", self.stop_paddle)
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
    def turn_left(self, evt):
        self.x = -2
    def turn_right(self, evt):
        self.x = 2
    def stop_paddle(self, evt):
        self.x = 0

if __name__=="__main__":
    root = tk.Tk()
    root.title("Ping-Pong")
    root.resizable(0, 0)
    root.wm_attributes("-topmost", 1)
    canvas = tk.Canvas(root, width=500, height=400, bd=0, highlightthickness=0)
    canvas.pack()
    root.update()
    paddle = Paddle(canvas)
    ball = Ball(canvas, paddle)
    while True:
        if not ball.hit_bottom:
            ball.draw()
            paddle.draw()
        root.update_idletasks()
        root.update()
        root.after(10)
    root.mainloop()