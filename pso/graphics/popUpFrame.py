
import tkinter as tk
from tkinter import font

from pso.graphics.colors import Color
from pso.graphics.fonts import FontName

class PopUpFrame(tk.Frame):
    def __init__(self, text: str):
        self.__text: tk.Text = tk.Text()
        self.__hide_button: tk.Button = tk.Button()
        self.__scrollbar: tk.Scrollbar = tk.Scrollbar()

    def display(self):
        pass