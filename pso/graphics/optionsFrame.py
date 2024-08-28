"""
This module defines the OptionsFrame class, which sets the buttons on the frame, to open their respectives menus.

## Classes
- OptionsFrame: Represents the options frame in a graphical user interface.

### Attributes
- __root_frame: tk.Frame - The root frame for the options frame.
- root: tk.Frame - The main frame for the options frame.
- __change_menu: callable - A callable to change the menu.
- __title: tk.Label - Label displaying the title of the options frame.
- __window_width: int - The width of the window.
- __window_height: int - The height of the window.
- __title_height: int - The height of the title.
- __bottom_frame_height: int - The height of the bottom frame.
- __button_parameters: dict - Parameters for the buttons.
- __create_button: tk.Button - Button to create an optimization.
- __select_button: tk.Button - Button to select an optimization.
- __delete_button: tk.Button - Button to delete an optimization.
- __exit_button: tk.Button - Button to exit the application.
- __buttons: list - List of buttons in the options frame.
- __bottom_frame: tk.Frame - The bottom frame of the options frame.

### Methods
# - display(bottom_frame: tk.Frame): Displays the options frame and configures the buttons.
- __enter_button(e, button: tk.Button): Changes the background and foreground of the button when the cursor enters.
- __leave_button(e, button: tk.Button): Restores the background and foreground of the button when the cursor leaves.
- __click_button(e, button: tk.Button): Changes the background and foreground of the button when clicked.
- __release_button(e, button: tk.Button) -> None: Handles the button release event and changes the menu based on the button text.
"""
import tkinter as tk
from tkinter import font

from pso.graphics.colors import Color
from pso.graphics.fonts import FontName

class OptionsFrame():
    def __init__(self, root_frame: tk.Frame, title: tk.Label, change_menu: callable,  window_width: int, window_height: int, title_height, bottom_frame_height: int):
        self.__root_frame: tk.Frame = root_frame
        self.root: tk.Frame = tk.Frame(root_frame, bg=Color.window_bg)
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
            "cursor": "hand2"
            }
        self.__create_button: tk.Button = tk.Button(
            self.root,
            text="Create optimization",
            **self.__button_parameters
            )
        self.__select_button: tk.Button = tk.Button(
            self.root,
            text="Select optimization",
            **self.__button_parameters
            )
        self.__delete_button: tk.Button = tk.Button(
            self.root,
            text="Delete optimization",
            **self.__button_parameters
            )
        self.__exit_button: tk.Button = tk.Button(
            self.root,
            text="Exit",
            **self.__button_parameters
            )
        self.__buttons = [self.__create_button, self.__select_button, self.__delete_button, self.__exit_button]


    def display(self, bottom_frame: tk.Frame):
        self.__bottom_frame: tk.Frame = bottom_frame
        BUTTON_PADDING: int = 8
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.columnconfigure(0, weight=1)
        # * Binding all the buttons to different events
        self.__create_button.focus_set()
        button_row = 0
        for button in self.__buttons:
            # * Lambda needs to have two arguments because any variable that's not a default argument is pointed to by reference, so at the end, all will have the same argument (in this case, exit button) 
            button.bind("<Enter>", lambda event, b=button: self.__enter_button(event, b))
            button.bind("<Leave>", lambda event, b=button: self.__leave_button(event, b))
            button.bind("<Button-1>", lambda event, b=button: self.__click_button(event, b))
            button.bind("<ButtonRelease-1>", lambda event, b=button: self.__release_button(event, b))
            button.bind("<KeyRelease-Return>", lambda event, b=button: self.__release_button(event, b))
            button.grid(row=button_row, column=0, pady=BUTTON_PADDING,
                padx=4*BUTTON_PADDING, sticky="nsew")
            button_row += 1
        # ! CHECK: Functionality of the binding in Windows
        frame_width = self.__window_width
        frame_height = self.__window_height - (self.__title_height + self.__bottom_frame_height)
        self.root.place(x=0, y=self.__title_height, width=frame_width, height=frame_height)

    # * Could be changed to class methods in the future. All except release
    def __enter_button(self, e, button: tk.Button):
        button.config(activebackground=Color.optim_button_abg, activeforeground=Color.optim_button_afg)
    
    def __leave_button(self, e, button: tk.Button):
        button.config(bg=Color.optim_button_bg, fg=Color.optim_button_fg)
    
    def __click_button(self, e, button: tk.Button):
        button.config(activebackground=Color.optim_button_cbg, activeforeground=Color.optim_button_cfg)
    
    def __release_button(self, e, button: tk.Button) -> None:
        button_text: str = button.cget("text")
        self.__title.place_forget()
        self.root.place_forget()
        self.__bottom_frame.place_forget()
        if button_text == "Create optimization":
            self.__change_menu("create")
        elif button_text == "Select optimization":
            self.__change_menu("select")
        elif button_text == "Delete optimization":
            self.__change_menu("delete")
        elif button_text == "Exit":
            self.__change_menu("exit")
            self.__root_frame.after(1000, self.__root_frame.quit)
        else:
            raise ValueError("Invalid button pressed.")
