import tkinter as tk
from tkinter import font

from pso.graphics.bottomFrame import BottomFrame
from pso.graphics.fonts import FontName
from pso.graphics.colors import Color

class MainMenu():
    def __init__(self, root_frame: tk.Frame, initialize_window: callable):
        self.root: tk.Frame = root_frame
        self.__root_frame: tk.Frame = tk.Frame(self.root)
        self.__initialize_window: callable = initialize_window
        pass

    # ! May need another class for the info and button frame (a single one and the two will be objects of that class).

    # * The baseMenu idea was discarded to avoid a circular import with GUI.

    def display_options(self):
        pass
            
    def display(self):
        """
        """
        self.__initialize_window(width=250, height=250)
    # * Setting title
        self._title_height: int = 40
        title: tk.Label = tk.Label(self.__root_frame, text="PSO manager",
            bg=Color.optim_label_bg, font=font.Font(family=FontName.title, size=15), wraplength=450,
            anchor="center")
        title.place(x=0, y=0, width=self.__window_width,
            height=self._title_height)

    # * Setting center (optimization) frame
        OPTIM_BUTTON_PADDING: int = 10
        self._button_frame: tk.Frame = tk.Frame(self.__root_frame, bg=Color.window_bg)
        self._bottom_frame_height: int = 30
        self.bottom_frame = BottomFrame(self.__root_frame, self._button_frame, self._title_height, self._bottom_frame_height)
        self._button_frame.rowconfigure(0, weight=1)
        self._button_frame.rowconfigure(1, weight=1)
        self._button_frame.rowconfigure(2, weight=1)
        self._button_frame.rowconfigure(3, weight=1)
        self._button_frame.columnconfigure(0, weight=1)
        optimization_button_parameters: dict = {
            "bg": Color.optim_button_bg,
            "fg": Color.optim_button_fg,
            "relief": "flat",
            "font": font.Font(family=FontName.button, size=10),
            "activebackground": Color.optim_button_abg,
            "activeforeground": Color.optim_button_afg,
            "highlightbackground": Color.optim_button_hbg,
            "highlightcolor": Color.optim_button_hcolor,
            "highlightthickness": 1,
            "cursor": "hand2"
            }

        def menu_button_on_click(e, button: tk.Button) -> None:
            button.focus_set()
            button.config(activebackground=Color.optim_button_cbg, activeforeground=Color.optim_button_cfg)

        def menu_button_on_release(self, e, button: tk.Button) -> None:
            button.config(activebackground=Color.optim_button_abg, activeforeground=Color.optim_button_afg)
            button_text: str = button.cget("text")
            title.place_forget()
            self._button_frame.place_forget()
            self.bottom_frame.place_forget()
            if button_text == "Create optimization":
                self.__display_create_menu()
            elif button_text == "Select optimization":
                self.__display_select_menu()
            elif button_text == "Delete optimization":
                self.__display_delete_menu()
            elif button_text == "Exit":
                self.__display_exit_menu()
                self.__root_frame.after(1000, self.__root_frame.quit)
            else:
                raise ValueError("Invalid button pressed.")

        create_button: tk.Button = tk.Button(
            self._button_frame,
            text="Create optimization",
            **optimization_button_parameters
            )
        create_button.focus_set()
        create_button.bind("<Button-1>",
            lambda event: menu_button_on_click(event, create_button))
        create_button.bind("<ButtonRelease-1>",
            lambda event: menu_button_on_release(self, event, create_button))
        create_button.grid(row=0, column=0, pady=OPTIM_BUTTON_PADDING,
            padx=4*OPTIM_BUTTON_PADDING, sticky="nsew")
        select_button: tk.Button = tk.Button(
            self._button_frame,
            text="Select optimization",
            **optimization_button_parameters
            )
        select_button.bind("<Button-1>",
            lambda event: menu_button_on_click(event, select_button))
        select_button.bind("<ButtonRelease-1>",
            lambda event: menu_button_on_release(self, event, select_button))
        select_button.grid(row=1, column=0, pady=(0,OPTIM_BUTTON_PADDING), padx=4*OPTIM_BUTTON_PADDING, sticky="nsew")
        delete_button: tk.Button = tk.Button(
            self._button_frame,
            text="Delete optimization",
            **optimization_button_parameters
            )
        delete_button.bind("<Button-1>",
            lambda event: menu_button_on_click(event, delete_button))
        delete_button.bind("<ButtonRelease-1>",
            lambda event: menu_button_on_release(self, event, delete_button))
        delete_button.grid(row=2, column=0, pady=(0,OPTIM_BUTTON_PADDING), padx=4*OPTIM_BUTTON_PADDING, sticky="nsew")
        exit_button: tk.Button = tk.Button(
            self._button_frame,
            text="Exit",
            **optimization_button_parameters
            )
        exit_button.bind("<Button-1>",
            lambda event: menu_button_on_click(event, exit_button))
        exit_button.bind("<ButtonRelease-1>",
            lambda event: menu_button_on_release(self, event, exit_button))
        exit_button.grid(row=3, column=0, pady=(0,OPTIM_BUTTON_PADDING), padx=4*OPTIM_BUTTON_PADDING, sticky="nsew")
        # ? How do you add multiple suggestions to parameters like sticky does?

        self._button_frame.place(x=0, y=self._title_height, width=self.__window_width, height=self.__window_height - (self._title_height + self._bottom_frame_height))

    