import os

import tkinter as tk
from tkinter import font

from pso.graphics.colors import Color
from pso.graphics.fonts import FontName
from pso.optimization import Optimization
from pso.graphics.optimizationFrame import OptimizationFrame
from pso.graphics.optionsButton import OptionsButton

class SelectMenu():
    def __init__(self, parent_frame: tk.Frame, initialize_window: callable, change_menu: callable, optimization_history: list[Optimization], window_width: int, window_height: int):
        # ! Add highlight color to the back button as well as KeyRelease-Return binding support
        self.__change_menu: callable = change_menu
        self.__optimization_history: list[Optimization] = optimization_history
        self.__window_width: int = window_width
        self.__window_height: int = window_height
        self.__initialize_window: callable = initialize_window
        self.__title_height: int = 2 # * Text units, not pixels. It doesn't correspond exactly to the size of the font. Default is 17, Ubuntu size 15 is 15 + 9 = 24 px.
        self.root: tk.Frame = tk.Frame(parent_frame, bg=Color.test1_bg)

        self.__title: tk.Label = tk.Label(self.root, text="Select a previous optimization", height=self.__title_height, bg=Color.select_title_bg, fg=Color.select_title_fg, font=font.Font(family=FontName.title, size=15))
        # print(font.Font(family=FontName.title, size=15).metrics("linespace"))
        self.__canvas: tk.Canvas = tk.Canvas(self.root, bg=Color.test1_bg)
        container_frame_y_padding: int = 30
        self.__container_frame_height: int = self.__window_height - (self.__title_height + container_frame_y_padding)
        self.__container_frame_width: int = self.__window_width - container_frame_y_padding
        self.__container_frame: tk.Frame = tk.Frame(self.__canvas, bg=Color.test3_bg) # * Will be the basis for the canvas of optimization frames and the scrollbar
        self.__scrollbar_width: int = 20
        self.__scrollbar: tk.Scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.__canvas.yview)
        # ! tk.Buttons could actually be overriden to get the best out of inheritance, especially in MainMenu
        arrow_back_path: str = "assets/arrow-back.png"
        self.__arrow_back_image: tk.PhotoImage = tk.PhotoImage(file=arrow_back_path).subsample(4)
        arrow_back_path_active: str = "assets/arrow-back-active.png"
        self.__arrow_back_image_active: tk.PhotoImage = tk.PhotoImage(file=arrow_back_path_active).subsample(4)
        self.__back_button: tk.Button = tk.Button(self.root, image=self.__arrow_back_image, relief="flat", cursor="hand2", bg=Color.back_button_bg, activebackground=Color.back_button_abg, highlightthickness=0, borderwidth=0)
        self.__no_optimizations_label: tk.Label = tk.Label(self.root, height=2, text="Nop optimizations have been made yet.", bg=Color.select_label_no_optim_bg, fg=Color.select_label_no_optim_fg) # ? Should it be conditioned to the length of the optimization list being 0 or is it good like this?
        self.__create_optimization_button: OptionsButton = OptionsButton(self.root, text="Create optimization", callable=change_menu, callable_args={"menu_name": "create"}, padx=(self.__window_width//2 - 250,)*2, pady=(0,0))
        self.__optimization_frames: list[OptimizationFrame] = []

    def __enter__back_button(self, e):
        self.__back_button.config(image=self.__arrow_back_image_active, bg=Color.back_button_abg)    
    def __leave_back_button(self, e):
        self.__back_button.config(image=self.__arrow_back_image, bg=Color.back_button_bg)

    def __click_back_button(self, e):
        self.__back_button.config(activebackground=Color.back_button_cbg, bg=Color.back_button_cbg, image=self.__arrow_back_image)
    
    def __release_back_button(self, event: tk.Event):
        self.__change_menu("main")

    def display(self):
        self.__title_height = 2 # * To avoid recording the value from the previous display call
        self.__initialize_window(width=self.__window_width, height=self.__window_height, title="Select optimization - PSO")
        self.__title.pack(fill="x", anchor="e")
        self.__back_button.bind("<Enter>", self.__enter__back_button)
        self.__back_button.bind("<Leave>", self.__leave_back_button)
        self.__back_button.bind("<Button-1>", self.__click_back_button)
        self.__back_button.bind("<ButtonRelease-1>", self.__release_back_button)
        self.__back_button.place(x=0, y=0, height=self.__title_height * 25, width=self.__title_height * 25)

        if len(self.__optimization_history) == 0:
            print("len 0")
            self.__no_optimizations_label.pack(fill="both", anchor="center", pady=(20, 0), padx=(self.__window_width//2) - 250)
            self.__create_optimization_button.pack_display(fill="x", anchor="center")

        else:
            index = 0
            for optimization in self.__optimization_history:
                self.__optimization_frames.append(OptimizationFrame(self.__container_frame, optimization, width=self.__container_frame_width - 50, scrollbar_width=self.__scrollbar_width, height=120, separation=20, frame_index=index))
                index += 1
            for optim_frame in self.__optimization_frames:
                for child in optim_frame.frame.winfo_children() + [optim_frame.frame]:
                    child.bind("<MouseWheel>", self.__scroll_mouse_wheel)
                    child.bind("<Button-4>", self.__scroll_mouse_wheel)
                    child.bind("<Button-5>", self.__scroll_mouse_wheel)
            self.__container_frame.bind("<MouseWheel>", self.__scroll_mouse_wheel)
            self.__container_frame.bind("<Button-4>", self.__scroll_mouse_wheel)
            self.__container_frame.bind("<Button-5>", self.__scroll_mouse_wheel)
            self.__title_height *= 25 # * To compensate for the difference between pixels and font size
            self.__canvas.place(y=(self.__title_height) + 15, x=15, width=self.__window_width - (30 + self.__scrollbar_width), height=self.__window_height - (self.__title_height + 30))
            self.__scrollbar.place(x=self.__window_width - (15 + self.__scrollbar_width), y=self.__title_height + 15, height=self.__window_height - (self.__title_height + 30), width=self.__scrollbar_width)
            self.__canvas.configure(yscrollcommand=self.__scrollbar.set)
            for frame in self.__optimization_frames:
                frame.display(self.__container_frame_width)
            self.__canvas.create_window((0, 0), window=self.__container_frame, anchor="nw", width=self.__container_frame_width, height=self.__container_frame_height) # * Creates a window inside the current tk.Tk() window, so it only displays a certain portion of the widgets contained inside.
            self.__canvas.configure(scrollregion=self.__canvas.bbox("all"))
        self.root.place(x=0, y=0, width=self.__window_width, height=self.__window_height)
        # print(self.__window_width, self.__window_height)

    def __scroll_mouse_wheel(self, event):
            if os.name == "nt":
                self.__canvas.yview_scroll(int(-1*(event.delta/120)), "units")
            elif os.name == "posix":
                if event.num == 4:
                    self.__canvas.yview_scroll(-1, "units")
                elif event.num == 5:
                    self.__canvas.yview_scroll(1, "units")

    def forget(self):
        self.root.place_forget()
        self.__canvas.place_forget()

