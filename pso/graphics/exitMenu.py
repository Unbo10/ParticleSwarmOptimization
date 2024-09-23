import tkinter as tk
from tkinter import font

from pso.graphics.colors import Color
from pso.graphics.fonts import FontName

class ExitMenu():
    """ 
    Class that manages the exit menu of the GUI.
    """
    def __init__(self, parent_frame: tk.Frame, initialize_window: callable):
        self.__parent_frame: tk.Frame = parent_frame
        self.root: tk.Frame = tk.Frame(parent_frame,
            bg=Color.goodbye_frame_bg)
        self.__initialize_window: callable = initialize_window
        self.__image: tk.PhotoImage = tk.PhotoImage(
            file="graphics/assets/goodbye.png").subsample(2)
        self.__label: tk.Label = tk.Label(self.root, image=self.__image, bg=Color.goodbye_label_bg, borderwidth=0, highlightthickness=0) 
        self.__text: tk.Text = tk.Text(self.root, bg=Color.goodbye_frame_bg, wrap="word", font=font.Font(family=FontName.label, size=25), fg=Color.goodbye_text_fg, background=Color.goodbye_text_bg, borderwidth=0, highlightthickness=0)
        self.__text.insert(index="end", chars="Goodbye!")
        self.__text.tag_config(tagName="center", justify="center")
        self.__text.tag_add("center", "1.0", "end")
        self.__text.config(state="disabled")

    def display(self) -> None:
        self.__initialize_window(width=250, height=250, title="See you later!")
        self.root.rowconfigure(0, weight=0)
        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.__label.grid(row=0, column=0, pady=(25, 0), sticky="nsew")
        self.__text.grid(row=1, column=0, pady=(25, 25), sticky="nsew")
        # ? A more rigurous way of centering the label and the text could be implemented.
        self.__label.image = self.__image
        self.root.place(x=0, y=0, width=250, height=250)
        self.__parent_frame.after(500, self.__parent_frame.quit)

    def forget(self):
        self.root.forget()

    