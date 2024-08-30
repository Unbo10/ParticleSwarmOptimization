import tkinter as tk
from tkinter import font

from pso.graphics.bottomFrame import BottomFrame
from pso.graphics.optionsFrame import OptionsFrame
from pso.graphics.fonts import FontName
from pso.graphics.colors import Color

class MainMenu():
    def __init__(self, parent_frame: tk.Frame, initialize_window: callable, change_menu: callable, program_version: str, window_width: int=250, window_height: int=250):
        self._parent_frame: tk.Frame = parent_frame # ! Check if this is the right root
        self.root: tk.Frame = tk.Frame(parent_frame, bg=Color.test2_bg)
        self.__initialize_window: callable = initialize_window
        self._title: tk.Label = tk.Label(self.root, text="PSO manager",
            bg=Color.optim_label_bg, font=font.Font(family=FontName.title, size=15), wraplength=450,
            anchor="center")
        self._window_width: int = window_width
        self._window_height: int = window_height
        self._title_height: int = 40
        self._bottom_frame_height: int = 30
        self.__bottom_frame: BottomFrame = BottomFrame(self.root, self._window_width, self._window_height, self._title_height, self._bottom_frame_height, program_version)
        self.__options_frame: OptionsFrame = OptionsFrame(self.root, self._title, change_menu, self._window_width, self._window_height, self._title_height, self._bottom_frame_height)

    # * The baseMenu idea was discarded to avoid a circular import with GUI.
            
    def display(self):
        """
        """
        self.__initialize_window(width=250, height=250)
        self._title.place(x=0, y=0, width=self._window_width,
            height=self._title_height)
        self.__bottom_frame.display(self.__options_frame.root)
        self.__options_frame.display()
        self.root.place(x=0, y=0, width=250, height=250)

    def forget(self):
        self.root.place_forget()
        self.__bottom_frame.root.place_forget()
        self.__options_frame.root.place_forget()
        
    