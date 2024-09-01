import tkinter as tk
from tkinter import font

from pso.graphics.colors import Color
from pso.graphics.fonts import FontName

class OptionsButton(tk.Button):

    def __init__(self, parent_frame: tk.Frame, text: str, callable: callable, callable_args: dict, padx: tuple, pady: tuple, button_font: font.Font = None, args: dict = {
    "bg": Color.optim_button_bg,
    "fg": Color.optim_button_fg,
    "relief": "flat",
    "highlightbackground": Color.optim_button_hbg,
    "highlightcolor": Color.optim_button_hcolor,
    "highlightthickness": 1,
    "cursor": "hand2",
    }) -> None:
        # TODO: Make the color-related arguments attribute arguments so that it does depend in the initialization in case the default values are different (and for the mere purpose of keeping the code consistent and good)
        if button_font == None:
            args.update({"font": font.Font(family=FontName.button, size=10)})
        super().__init__(parent_frame, text=text, **args)
        self.__parent_frame: tk.Frame = parent_frame
        self.__callable: callable = callable
        self.__callable_args: dict = callable_args
        self.__padx: tuple = padx
        self.__pady: tuple = pady

    def __enter(self, e) -> None:
        self.config(bg=Color.optim_button_abg, fg=Color.back_button_afg, activebackground=Color.optim_button_abg, activeforeground=Color.optim_button_afg)

    def __leave(self, e) -> None:
        self.config(bg=Color.optim_button_bg, fg=Color.optim_button_fg)

    def __click(self, e) -> None:
        self.config(bg=Color.optim_button_cbg, fg=Color.optim_button_cfg, activebackground=Color.optim_button_cbg, activeforeground=Color.optim_button_cfg)
    
    def __release(self, event: tk.Event) -> None:
        if event.type == '3':
            pass
        elif event.type == '5':
            self.config(bg=Color.optim_button_abg, fg=Color.back_button_afg, activebackground=Color.optim_button_abg, activeforeground=Color.optim_button_afg)
        self.__parent_frame.forget()
        self.__callable(**self.__callable_args)

    def bind_to_events(self) -> None:
        self.bind("<Enter>", self.__enter)
        self.bind("<Leave>", self.__leave)
        self.bind("<Button-1>", self.__click)
        self.bind("<ButtonRelease-1>", self.__release)
        self.bind("<KeyRelease-Return>", self.__release)

    def grid_display(self, row: int, column: int, sticky: str) -> None:
        self.bind_to_events()
        self.grid(row=row, column=column, padx=self.__padx, pady=self.__pady, sticky=sticky)

    def pack_display(self, fill: str, anchor: str) -> None:
        self.bind_to_events()
        self.pack(fill=fill, anchor=anchor, padx=self.__padx, pady=self.__pady)