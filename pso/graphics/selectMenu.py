import tkinter as tk

from pso.graphics.colors import Color

class SelectMenu():
    def __init__(self, root_frame: tk.Frame):
        self.root: tk.Frame = tk.Frame(root_frame, bg=Color.window_bg)