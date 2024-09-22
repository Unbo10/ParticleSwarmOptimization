import tkinter as tk

from pso.graphics.colors import Color

class BackButton(tk.Button):
    def __init__(self, menu_frame, image: tk.PhotoImage, active_image: tk.PhotoImage, width: int, height: int,  change_menu: callable, change_menu_args: dict = {"menu_name": "main"}, cbg: str = Color.back_button_cbg, args: dict = {
        "bg": Color.back_button_bg,
        "activebackground": Color.back_button_abg,
        "relief": "flat", 
        "cursor": "hand2",
        "highlightcolor": Color.back_button_hcolor,
        "highlightthickness": 1
        }):
        super().__init__(menu_frame, image=image, **args)
        self.__image: tk.PhotoImage = image
        self.__active_image: tk.PhotoImage = active_image
        self.__width: int = width
        self.__height: int = height
        self.__change_menu: callable = change_menu
        self.__change_menu_args: dict = change_menu_args

    def __enter(self, e) -> None:
        self.config(bg=Color.back_button_abg, activebackground=Color.back_button_abg, image=self.__active_image)

    def __leave(self, e) -> None:
        self.config(bg=Color.back_button_bg, image=self.__image)

    def __click(self, e) -> None:
        self.config(bg=Color.back_button_cbg, activebackground=Color.back_button_cbg, image=self.__image)

    def __release(self, e) -> None:
        self.__change_menu(**self.__change_menu_args)

    # ! Consider binding to events in the initializer so that every time a widget is displayed it doesn't need to bind events again.
    # * To keep the code consistent, might be better to leave it there, because BottomButton objects do need it to be there

    def __bind_to_events(self) -> None:
        self.bind("<Enter>", self.__enter)
        self.bind("<Leave>", self.__leave)
        self.bind("<Button-1>", self.__click)
        self.bind("<ButtonRelease-1>", self.__release)
        self.bind("<KeyRelease-Return>", self.__release)

    def display(self, x: int, y: int) -> None:
        self.__bind_to_events()
        self.place(x=x, y=y, width=self.__width, height=self.__height)