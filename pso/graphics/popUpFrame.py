
import tkinter as tk
from tkinter import font

from pso.graphics.colors import Color
from pso.graphics.fonts import FontName

class PopUpFrame(tk.Frame):
    def __init__(self, main_frame: tk.Frame, name: str, height: int, width: int, y: int, text: str):
        super().__init__(main_frame)
        self.name: str = name # ! Change to private when debugging is done
        self.__text_to_insert: str = text
        text_parameters: dict =  {
            "bg": Color.bottom_label_bg,
            "fg": Color.bottom_label_fg,
            "font": font.Font(family=FontName.label, size=10),
            "wrap": "word",
            "padx": 5,
            "pady": 5,  
            "borderwidth": 0,
            "highlightthickness": 0
        }
        self.__text: tk.Text = tk.Text(self, **text_parameters)
        button_parameters: dict = {
            "bg": Color.hide_button_bg,
            "fg": Color.hide_button_fg,
            "activebackground": Color.hide_button_abg,
            "activeforeground": Color.hide_button_afg,
            "highlightbackground": Color.hide_button_hbg,
            "highlightcolor": Color.hide_button_hcolor,
            "highlightthickness": 1,
            "font": font.Font(family=FontName.label, size=10, weight="bold"),
            "relief": "flat",
            "cursor": "hand2",
            "text": "Hide"
        }
        self.__text.config(state="normal") # ! Check if this line is necessary
        self.__text.insert(index="end", chars=self.__text_to_insert)
        self.__text.tag_config(tagName="center", justify="center")
        self.__text.tag_add("center", "1.0", "end") # ! Check which parameters do this args are being assigned to
        self.__text.config(state="disabled")
        self.__hide_button: tk.Button = tk.Button(self, **button_parameters)
        scrollbar_parameters: dict = {
            "bg": Color.bottom_scrollbar_bg,
            "activebackground": Color.bottom_scrollbar_abg,
            "troughcolor": Color.bottom_scrollbar_trough,
            "highlightbackground": Color.bottom_scrollbar_hbg,
            "highlightcolor": Color.bottom_scrollbar_hcolor,
            "highlightthickness": 1,
            "borderwidth": 0,
            "elementborderwidth": 1,
            "width": 10,
        }
        self.__scrollbar: tk.Scrollbar = tk.Scrollbar(self, scrollbar_parameters)
        self.__width: int = width
        self.__height: int = height
        self.__y: int = y
        self.visible: bool = False

    def __enter_hide_button(self, e) -> None:
        self.__hide_button.config(bg=Color.hide_button_abg, fg=Color.hide_button_afg, activebackground=Color.hide_button_abg, activeforeground=Color.hide_button_afg) # ? Is it necessary to change the abg and the afg?

    def __leave_hide_button(self, e) -> None:
        self.__hide_button.config(bg=Color.hide_button_bg, fg=Color.hide_button_fg)

    def __click_hide_button(self, e) -> None:
        self.__hide_button.config(bg=Color.hide_button_cbg, fg=Color.hide_button_cfg, activebackground=Color.hide_button_cbg, activeforeground=Color.hide_button_cfg)

    def __release_hide_button(self, e, other_frame: "PopUpFrame") -> None:
        self.visible = False
        self.place_forget()
        other_frame.visible = False
        other_frame.place_forget()

    def bind_hide_button(self, other_frame: "PopUpFrame") -> None:
        self.__hide_button.bind("<Enter>", self.__enter_hide_button)
        self.__hide_button.bind("<Leave>", self.__leave_hide_button)
        self.__hide_button.bind("<Button-1>", self.__click_hide_button)
        self.__hide_button.bind("<ButtonRelease-1>", lambda event: self.__release_hide_button(event, other_frame))
        self.__hide_button.bind("<KeyRelease-Return>", lambda event: self.__release_hide_button(event, other_frame))

    def display(self, other_frame: "PopUpFrame"):
        self.bind_hide_button(other_frame)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.__hide_button.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.__text.config(yscrollcommand=self.__scrollbar.set)
        self.__scrollbar.config(command=self.__text.yview)
        self.__text.grid(row=1, column=0, sticky="ew")
        self.__text.yview_moveto(0) # * Reset the visible area of the text.
        self.__scrollbar.grid(row=1, column=1, sticky="ns")
        self.place(x=0, y=self.__y, width=self.__width, height=self.__height)

    def get_name(self) -> str:
        return self.name