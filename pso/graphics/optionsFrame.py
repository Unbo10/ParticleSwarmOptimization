import tkinter as tk
from tkinter import font

from pso.graphics.optionsButton import OptionsButton
from pso.graphics.colors import Color
from pso.graphics.fonts import FontName

class OptionsFrame(tk.Frame):
    """
    OptionsFrame is a custom frame class that contains the main menu options.
    """
    def __init__(self, parent_frame: tk.Frame, change_menu: callable,  window_width: int, window_height: int, title_height, bottom_frame_height: int):
        super().__init__(parent_frame, bg=Color.window_bg)
        self.__window_width: int = window_width
        self.__window_height: int = window_height
        self.__title_height: int = title_height
        self.__bottom_frame_height: int = bottom_frame_height
        BUTTON_PADDING: int = 6
        self.__create_button: OptionsButton = OptionsButton(self, text="Create optimization", callable=change_menu, callable_args={"menu_name": "create"}, padx=BUTTON_PADDING*4, pady=(BUTTON_PADDING*2, BUTTON_PADDING))
        self.__select_button: OptionsButton = OptionsButton(self, text="Select optimization", callable=change_menu, callable_args={"menu_name": "select"}, padx=BUTTON_PADDING*4, pady=BUTTON_PADDING)
        self.__exit_button: OptionsButton = OptionsButton(self, text="Exit optimization", callable=change_menu, callable_args={"menu_name": "exit"}, padx=BUTTON_PADDING*4, pady=(BUTTON_PADDING, BUTTON_PADDING*2))
        self.__buttons = [self.__create_button, self.__select_button, self.__exit_button]

    def display(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.__create_button.focus_set()
        button_row = 0
        for button in self.__buttons:
            button.grid_display(row=button_row, column=0, sticky="nsew")
            button_row += 1
        # ! CHECK: Functionality of the binding in Windows
        # * Checked that it works properly in Windows
        frame_width = self.__window_width
        frame_height = self.__window_height - (self.__title_height + self.__bottom_frame_height)
        self.place(x=0, y=self.__title_height, width=frame_width, height=frame_height)

