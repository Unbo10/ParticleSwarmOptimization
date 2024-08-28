"""
This module defines the MainMenu class, which represents the main menu.

## Classes
- MainMenu: Represents the main menu in a graphical user interface.

### Attributes
- _root_frame: tk.Frame - The root frame for the main menu.
- root: tk.Frame - The main frame for the main menu.
- __initialize_window: callable - A callable to initialize the window.
- _title: tk.Label - Label displaying the title of the main menu.
- _window_width: int - The width of the window.
- _window_height: int - The height of the window.
- _title_height: int - The height of the title.
- _bottom_frame_height: int - The height of the bottom frame.
- __bottom_frame: BottomFrame - The bottom frame of the main menu.
- __options_frame: OptionsFrame - The options frame of the main menu.

### Methods
- display(): Displays the main menu and configures the title, bottom frame, and options frame.
"""

import tkinter as tk
from tkinter import font

from pso.graphics.bottomFrame import BottomFrame
from pso.graphics.optionsFrame import OptionsFrame
from pso.graphics.fonts import FontName
from pso.graphics.colors import Color

class MainMenu():
    def __init__(self, root_frame: tk.Frame, initialize_window: callable, change_menu: callable, program_version: str, window_width: int=250, window_height: int=250):
        self._root_frame: tk.Frame = root_frame # ! Check if this is the right root
        self.root: tk.Frame = tk.Frame(root_frame, bg=Color.test2_bg)
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
        # * Setting title
        self._title.place(x=0, y=0, width=self._window_width,
            height=self._title_height)
        self.__bottom_frame.display(self.__options_frame.root)
        self.__options_frame.display(self.__bottom_frame.root)
        self.root.place(x=0, y=0, width=250, height=250)
        
    