import os
import time

import numpy as np
import tkinter as tk
from tkinter import font

from psopackage.graphics.colors import Color
from psopackage.graphics.createMenu.createMenu import CreateMenu
from psopackage.graphics.exitMenu import ExitMenu
from psopackage.graphics.mainMenu.mainMenu import MainMenu
from psopackage.graphics.selectMenu.selectMenu import SelectMenu
from psopackage.optimization import Optimization
from psopackage.database.data import Data

class GUI:
    __root: tk.Tk = tk.Tk()
    def __init__(self, optimization_history: list[Optimization], data: Data = Data("test"), program_version: str = "Error") -> None:
        # ? Future versions could include thread management. Could be an interesting way to start learning about parallelism and concurrency.
        self._master_frame: tk.Frame = tk.Frame(GUI.__root, bg=Color.test2_bg)
        self._window_height: int = 0
        self._window_width: int = 0
        self.__create_menu: CreateMenu = CreateMenu(self._master_frame, initialize_window=self._initialize_root, change_menu=self._change_menu, optimization_history=optimization_history, data=data, window_width=750, window_height=500)
        self.__exit_menu: ExitMenu = ExitMenu(self._master_frame, self._initialize_root)
        self.__main_menu: MainMenu = MainMenu(self._master_frame, self._initialize_root, self._change_menu, program_version)
        self.__select_menu: SelectMenu = SelectMenu(self._master_frame, self._initialize_root, self._change_menu, optimization_history, window_width=750, window_height=500)
        self.__menus: dict = {"exit": self.__exit_menu, "main": self.__main_menu, "select": self.__select_menu, "create": self.__create_menu}
        self.optimization_history = optimization_history

    # ! Consider organizing the module files in module packages so graphics/ isn't too messy
    def _change_menu(self, menu_name="") -> None:
        if menu_name in self.__menus:
            for menu in self.__menus.values():
                menu.forget()
            self.__menus[menu_name].display()
            print(menu_name)
            # print(self.optimization_history)
        else:
            raise Exception(f"Menu {menu_name} not found.")

    def _initialize_root(self, width: int, height: int, title: str = "Particle Swarm Optimization (PSO)") -> None:
        GUI.__root.title(title)

        # * Setting initial geometry (dimensions)
        GUI.__root.resizable(False, False)
        screen_width: int = GUI.__root.winfo_screenwidth()
        screen_height: int= GUI.__root.winfo_screenheight()
        self.__window_width: int = width
        self.__window_height: int = height
        top_left_x: int = (screen_width // 2) - (self.__window_width // 2)
        top_left_y: int = (screen_height // 2) - (self.__window_height // 2)
        GUI.__root.geometry(f"{self.__window_width}x{self.__window_height}+{top_left_x}+{top_left_y}")
        self._master_frame.place(x=0, y=0, width=width, height=height)

        # * Setting icon for the application switcher, the dock and the taskbar (Windows)
        small_logo_path: str = "graphics/assets/logo.png"
        large_logo_path: str = small_logo_path
        small_logo: tk.PhotoImage = tk.PhotoImage(file=small_logo_path).subsample(10)
        large_logo: tk.PhotoImage = tk.PhotoImage(file=large_logo_path)
        GUI.__root.iconphoto(False, small_logo, large_logo)

        # * Setting background color
        GUI.__root.configure(bg=Color.window_bg)

    def run(self):
        self._change_menu("main")
        print(GUI.__root.mainloop())

if __name__ == "__main__":
    gui = GUI(optimization_history=[], program_version="0.9.9")
    gui.run()