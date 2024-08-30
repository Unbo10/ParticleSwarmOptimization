import tkinter as tk
from tkinter import font

from pso.graphics.optionsButton import OptionsButton
from pso.graphics.colors import Color
from pso.graphics.fonts import FontName

class OptionsFrame():
    def __init__(self, parent_frame: tk.Frame, title: tk.Label, change_menu: callable,  window_width: int, window_height: int, title_height, bottom_frame_height: int):
        self.__parent_frame: tk.Frame = parent_frame
        self.root: tk.Frame = tk.Frame(parent_frame, bg=Color.window_bg)
        self.__change_menu: callable = change_menu
        self.__title: tk.Label = title
        self.__window_width: int = window_width
        self.__window_height: int = window_height
        self.__title_height: int = title_height
        self.__bottom_frame_height: int = bottom_frame_height

        self.__button_parameters: dict = {
            "bg": Color.optim_button_bg,
            "fg": Color.optim_button_fg,
            "relief": "flat",
            "font": font.Font(family=FontName.button, size=10),
            "highlightbackground": Color.optim_button_hbg,
            "highlightcolor": Color.optim_button_hcolor,
            "highlightthickness": 1,
            "cursor": "hand2",
            }
        BUTTON_PADDING: int = 6
        self.__create_button: OptionsButton = OptionsButton(self.root, text="Create optimization", callable=change_menu, padx=BUTTON_PADDING*4, pady=(BUTTON_PADDING*2, BUTTON_PADDING), callable_args={"menu_name": "create"}, args=self.__button_parameters)
        self.__select_button: OptionsButton = OptionsButton(self.root, text="Select optimization", callable=change_menu, padx=BUTTON_PADDING*4, pady=BUTTON_PADDING, callable_args={"menu_name": "select"}, args=self.__button_parameters)
        self.__exit_button: OptionsButton = OptionsButton(self.root, text="Exit optimization", callable=change_menu, padx=BUTTON_PADDING*4, pady=(BUTTON_PADDING, BUTTON_PADDING*2), callable_args={"menu_name": "exit"}, args=self.__button_parameters)
        self.__buttons = [self.__create_button, self.__select_button, self.__exit_button]

    def display(self):
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.__create_button.focus_set()
        button_row = 0
        for button in self.__buttons:
            button.display(row=button_row, column=0, sticky="nsew")
            button_row += 1
        # ! CHECK: Functionality of the binding in Windows
        frame_width = self.__window_width
        frame_height = self.__window_height - (self.__title_height + self.__bottom_frame_height)
        self.root.place(x=0, y=self.__title_height, width=frame_width, height=frame_height)

