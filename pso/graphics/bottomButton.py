
import tkinter as tk

from pso.graphics.colors import Color
from pso.graphics.popUpFrame import PopUpFrame

class BottomButton(tk.Button):
    def __init__(self, parent_frame: tk.Frame, image: tk.PhotoImage, active_image: tk.PhotoImage, pop_up_text: tk.Text, abg: str = Color.bottom_button_abg, cbg: str = Color.bottom_button_cbg, args: dict = {
        "relief": "flat",
        "bg": Color.bottom_button_bg,
        "highlightbackground": Color.bottom_button_hbg,
        "hcolor": Color.bottom_button_hcolor,
        "highlightthickness": 1,
        "borderwidth": 0,
        "cursor": "hand2"
        }) -> None:
        super().__init__(parent_frame, image=image, **args)
        self.__image: tk.PhotoImage = image
        self.__active_image: tk.PhotoImage = active_image
        self.__bg: str = args["bg"]
        self.__abg: str = abg
        self.__cbg: str = cbg
        self.pop_up_frame: PopUpFrame = PopUpFrame(text=pop_up_text)

    def enter(self, e):
        self.config(bg=self.__abg, activebackground=self.__abg, image=self.__active_image)
    
    def leave(self, e):
        self.config(bg=self.__bg, image=self.__image)

    def click(self, e):
        self.config(bg=self.__cbg, image=self.__image)

    def release(self, e):
        # TODO next: Pass the release logic onto here, or if it is not possible then pass this function as an argument on init. 
        # TODO after: continue adapting BottomFrame to this and define PopUpFrame. Do not execute until all of this is set.
        pass

    def display(self, pop_up_frames: dict):
        pass