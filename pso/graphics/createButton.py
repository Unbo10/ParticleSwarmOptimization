import tkinter as tk
from tkinter import font

from pso.graphics.colors import Color
from pso.graphics.fonts import FontName

class CreateButton(tk.Button):
    def __init__(self, parent_frame: tk.Frame, text1: str, text2: str, callable1: callable, callable2: callable) -> None:
        super().__init__(parent_frame, text=text1, font=font.Font(family=FontName.button, size=10), bg=Color.bottom_button_bg, fg=Color.bottom_button_fg)
        self.__bg: str = Color.bottom_button_bg
        self.__fg: str = Color.bottom_button_fg
        self.__abg: str = Color.create_button_abg
        self.__callable1: callable = callable1
        self.__callable2: callable = callable2
        self.__state: int = 1

    def __enter(self, e) -> None:
        self.config(bg=Color.bottom_button_hbg)

    def display(self) -> None:
        pass