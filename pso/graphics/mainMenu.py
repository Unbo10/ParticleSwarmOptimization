import tkinter as tk
from tkinter import font

from pso.graphics.fonts import FontName
from pso.graphics.colors import Color

class MainMenu():
    def __init__(self, root_frame: tk.Frame, initialize_window: callable):
        self.root: tk.Frame = root_frame
        self.__root_frame: tk.Frame = tk.Frame(self.root, bg=Color.opti)
        self.__initialize_window: callable = initialize_window
        pass

    # ! May need another class for the info and button frame (a single one and the two will be objects of that class).

    # ? A baseMenu class could also be created.

    def display_options(self):
        pass
            
    def display(self):
        """
        """
        self.__initialize_root(width=250, height=250)
    # * Setting title
        title_height: int = 40
        title: tk.Label = tk.Label(self.__root_frame, text="PSO manager",
            bg=Color.optim_label_bg, font=font.Font(family=FontName.title, size=15), wraplength=450,
            anchor="center")
        title.place(x=0, y=0, width=self.__window_width,
            height=title_height)

        bottom_frame_height: int = 30

    # ! In future versions the bottom, help and info frames could be instance attributes to allow object clients to modify them to their requirements.
    # * Setting bottom frame
        bottom_frame: tk.Frame = tk.Frame( self.__root_frame,
            bg=Color.bottom_button_abg)
        bottom_frame.rowconfigure(0, weight=1)
        bottom_frame.columnconfigure(0, weight=1)
        bottom_frame.columnconfigure(1, weight=1)
        bottom_frame.columnconfigure(2, weight=1)

        bottom_button_parameters: dict = {
            "bg": Color.bottom_button_bg,
            "relief": "flat",
            "activebackground": Color.bottom_button_abg,
            "highlightbackground": Color.bottom_button_hbg,
            "highlightcolor": Color.bottom_button_hcolor,
            "highlightthickness": 1,
            "borderwidth": 0,
            "cursor": "hand2"
            }
        # TODO: Consider loading the active image with a darker color over a lighter background

        info_image: tk.PhotoImage = tk.PhotoImage(file="assets/info.png").subsample(3)
        info_active_image: tk.PhotoImage = tk.PhotoImage(file="assets/info-active.png").subsample(3)
        help_image: tk.PhotoImage = tk.PhotoImage(file="assets/help.png").subsample(3)
        help_active_image: tk.PhotoImage = tk.PhotoImage(file="assets/help-active.png").subsample(3)
        images_str: dict = {
                "info_image": str(info_image),
                "info_active_image": str(info_active_image),
                "help_image": str(help_image),
                "help_active_image": str(help_active_image)
            }
        print(images_str)

        def bottom_button_on_enter(e, button:tk.Button) -> None:
            if (button.cget("image") == images_str["info_image"]) or (button.cget("image") == images_str["info_active_image"]):
                button.config(image=info_active_image)
            elif button.cget("image") == images_str["help_image"]:
                button.config(image=help_active_image)
            else:
                raise ValueError("Invalid button pressed. Image associated:", str(button.cget("image")))

        def bottom_button_on_leave(e, button:tk.Button) -> None:
            if button.cget("image") == images_str["info_active_image"]:
                button.config(image=info_image)
            elif button.cget("image") == images_str["help_active_image"]:
                button.config(image=help_image)
            else:
                raise ValueError("Invalid button pressed. Image associated:", str(button.cget("image")))

        def bottom_button_on_click(e, button: tk.Button) -> None:
            button.focus_set()
            if button.cget("image") == images_str["info_active_image"]:
                button.config(
                    image=info_image,
                    activebackground=Color.bottom_button_cbg,
                    activeforeground=Color.bottom_button_cfg
                    )
            elif button.cget("image") == images_str["help_active_image"]:
                button.config(
                    image=help_image,
                    activebackground=Color.bottom_button_cbg,
                    activeforeground=Color.bottom_button_cfg
                    )
            else:
                raise ValueError("Invalid button pressed. Image associated:", str(button.cget("image")))

        def bottom_button_on_release(e, button: tk.Button) -> None:
            if (button.cget("image") == images_str["info_image"]) or (button.cget("image") == images_str["info_active_image"]):
                button.config(
                    image=info_active_image,
                    activebackground=Color.bottom_button_abg,
                    activeforeground=Color.bottom_button_afg
                    )
                if info_frame_state["visible"] == False:
                    button_frame.place_forget()
                    help_frame.place_forget()
                    info_frame.place(x=0, y=title_height, width=self.__window_width, height=INFO_FRAME_HEIGHT)
                    info_frame_state["visible"] = True
                    help_frame_state["visible"] = False
                else:
                    info_frame.place_forget()
                    help_frame.place_forget()
                    button_frame.place(x=0, y=title_height, width=self.__window_width, height=self.__window_height - (title_height + bottom_frame_height))
                    info_frame_state["visible"] = False
                    help_frame_state["visible"] = False

            elif button.cget("image") == images_str["help_image"]:
                button.config(
                    image=help_active_image,
                    activebackground=Color.bottom_button_abg,
                    activeforeground=Color.bottom_button_afg
                    )
                if help_frame_state["visible"] == False:
                    button_frame.place_forget()
                    info_frame.place_forget()
                    help_frame.place(x=0, y=title_height, width=self.__window_width, height=INFO_FRAME_HEIGHT)
                    help_frame_state["visible"] = True
                    info_frame_state["visible"] = False
                else:
                    help_frame.place_forget()
                    info_frame.place_forget()
                    button_frame.place(x=0, y=title_height, width=self.__window_width, height=self.__window_height - (title_height + bottom_frame_height))
                    help_frame_state["visible"] = False
                    info_frame_state["visible"] = False
            
            else:
                raise ValueError("Invalid button pressed. Image associated: ", str(button.cget("image")))


        info_button: tk.Button = tk.Button(
            bottom_frame,
            image=info_image,
            **bottom_button_parameters
            )
        info_button.grid(row=0, column=0, sticky="nsew")
        info_button.bind("<Enter>", lambda event: bottom_button_on_enter(event, info_button))
        info_button.bind("<Leave>", lambda event: bottom_button_on_leave(event, info_button))
        info_button.bind("<Button-1>", lambda event: bottom_button_on_click(event, info_button))
        # info_button.bind("<Return>", lambda event: bottom_button_on_click(event, info_button))
        info_button.bind("<ButtonRelease-1>", lambda event: bottom_button_on_release(event, info_button))
        info_button.bind("<KeyRelease-Return>", lambda event: bottom_button_on_release(event, info_button))
        
        # * The issue was solved and seems to work fine testing only using the keyboard, only the mouse, and both.
        # ! However, further testing should be done to ensure it can work for the other buttons, which will be something to implement in another version.

        help_button: tk.Button = tk.Button(
            bottom_frame,
            image=help_image,
            **bottom_button_parameters
            )
        help_button.grid(row=0, column=1, sticky="nsew")

        help_button.bind("<Enter>", lambda event: bottom_button_on_enter(event, help_button))
        help_button.bind("<Leave>", lambda event: bottom_button_on_leave(event, help_button))
        help_button.bind("<Button-1>",
            lambda event: bottom_button_on_click(event, help_button))
        help_button.bind("<ButtonRelease-1>", lambda event: bottom_button_on_release(event, help_button))

        version_label: tk.Label = tk.Label(
            bottom_frame,
            text=f"V {self.__version}",
            bg=Color.bottom_button_bg,
            fg=Color.bottom_button_fg,
            font=font.Font(family=FontName.label, size=10, weight="bold")
            )
        # * To avoid being deleted by Python's garbage collector
        info_button.image = info_image
        help_button.image = help_image
        version_label.grid(row=0, column=2, sticky="nsew")
        bottom_frame.place(x=0, y=self.__window_height - bottom_frame_height, width=self.__window_width,
                           height=bottom_frame_height)

    # * Setting information frame
        INFO_FRAME_HEIGHT: int = self.__window_height - (title_height + bottom_frame_height)
        help_frame_state:dict = {"visible": False}
        info_frame_state: dict = {"visible": False}
        info_frame: tk.Frame = tk.Frame(self.__root_frame,
                                        height=INFO_FRAME_HEIGHT)
        info_frame.columnconfigure(0, weight=1)
        info_frame.columnconfigure(1, weight=0)
        info_frame.rowconfigure(0, weight=0)
        info_frame.rowconfigure(1, weight=1)

        hide_button_parameters: dict = {
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

        info_hide_button: tk.Button = tk.Button(info_frame,
                                                **hide_button_parameters)

        def hide_button_on_click(e, button: tk.Button) -> None:
            button.focus_set()
            button.config(activebackground=Color.hide_button_cbg,
                activeforeground=Color.hide_button_cfg)

        def hide_button_on_release(e, button: tk.Button) -> None:
            button.config(activebackground=Color.hide_button_abg,
                activeforeground=Color.hide_button_afg)
            if info_frame_state["visible"] == True:
                info_frame.place_forget()
                help_frame.place_forget()
                button_frame.place(x=0, y=title_height, width=self.__window_width, height=self.__window_height - (title_height + bottom_frame_height))
                info_button.focus_set()
            elif help_frame_state["visible"] == True:
                help_frame.place_forget()
                info_frame.place_forget()
                button_frame.place(x=0, y=title_height, width=self.__window_width, height=self.__window_height - (title_height + bottom_frame_height))
                help_button.focus_set()
            info_frame_state["visible"] = False
            help_frame_state["visible"] = False

        info_hide_button.grid(row=0, column=0, columnspan=2, sticky="nsew")
        info_hide_button.bind("<Button-1>", lambda event: hide_button_on_click(event, info_hide_button))
        info_hide_button.bind("<ButtonRelease-1>", lambda event: hide_button_on_release(event, info_hide_button))
        scrollbar_parameters: dict = {
            "bg": Color.info_scrollbar_bg,
            "activebackground": Color.info_scrollbar_abg,
            "troughcolor": Color.info_scrollbar_trough,
            "highlightthickness": 0,
            "borderwidth": 0,
            "elementborderwidth": 0,
            "width": 10,
        }
        info_scrollbar: tk.Scrollbar = tk.Scrollbar(info_frame, **scrollbar_parameters)
        # * For now, the scrollbar will be left as it comes with the
        # * tkinter API. In later versions a migration to tools like
        # * CTtkinter or ttk will be considered.
        text_parameters: dict = {
            "bg": Color.bottom_label_bg,
            "fg": Color.bottom_label_fg,
            "font": font.Font(family=FontName.label, size=10),
            "wrap": "word",
            "padx": 5,
            "pady": 5,  
            "borderwidth": 0,
            "highlightthickness": 0
        }
        info_text: tk.Text = tk.Text(info_frame, **text_parameters)
        info_text.config(state="normal")
        info_text.insert(index="end", chars="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?")
        # ? We could create a function to justify the text
        info_text.tag_config(tagName="center", justify="center")
        info_text.tag_add("center", "1.0", "end")
        info_text.config(state="disabled")
        info_text.config(yscrollcommand=info_scrollbar.set)
        info_scrollbar.config(command=info_text.yview)
        info_text.grid(row=1, column=0)
        info_scrollbar.grid(row=1, column=1, sticky="ns")

    # * Setting the help frame
        help_frame:tk.Frame = tk.Frame(self.__root_frame)
        help_frame.rowconfigure(0, weight=0)
        help_frame.rowconfigure(1, weight=1)
        help_frame.columnconfigure(0, weight=1)
        help_frame.columnconfigure(1, weight=0)

        # ! Check the functionality of the hovering, clicking and releasing of the help_button. Seems to be working fine but there could be problems when entering the help frame from the info frame
        help_hide_button: tk.Button = tk.Button(master=help_frame,
            **hide_button_parameters)
        help_hide_button.bind("<Button-1>", lambda event : hide_button_on_click (event, help_hide_button))
        help_hide_button.bind("<ButtonRelease-1>", lambda event: hide_button_on_release(event, help_hide_button))
        help_hide_button.grid(row=0, column=0, columnspan=2, sticky="nsew")

        help_text: tk.Text = tk.Text(master=help_frame, **text_parameters)
        help_scrollbar: tk.Scrollbar = tk.Scrollbar(help_frame,
            **scrollbar_parameters)
        help_text.config(state="normal")
        help_text.insert(index="end",
            chars="aaaaaaaaaaaaaaaaaaaaaaaaaaaaa lo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam que")
        help_text.config(state="disabled")
        help_text.tag_config(tagName="center", justify="center")
        help_text.tag_add("center", "1.0", "end")
        help_text.config(yscrollcommand=help_scrollbar.set)
        help_scrollbar.config(command=help_text.yview)
        help_text.grid(row=1, column=0, sticky="nsew")
        help_scrollbar.grid(row=1, column=1, sticky="ns")

    # * Setting center (optimization) frame
        OPTIM_BUTTON_PADDING: int = 10
        button_frame: tk.Frame = tk.Frame(self.__root_frame, bg=Color.window_bg)
        button_frame.rowconfigure(0, weight=1)
        button_frame.rowconfigure(1, weight=1)
        button_frame.rowconfigure(2, weight=1)
        button_frame.rowconfigure(3, weight=1)
        button_frame.columnconfigure(0, weight=1)
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
            button_frame.place_forget()
            bottom_frame.place_forget()
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
            button_frame,
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
            button_frame,
            text="Select optimization",
            **optimization_button_parameters
            )
        select_button.bind("<Button-1>",
            lambda event: menu_button_on_click(event, select_button))
        select_button.bind("<ButtonRelease-1>",
            lambda event: menu_button_on_release(self, event, select_button))
        select_button.grid(row=1, column=0, pady=(0,OPTIM_BUTTON_PADDING), padx=4*OPTIM_BUTTON_PADDING, sticky="nsew")
        delete_button: tk.Button = tk.Button(
            button_frame,
            text="Delete optimization",
            **optimization_button_parameters
            )
        delete_button.bind("<Button-1>",
            lambda event: menu_button_on_click(event, delete_button))
        delete_button.bind("<ButtonRelease-1>",
            lambda event: menu_button_on_release(self, event, delete_button))
        delete_button.grid(row=2, column=0, pady=(0,OPTIM_BUTTON_PADDING), padx=4*OPTIM_BUTTON_PADDING, sticky="nsew")
        exit_button: tk.Button = tk.Button(
            button_frame,
            text="Exit",
            **optimization_button_parameters
            )
        exit_button.bind("<Button-1>",
            lambda event: menu_button_on_click(event, exit_button))
        exit_button.bind("<ButtonRelease-1>",
            lambda event: menu_button_on_release(self, event, exit_button))
        exit_button.grid(row=3, column=0, pady=(0,OPTIM_BUTTON_PADDING), padx=4*OPTIM_BUTTON_PADDING, sticky="nsew")
        # ? How do you add multiple suggestions to parameters like sticky does?

        button_frame.place(x=0, y=title_height, width=self.__window_width, height=self.__window_height - (title_height + bottom_frame_height))

    