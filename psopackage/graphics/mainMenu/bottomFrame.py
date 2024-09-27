import tkinter as tk
from tkinter import font

from psopackage.graphics.colors import Color
from psopackage.graphics.fonts import FontName
from psopackage.graphics.mainMenu.bottomButton import BottomButton
from psopackage.graphics.mainMenu.popUpFrame import PopUpFrame

class BottomFrame(tk.Frame):
    """ 
    Manages the bottom frame of the GUI that contains the buttons for the info and help pop up frames.
    """
    def __init__(self, master_frame, menu_frame: tk.Frame, window_width: int, window_height, title_height: int, bottom_frame_height: int, program_version: str):
        super().__init__(menu_frame, bg=Color.test3_bg)
        self.__window_width: int = window_width
        self.__window_height: int = window_height
        self.__height: int = bottom_frame_height
        self._pop_up_frame_height: int = self.__window_height - title_height - self.__height

        info_image: tk.PhotoImage = tk.PhotoImage(file="graphics/assets/info.png").subsample(3)
        info_active_image: tk.PhotoImage = tk.PhotoImage(file="graphics/assets/info-active.png").subsample(3)
        self.__info_button: BottomButton = BottomButton(master_frame, self, image=info_image, active_image=info_active_image, name="info", pop_up_frame_height=self._pop_up_frame_height, pop_up_frame_width=self.__window_width, pop_up_frame_y=title_height, pop_up_text="This is a program to simulate the PSO algorithm. It's an optimization algorithm, that its purpose is to find the minimum of a function. As of Version 1.0.0, you manually select the function to be optimized, having four options, Sphere, Booth, Rastrigin and Goldstein-Price.")
        help_image: tk.PhotoImage = tk.PhotoImage(file="graphics/assets/help.png").subsample(3)
        help_active_image: tk.PhotoImage = tk.PhotoImage(file="graphics/assets/help-active.png").subsample(3)
        self.__help_button: BottomButton = BottomButton(master_frame, self, image=help_image, active_image=help_active_image, name="help", pop_up_frame_height=self._pop_up_frame_height, pop_up_frame_width=self.__window_width, pop_up_frame_y=title_height, pop_up_text="First, you click on create optimization, manually type the number of iterations, particles or the coefficients needed for the algorithm, and then you click Run Optimization. You then can go back to the menu and click Select optimization to view the results of it, displaying the particles graphed on each iteration. ALternatively, you can directly click View Results and it will redirect you to the select menu.")
        self._pop_up_frames: list[PopUpFrame] = [self.__help_button.pop_up_frame, self.__info_button.pop_up_frame] # ! Could be immutable actually
        
        self.__version_label: tk.Label = tk.Label(
            self,
            text=f"V {program_version}",
            bg=Color.bottom_button_bg,
            fg=Color.bottom_button_fg,
            font=font.Font(family=FontName.label, size=10, weight="bold")
            )

    def display(self):     
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.__info_button.display(self._pop_up_frames, row=0, column=0, sticky="nsew")
        self.__help_button.display(self._pop_up_frames, row=0, column=1, sticky="nsew")
        self.__version_label.grid(row=0, column=2, sticky="nsew")
        self.place(x=0, y=self.__window_height - self.__height, width=self.__window_width, height=self.__height)