import tkinter as tk
from tkinter import font

from pso.graphics.colors import Color
from pso.graphics.fonts import FontName
from pso.graphics.optionsButton import OptionsButton

class CreateButton(OptionsButton):
    def __init__(self, parent_frame: tk.Frame, text1: str, text2: str, callable1: callable, callable2: callable, padx: int, pady: int) -> None:
        super().__init__(parent_frame, text=text1, button_font=font.Font(family=FontName.button, size=10), padx=padx, pady=pady, callable=None, callable_args=None) # ? Callable is none here?
        if text1 == text2:
            raise NotImplementedError("text1 and text2 cannot be the same")
        self.text1: str = text1
        self.text2: str = text2
        self.__active_text: str = text1
        self.__callable1: callable = callable1
        self.__callable2: callable = callable2
    
    def _release(self, event: tk.Event) -> None:
        if event.type == '3':
            pass
        elif event.type == '5':
            self.config(bg=Color.optim_button_abg, fg=Color.back_button_afg, activebackground=Color.optim_button_abg, activeforeground=Color.optim_button_afg)
        if self.__active_text == self.text1:
            self.config(text=self.text2)
            self.__active_text = self.text2
            self.__callable1()
        elif self.__active_text == self.text2:
            self.config(text=self.text1)
            self.__active_text = self.text1
            self.__callable2()
        else:
            raise NotImplementedError("The text of the button doesn't match neither callable")