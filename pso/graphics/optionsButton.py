import tkinter as tk

from pso.graphics.colors import Color

class OptionsButton(tk.Button):

    def __init__(self, parent_frame: tk.Frame, text: str, callable: callable, callable_args: dict, padx: tuple, pady: tuple, args: dict):
        super().__init__(parent_frame, text=text, **args)
        self.__parent_frame: tk.Frame = parent_frame
        self.__callable: callable = callable
        self.__callable_args: dict = callable_args
        self.__padx: tuple = padx
        self.__pady: tuple = pady

    def __enter(self, e):
        self.config(bg=Color.optim_button_abg, fg=Color.back_button_afg, activebackground=Color.optim_button_abg, activeforeground=Color.optim_button_afg)

    def __leave(self, e):
        self.config(bg=Color.optim_button_bg, fg=Color.optim_button_fg)

    def __click(self, e):
        self.config(bg=Color.optim_button_cbg, fg=Color.optim_button_cfg, activebackground=Color.optim_button_cbg, activeforeground=Color.optim_button_cfg)
    
    def __release(self, event: tk.Event):
        if event.type == '3':
            pass
        elif event.type == '5':
            self.config(bg=Color.optim_button_abg, fg=Color.back_button_afg, activebackground=Color.optim_button_abg, activeforeground=Color.optim_button_afg)
        self.__parent_frame.forget()
        self.__callable(**self.__callable_args)

    def display(self, row: int, column: int, sticky: str):
        self.bind("<Enter>", self.__enter)
        self.bind("<Leave>", self.__leave)
        self.bind("<Button-1>", self.__click)
        self.bind("<ButtonRelease-1>", self.__release)
        self.bind("<KeyRelease-Return>", self.__release)
        self.grid(row=row, column=column, pady=self.__pady, padx=self.__padx, sticky=sticky)