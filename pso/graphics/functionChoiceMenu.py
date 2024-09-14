import tkinter as tk
from tkinter import font

from pso.graphics.colors import Color
from pso.graphics.fonts import FontName

class FunctionChoiceMenu():
    def __init__(self, parent_frame: tk.Frame, text: str, options: list[str], display_graph: callable) -> None:
        self.__display_graph: callable = display_graph
        self.__choice: tk.StringVar = tk.StringVar()
        self.__choice.set(options[0])
        self.__choice.trace_add("write", self.__trigger_graph_change)
        self.__dropdown_menu: tk.OptionMenu = tk.OptionMenu(parent_frame, self.__choice, *options)
        self.__label: tk.Label = tk.Label(parent_frame, text=text, bg=Color.create_label_bg, fg=Color.create_label_fg, font=font.Font(family=FontName.label, size=12))

    def __trigger_graph_change(self, *args) -> None:
        print("0")
        self.__display_graph(self.__choice.get())
        print("1")

    def grid(self, label_row: int, column: int, sticky: str) -> None:
        self.__label.grid(row=label_row, column=column, sticky=sticky, padx=(10, 0), pady=20)
        self.__dropdown_menu.grid(row=label_row, column=column + 1, sticky=sticky, padx=(0, 10), pady=20) # ! Padding seems to have a limited effect in an OptionMenu