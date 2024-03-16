from tkinter import *
from PIL import ImageTk, Image
from pathlib import *


class PhotoViewer(Tk):
    def __init__(self):
        super().__init__()
        self.images=[]
        self.img=PhotoImage()