import tkinter as tk
from tkinter import font

from pso.graphics.colors import Color
from pso.graphics.fonts import FontName

class CreateInput:
    def __init__(self, parent_frame, text: str, width: int):
        self.__label: tk.Label = tk.Label(parent_frame, text=text, font=font.Font(family=FontName.label, size=12), bg=Color.create_label_bg, fg=Color.create_label_fg)
        self.input_value: tk.StringVar = tk.StringVar()
        self.entry: tk.Entry = tk.Entry(parent_frame, width=width, justify="center", bg=Color.create_entry_bg, fg=Color.create_entry_fg, textvariable=self.input_value)

    def grid(self, label_row: int, column: int, sticky: str):
        self.__label.grid(row=label_row, column=column, sticky=sticky, padx=(10, 0), pady=20)
        self.entry.grid(row=label_row, column=column + 1, sticky=sticky, padx=(0, 10), pady=20)

    def get_input(self) -> str:
        return self.input_value.get()