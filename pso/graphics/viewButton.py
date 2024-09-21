
import tkinter as tk

from pso.graphics.colors import Color

class ViewButton(tk.Button):
    def __init__(self, master: tk.Frame, image: tk.Image, active_image: tk.Image, bg: str, fg: str):
        super().__init__(master=master, image=image, bg=bg, fg=fg)
        self.__image: tk.Image = image
        self.__active_image: tk.Image = active_image
        self.__bind_to_events()

    def __enter(self, e):
        self.config(bg=Color.preview_button_abg, image=self.__active_image)

    def __leave(self, e):
        self.config(bg=Color.preview_button_bg, image=self.__image)

    def __click(self, e):
        self.config(bg=Color.preview_button_cbg, image=self.__image)

    def __release(self, e):
        pass
    
    def __bind_to_events(self) -> None:
        self.bind("<Enter>", self.__enter)
        self.bind("<Leave>", self.__leave)
        self.bind("<Button-1>", self.__click)
        self.bind("ButtonRelease-1", self.__release)