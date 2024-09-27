
import tkinter as tk

from psopackage.graphics.colors import Color
from psopackage.graphics.selectMenu.viewFrame import ViewFrame
from psopackage.optimization import Optimization

class ViewButton(tk.Button):
    """ 
    Sets the button to change the windonw and show the optimization.
    """
    def __init__(self, master: tk.Frame, image: tk.Image, active_image: tk.Image, forget_select_menu: callable, initialize_window: callable, change_menu: callable,optimization: Optimization, bg: str = Color.select_label_optim_bg, fg: str=Color.select_label_optim_fg) -> "ViewButton":
        super().__init__(master=master, image=image, bg=bg, fg=fg)
        self.__image: tk.Image = image
        self.__active_image: tk.Image = active_image
        self.view_frame: ViewFrame = ViewFrame(optimization=optimization, initialize_window=initialize_window, change_menu=change_menu, function_fig=optimization.function_fig)
        self.__forget_select_menu: callable = forget_select_menu
        self.__bind_to_events()

    def __enter(self, e):
        self.config(bg=Color.preview_button_abg, image=self.__active_image)

    def __leave(self, e):
        self.config(bg=Color.preview_button_bg, image=self.__image)

    def __click(self, e):
        self.config(bg=Color.preview_button_cbg, image=self.__image)

    def __release(self, e):
        self.__forget_select_menu()
        self.view_frame.display()
    
    def __bind_to_events(self) -> None:
        self.bind("<Enter>", self.__enter)
        self.bind("<Leave>", self.__leave)
        self.bind("<Button-1>", self.__click)
        self.bind("<ButtonRelease-1>", self.__release)
        self.bind("<KeyRelease-Return>", self.__release)