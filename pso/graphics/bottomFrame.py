import tkinter as tk
from tkinter import font

from pso.graphics.colors import Color
from pso.graphics.fonts import FontName

class BottomFrame():
    def __init__(self, parent_frame: tk.Frame, window_width: int, window_height, title_height: int, bottom_frame_height: int, program_version: str):
        # ! Pop-up frame must be another class
        self.root: tk.Frame = tk.Frame(parent_frame, bg=Color.test1_bg)
        self.__window_width: int = window_width
        self.__window_height: int = window_height
        self.__title_height: int = title_height
        self.root_height: int = bottom_frame_height
        self.__POP_UP_FRAME_HEIGHT: int = self.__window_height - title_height - self.root_height

        self.__button_parameters: dict = {
            "relief": "flat",
            "bg": Color.bottom_button_bg,
            "activebackground": Color.bottom_button_abg,
            "highlightbackground": Color.bottom_button_hbg,
            "highlightcolor": Color.bottom_button_hcolor,
            "highlightthickness": 1,
            "borderwidth": 0,
            "cursor": "hand2"
            }
        self.__info_image: tk.PhotoImage = tk.PhotoImage(file="assets/info.png").subsample(3)
        self.__info_active_image: tk.PhotoImage = tk.PhotoImage(file="assets/info-active.png").subsample(3)
        self.__help_image: tk.PhotoImage = tk.PhotoImage(file="assets/help.png").subsample(3)
        self.__help_active_image: tk.PhotoImage = tk.PhotoImage(file="assets/help-active.png").subsample(3)
        self.__info_button: tk.Button = tk.Button(
            self.root,
            image=self.__info_image,
            **self.__button_parameters
            )
        
        self.__help_button: tk.Button = tk.Button(
            self.root,
            image=self.__help_image,
            **self.__button_parameters
            )
        self.__version_label: tk.Label = tk.Label(
            self.root,
            text=f"V {program_version}",
            bg=Color.bottom_button_bg,
            fg=Color.bottom_button_fg,
            font=font.Font(family=FontName.label, size=10, weight="bold")
            )

        self.__frames_visibility: dict = {"info": False, "help": False}
        self.__info_frame: tk.Frame = tk.Frame(parent_frame)
        self.__help_frame: tk.Frame = tk.Frame(parent_frame)
        self.__hide_button_parameters: dict = {
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
        self.__info_hide_button: tk.Button = tk.Button(self.__info_frame,
            **self.__hide_button_parameters)
        self.__help_hide_button: tk.Button = tk.Button(self.__help_frame,
            **self.__hide_button_parameters)
        self.__scrollbar_parameters: dict = {
            "bg": Color.bottom_scrollbar_bg,
            "activebackground": Color.bottom_scrollbar_abg,
            "troughcolor": Color.bottom_scrollbar_trough,
            "highlightbackground": Color.bottom_scrollbar_hbg,
            "highlightcolor": Color.bottom_scrollbar_hcolor,
            "highlightthickness": 1,
            "borderwidth": 0,
            "elementborderwidth": 0,
            "width": 10,
            }
        self.__info_scrollbar: tk.Scrollbar = tk.Scrollbar(self.__info_frame,
            **self.__scrollbar_parameters)
        self.__help_scrollbar: tk.Scrollbar = tk.Scrollbar(self.__help_frame,
            **self.__scrollbar_parameters)
        self.__text_parameters: dict = {
            "bg": Color.bottom_label_bg,
            "fg": Color.bottom_label_fg,
            "font": font.Font(family=FontName.label, size=10),
            "wrap": "word",
            "padx": 5,
            "pady": 5,  
            "borderwidth": 0,
            "highlightthickness": 0
            }
        self.__info_text: tk.Text = tk.Text(self.__info_frame,
            **self.__text_parameters)
        self.__help_text: tk.Text = tk.Text(self.__help_frame,
            **self.__text_parameters)

    def display(self, options_frame: tk.Frame):
        self.options_frame: tk.Frame = options_frame        
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.__info_button.grid(row=0, column=0, sticky="nsew")
        self.__info_button.bind("<Enter>", self.__enter_info_button)
        self.__info_button.bind("<Leave>", self.__leave_info_button)
        self.__info_button.bind("<Button-1>", self.__click_info_button)
        self.__info_button.bind("<ButtonRelease-1>", self.__release_info_button)
        self.__info_button.bind("<KeyRelease-Return>", self.__release_info_button)

        self.__help_button.grid(row=0, column=1, sticky="nsew")
        self.__help_button.bind("<Enter>", self.__enter_help_button)
        self.__help_button.bind("<Leave>", self.__leave_help_button)
        self.__help_button.bind("<Button-1>", self.__click_help_button)
        self.__help_button.bind("<ButtonRelease-1>", self.__release_help_button)
        self.__help_button.bind("<KeyRelease-Return>", self.__release_help_button)
        self.__version_label.grid(row=0, column=2, sticky="nsew")
        self.root.place(x=0, y=self.__window_height - self.root_height, width=self.__window_width, height=self.root_height)

        # * Displaying the information frame
        self.__info_frame.columnconfigure(0, weight=1)
        self.__info_frame.columnconfigure(1, weight=0)
        self.__info_frame.rowconfigure(0, weight=0)
        self.__info_frame.rowconfigure(1, weight=1)
        self.__info_hide_button.bind("<Enter>", lambda event: self.__enter_hide_button(event, self.__info_hide_button))
        self.__info_hide_button.bind("<Leave>", lambda event: self.__leave_hide_button(event, self.__info_hide_button))
        self.__info_hide_button.bind("<Button-1>", lambda event: self.__click_hide_button(event, self.__info_hide_button))
        self.__info_hide_button.bind("<ButtonRelease-1>", self.__release_hide_button)
        self.__info_hide_button.bind("<KeyRelease-Return>", self.__release_hide_button)
        self.__info_hide_button.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.__info_text.config(state="normal") # * Allow adding text
        self.__info_text.insert(index="end", chars="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?")
        self.__info_text.tag_config(tagName="center", justify="center")
        self.__info_text.tag_add("center", "1.0", "end") # * ???
        self.__info_text.config(state="disabled")
        self.__info_text.config(yscrollcommand=self.__info_scrollbar.set)
        self.__info_scrollbar.config(command=self.__info_text.yview)
        self.__info_text.grid(row=1, column=0)
        self.__info_scrollbar.grid(row=1, column=1, sticky="ns")

        # * Displaying the help frame
        self.__help_frame.columnconfigure(0, weight=1)
        self.__help_frame.columnconfigure(1, weight=0)
        self.__help_frame.rowconfigure(0, weight=0)
        self.__help_frame.rowconfigure(1, weight=1)
        self.__help_hide_button.bind("<Enter>", lambda event: self.__enter_hide_button(event, self.__help_hide_button))
        self.__help_hide_button.bind("<Leave>", lambda event: self.__leave_hide_button(event, self.__help_hide_button))
        self.__help_hide_button.bind("<Button-1>", lambda event: self.__click_hide_button(event, self.__help_hide_button))
        self.__help_hide_button.bind("<ButtonRelease-1>", self.__release_hide_button)
        self.__help_hide_button.bind("<KeyRelease-Return>", self.__release_hide_button)
        self.__help_hide_button.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.__help_text.config(state="normal") # * Allow adding text
        self.__help_text.insert(index="end", chars=" aaaaaaaaaaaaa Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?")
        self.__help_text.tag_config(tagName="center", justify="center")
        self.__help_text.tag_add("center", "1.0", "end") # * ???
        self.__help_text.config(state="disabled")
        self.__help_text.config(yscrollcommand=self.__help_scrollbar.set)
        self.__help_scrollbar.config(command=self.__help_text.yview)
        self.__help_text.grid(row=1, column=0)
        self.__help_scrollbar.grid(row=1, column=1, sticky="ns")
    
    # TODO: Test in Windows if 

    def __enter_info_button(self, e):
        self.__info_button.config(image=self.__info_active_image, bg=Color.bottom_button_abg)
    
    def __enter_help_button(self, e):
        self.__help_button.config(image=self.__help_active_image, bg=Color.bottom_button_abg)

    def __enter_hide_button(self, e, button: tk.Button):
        button.config(activebackground=Color.hide_button_abg, activeforeground=Color.hide_button_afg)

    def __leave_info_button(self, e):
        self.__info_button.config(image=self.__info_image, bg=Color.bottom_button_bg)

    def __leave_help_button(self, e):
        self.__help_button.config(image=self.__help_image, bg=Color.bottom_button_bg)

    def __leave_hide_button(self, e, button: tk.Button):
        button.config(bg=Color.hide_button_bg, fg=Color.hide_button_fg)

    def __click_info_button(self, e):
        self.__info_button.config(
            image=self.__info_image,
            activebackground=Color.bottom_button_cbg
            )
    
    def __click_help_button(self, e):
        self.__help_button.config(
            image=self.__help_image,
            activebackground=Color.bottom_button_cbg
            )
    
    def __click_hide_button(self, e: tk.Event, button:tk.Button):
        button.config(bg=Color.hide_button_cbg, fg=Color.hide_button_cfg, activebackground=Color.hide_button_cbg, activeforeground=Color.hide_button_cfg)

    def __release_info_button(self, event: tk.Event):
        # * type 3 is KeyRelease-Return and type 5 is Button1-Release
        # * Although they are printed as integers, they are strings, and they must be refered to with single quotes.
        if event.type == '3':
            pass
        elif event.type == '5':
            self.__info_button.config(
                image=self.__info_active_image,
                activebackground=Color.bottom_button_abg,
                bg=Color.bottom_button_abg
                )
        if self.__frames_visibility["info"] == False:
            self.options_frame.place_forget()
            self.__help_frame.place_forget()
            self.__info_frame.place(x=0, y=self.__title_height, width=self.__window_width, height=self.__POP_UP_FRAME_HEIGHT)
            self.__frames_visibility["info"] = True
            self.__frames_visibility["help"] = False
        
        elif self.__frames_visibility["info"] == True:
            self.options_frame.place(x=0, y=self.__title_height, width=self.__window_width, height=self.__window_height - (self.__title_height + self.root_height))
            self.__info_frame.place_forget()
            self.__help_frame.place_forget()
            self.__frames_visibility["info"] = False
            self.__frames_visibility["help"] = False
        
        else:
            raise NotImplementedError("Menu not implemented on release method.")

    
    def __release_help_button(self, event: tk.Event):
        if event.type == '3':
            pass
        elif event.type == '5':
            self.__help_button.config(
                image=self.__help_active_image,
                activebackground=Color.bottom_button_abg,
                bg=Color.bottom_button_abg
                )
        if self.__frames_visibility["help"] == False:
            self.options_frame.place_forget()
            self.__info_frame.place_forget()
            self.__help_frame.place(x=0, y=self.__title_height, width=self.__window_width, height=self.__POP_UP_FRAME_HEIGHT)
            self.__frames_visibility["help"] = True
            self.__frames_visibility["info"] = False

        elif self.__frames_visibility["help"] == True:
            self.options_frame.place(x=0, y=self.__title_height, width=self.__window_width, height=self.__window_height - (self.__title_height + self.root_height))
            self.__help_frame.place_forget()
            self.__info_frame.place_forget()
            self.__frames_visibility["help"] = False
            self.__frames_visibility["info"] = False
        
        else:
            raise NotImplementedError("Menu not implemented on release method.")

    def __release_hide_button(self, e):
        self.__info_frame.place_forget()
        self.__help_frame.place_forget()
        self.options_frame.place(x=0, y=self.__title_height, width=self.__window_width, height=self.__window_height - (self.__title_height + self.root_height))
        self.__frames_visibility["info"] = False
        self.__frames_visibility["help"] = False
