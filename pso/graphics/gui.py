
# TODO: When select, create and delete menus are implemented, documentation must be added to the gui, fonts and colors modules.

import os

import numpy as np
import tkinter as tk
from tkinter import font

from pso.graphics.colors import Color
from pso.graphics.exitMenu import ExitMenu
from pso.graphics.mainMenu import MainMenu
from pso.graphics.selectMenu import SelectMenu
from pso.graphics.fonts import FontName
from pso.optimization import Optimization

class GUI:
    __root: tk.Tk = tk.Tk()
    def __init__(self, optimization_history: list[Optimization], program_version: str = "Error") -> None:
        # * Will probably need to pass as a parameter the __optimizations attribute of Main.
        # * This would be done in order to be able to do the actions stated in the main menu.
        # ? Future versions could include thread management. Could be an interesting way to start learning about parallelism and concurrency.
        self._root_frame: tk.Frame = tk.Frame(GUI.__root, bg=Color.test2_bg)
        self.__exit_menu: ExitMenu = ExitMenu(self._root_frame, self._initialize_root)
        self.__main_menu: MainMenu = MainMenu(self._root_frame, self._initialize_root)
        self.__select_menu: SelectMenu = SelectMenu(self._root_frame)
        self.__menus: dict = {"exit": self.__exit_menu, "main": self.__main_menu, "select": self.__select_menu}
        self.__optimization_history: list[Optimization] = optimization_history
        self.__version: str = program_version
        self._window_height: int = 0
        self._window_width: int = 0

    def change_menu(self, menu_name="") -> None:
        if menu_name in self.__menus:
            for menu in self.__menus.values():
                menu.root.forget()
            self.__menus[menu_name].display()
            self.__menus[menu_name].root.tkraise()
            # ! Don't forget to implement GUI.__root.after(1000, GUI.__root.quit()) at some point in the code.

            # if menu_name == "exit":
            #     print("a")
        else:
            raise Exception(f"Menu {menu_name} not found.")

    def __display_create_menu(self) -> None:
        print("c")

    def __display_delete_menu(self) -> None:
        print("d")

    def __display_exit_menu(self) -> None:
        goodbye_frame: tk.Frame = tk.Frame(GUI.__root,
            bg=Color.goodbye_frame_bg)
        goodbye_frame.rowconfigure(0, weight=0)
        goodbye_frame.rowconfigure(1, weight=1)
        goodbye_frame.columnconfigure(0, weight=1)
        goodbye_image: tk.PhotoImage = tk.PhotoImage(
            file="assets/goodbye.png").subsample(2)
        goodbye_label: tk.Label = tk.Label(goodbye_frame, image=goodbye_image, bg=Color.goodbye_label_bg, borderwidth=0, highlightthickness=0) 
        goodby_text: tk.Text = tk.Text(goodbye_frame, bg=Color.goodbye_frame_bg, wrap="word", font=font.Font(family=FontName.label, size=25), fg=Color.goodbye_text_fg, background=Color.goodbye_text_bg, borderwidth=0, highlightthickness=0)
        goodby_text.insert(index="end", chars="Goodbye!")
        goodby_text.tag_config(tagName="center", justify="center")
        goodby_text.tag_add("center", "1.0", "end")
        goodby_text.config(state="disabled")
        goodbye_label.grid(row=0, column=0, pady=(25, 0), sticky="nsew")
        goodby_text.grid(row=1, column=0, pady=(25, 25), sticky="nsew")
        # ? A more rigurous way of centering the label and the text could be implemented.
        goodbye_label.image = goodbye_image
        goodbye_frame.place(x=0, y=0, width=self.__window_width, height=self.__window_height)
    
    def __display_main_menu(self):
        """
        """
        self.__initialize_root(width=250, height=250)
    # * Setting title
        title_height: int = 40
        title: tk.Label = tk.Label(GUI.__root, text="PSO manager",
            bg=Color.optim_label_bg, font=font.Font(family=FontName.title, size=15), wraplength=450,
            anchor="center")
        title.place(x=0, y=0, width=self.__window_width,
            height=title_height)

        bottom_frame_height: int = 30

    # ! In future versions the bottom, help and info frames could be instance attributes to allow object clients to modify them to their requirements.
    # * Setting bottom frame
        bottom_frame: tk.Frame = tk.Frame( GUI.__root,
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
        info_frame: tk.Frame = tk.Frame(GUI.__root,
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
        help_frame:tk.Frame = tk.Frame(GUI.__root)
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
        button_frame: tk.Frame = tk.Frame(GUI.__root, bg=Color.window_bg)
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
                GUI.__root.after(1000, GUI.__root.quit)
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

    def __display_select_menu(self) -> None:
        self.__initialize_root(width=750, height=500, title="Select optimization - PSO")
        title_height: int = 2 # * Text units, not pixels. It doesn't correspond exactly to the size of the font. Default is 17, Ubuntu size 15 is 15 + 9 = 24 px.
        title: tk.Label = tk.Label(GUI.__root, text="Select a previous optimization", height=title_height, bg=Color.select_title_bg, fg=Color.select_title_fg, font=font.Font(family=FontName.title, size=15))
        title.pack(fill="x", anchor="e")
        print(font.Font(family=FontName.title, size=15).metrics("linespace"))

        arrow_back_path: str = "assets/arrow-back.png"
        arrow_back_image: tk.PhotoImage = tk.PhotoImage(file=arrow_back_path).subsample(4)
        arrow_back_path_active: str = "assets/arrow-back-active.png"
        arrow_back_image_active: tk.PhotoImage = tk.PhotoImage(file=arrow_back_path_active).subsample(4)
        back_button: tk.Button = tk.Button(GUI.__root, image=arrow_back_image, relief="flat", cursor="hand2", bg=Color.back_button_bg, activebackground=Color.back_button_abg, highlightthickness=0, borderwidth=0)

        def back_button_on_enter(e, button: tk.Button) -> None:
            button.config(image=arrow_back_image_active, bg=Color.back_button_abg)

        def back_button_on_leave(e, button: tk.Button) -> None:
            button.config(image=arrow_back_image, bg=Color.back_button_bg)
        
        def back_button_on_click(e, button: tk.Button) -> None:
            button.config(activebackground=Color.back_button_cbg, activeforeground=Color.back_button_cfg, image=arrow_back_image_active)

        # ! CONCERN: The names for button events are named differently in Windows and Linux. Needs to be tested and corrected if necessary (I am sure the enter event is different in Windows).

        back_button.place(x=0, y=0, height=title_height * 25, width=title_height * 25)
        back_button.bind("<Enter>", lambda event: back_button_on_enter(event, back_button))
        back_button.bind("<Leave>", lambda event: back_button_on_leave(event, back_button))
        back_button.bind("<Button-1>", lambda event: back_button_on_click(event, back_button))
        back_button.bind("<ButtonRelease-1>", lambda event: back_button_on_release(event, back_button))
        # * To avoid being deleted by Python's garbage collector
        back_button.image = arrow_back_image
        back_button.active_image = arrow_back_image_active

        if len(self.__optimization_history) == 0:
            print("len 0")
            no_optimizations_label: tk.Label = tk.Label(GUI.__root, height=2, text="No optimizations have been made yet.", bg=Color.select_label_no_optim_bg, fg=Color.select_label_no_optim_fg, font=font.Font(family=FontName.label, size=12))
            no_optimizations_label.pack(fill="both", anchor="center", pady=(20, 0), padx=self.__window_width//2 - 250)
            create_optimization: tk.Button = tk.Button(GUI.__root, text="Create optimization", height=3, bg=Color.optim_button_bg, fg=Color.optim_button_fg, font=font.Font(family=FontName.button, size=15), relief="flat", cursor="hand2", activebackground=Color.optim_button_abg, activeforeground=Color.optim_button_afg, highlightbackground= Color.optim_button_hbg, highlightcolor=Color.optim_button_hcolor, highlightthickness=1)
            create_optimization.pack(fill="x", anchor="center", padx=self.__window_width//2 - 250) # * Could be improved with inheritance

        else: 
            list_scrollbar_width: int = 20
            title_height *= 25 # * Compensating for difference between pixels and text units
            list_canvas: tk.Canvas = tk.Canvas(GUI.__root, bg=Color.test1_bg)
            list_canvas.place(y=(title_height) + 15, x=15, width=self.__window_width - (30 + list_scrollbar_width), height=self.__window_height - (title_height + 30))

            list_scrollbar: tk.Scrollbar = tk.Scrollbar(GUI.__root, orient="vertical", command=list_canvas.yview)
            list_scrollbar.place(x=self.__window_width - (15 + list_scrollbar_width), y=title_height + 15, height=self.__window_height - (title_height + 30), width=list_scrollbar_width)
            list_canvas.configure(yscrollcommand=list_scrollbar.set)

            list_parent_frame_height: int = self.__window_height - (title_height + 30)
            list_parent_frame_width: int = self.__window_width - (30 + list_scrollbar_width)
            list_parent_frame: tk.Frame = tk.Frame(list_canvas, bg=Color.test2_bg)

            inner_frame_height: int = 75
            inner_frame_separation: int = 20
            inner_frame_width: int = self.__window_width - (list_scrollbar_width + 60)

            def create_inner_frame(optimization: Optimization) -> tk.Frame:
                """
                This function initializes a frame for a single optimization.
                It adds multiple labels, buttons and images that correspond to
                the optimization in question. Finally, it returns them to be
                stored somewhere else and displayed.
                """
                inner_frame = tk.Frame(list_parent_frame, width=inner_frame_width, height=inner_frame_height)
                for col in range(5):
                    inner_frame.columnconfigure(col, weight=1)
                inner_frame.rowconfigure(0, weight=1)
                inner_frame.rowconfigure(1, weight=1)
                inner_frame.rowconfigure(2, weight=1)
                name_label: tk.Label = tk.Label(inner_frame, text=f"Optimization {optimization.get_index() + 1}", bg=Color.select_label_optim_bg, fg=Color.select_label_optim_fg, font=font.Font(family=FontName.label, size=12, weight="bold"))
                name_label.grid(row=0, column=0, sticky="nsew")
                function_label: tk.Label = tk.Label(inner_frame, text=f"Function: TO BE DECIDED", bg=Color.select_label_optim_bg, fg=Color.select_label_optim_fg, font=font.Font(family=FontName.label, size=10)) # ! Needs to be changed to the actual function
                function_label.grid(row=1, column=0, sticky="nsew")
                dimensions_label: tk.Label = tk.Label(inner_frame, text=f"Dimensions: {optimization.get_dimensions()}", bg=Color.select_label_optim_bg, fg=Color.select_label_optim_fg, font=font.Font(family=FontName.label, size=10))
                dimensions_label.grid(row=2, column=0, sticky="nsew")
                minima_indicator_label: tk.Label = tk.Label(inner_frame, text=f"Minima:", bg=Color.select_label_optim_bg, fg=Color.select_label_optim_fg, font=font.Font(family=FontName.label, size=10))
                minima_indicator_label.grid(row=0, column=1, sticky="nsew")
                minima_coordinates: np.ndarray = optimization.get_swarm().get_gbest().get_coordinates()
                minima_coordinates = np.round(minima_coordinates, 3)
                minima_value_label: tk.Label = tk.Label(inner_frame, text=f"{minima_coordinates}", bg=Color.select_label_optim_bg, fg=Color.select_label_optim_fg, font=font.Font(family=FontName.label, size=10))
                minima_value_label.grid(row=0, column=2, sticky="nsew")
                cognitive_coefficient_label:tk.Label = tk.Label(inner_frame, text=f"c1: {optimization.get_cognitive_coefficient()}", bg=Color.select_label_optim_bg, fg=Color.select_label_optim_fg, font=font.Font(family=FontName.label, size=10))
                cognitive_coefficient_label.grid(row=1, column=1, sticky="nsew")
                number_of_particles_label: tk.Label = tk.Label(inner_frame, text=f"Number of particles: {optimization.get_particle_amount()}", bg=Color.select_label_optim_bg, fg=Color.select_label_optim_fg, font=font.Font(family=FontName.label, size=10))
                number_of_particles_label.grid(row=2, column=1, sticky="nsew")
                social_coefficient_label: tk.Label = tk.Label(inner_frame, text=f"c2: {optimization.get_social_coefficient()}", bg=Color.select_label_optim_bg, fg=Color.select_label_optim_fg, font=font.Font(family=FontName.label, size=10))
                social_coefficient_label.grid(row=1, column=2, sticky="nsew")
                inertia_coefficient_label: tk.Label = tk.Label(inner_frame, text=f"Inertia: {optimization.get_inertia_coefficient()}", bg=Color.select_label_optim_bg, fg=Color.select_label_optim_fg, font=font.Font(family=FontName.label, size=10))
                inertia_coefficient_label.grid(row=1, column=3, sticky="nsew")
                iterations_label: tk.Label = tk.Label(inner_frame, text=f"Iterations: {optimization.get_iterations()}", bg=Color.select_label_optim_bg, fg=Color.select_label_optim_fg, font=font.Font(family=FontName.label, size=10))
                iterations_label.grid(row=2, column=3, sticky="nsew")

                # ? To the right of the minima label we could add a status label that shows if the optimization was completed or not (if incomplete optimizations were to be stored).

                return inner_frame

            list_inner_frames: list[tk.Frame] = [create_inner_frame(optimization) for optimization in self.__optimization_history]
            list_parent_frame.columnconfigure(0, weight=0)
            frame_index = 0
            while frame_index < len(self.__optimization_history):
                # * This cycle adds all of the inner (optimization) frames to the
                # * parent frame contained inside the canvas.
                list_parent_frame.rowconfigure(frame_index, weight=2)
                list_inner_frames[frame_index].place(x=(list_parent_frame_width - inner_frame_width)/2, y=frame_index*(inner_frame_height + inner_frame_separation) + inner_frame_separation, width=inner_frame_width, height=inner_frame_height)
                frame_index += 1
            if len(self.__optimization_history) > 4:
                list_parent_frame_height = len(self.__optimization_history)*(inner_frame_height + inner_frame_separation) + inner_frame_separation

            list_canvas.create_window((0, 0), window=list_parent_frame, anchor="nw", width=list_parent_frame_width, height=list_parent_frame_height)
            list_canvas.configure(scrollregion=list_canvas.bbox("all"))

            def on_mouse_wheel(event):
                if os.name == "nt":
                    list_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
                elif os.name == "posix":
                    if event.num == 4:
                        list_canvas.yview_scroll(-1, "units")
                    elif event.num == 5:
                        list_canvas.yview_scroll(1, "units")

            inner_frames_children: list = []
            for frame in list_inner_frames:
                inner_frames_children += frame.winfo_children()
            canvas_children = list_canvas.winfo_children() + list_inner_frames + inner_frames_children
            for child in canvas_children:
                child.bind("<MouseWheel>", on_mouse_wheel)
                child.bind("<Button-4>", on_mouse_wheel)
                child.bind("<Button-5>", on_mouse_wheel)
            # ! Now the problem is that the scrollbar is scrolling at a different rate than when the mouse is over the canvas. It is not that big of a problem though, but should be fixed (same happens in the info and help frames).
        
        def back_button_on_release(e, button: tk.Button) -> None:
            back_button.place_forget()
            title.pack_forget()
            if len(self.__optimization_history) != 0:
                list_canvas.place_forget()
            else:
                no_optimizations_label.pack_forget()
                create_optimization.pack_forget()
            self.__display_main_menu()

    def _initialize_root(self, width: int, height: int,
        title: str = "Particle Swarm Optimization (PSO)") -> None:
        GUI.__root.title(title)

        # * Setting initial geometry (dimensions)
        GUI.__root.resizable(False, False)
        screen_width: int = GUI.__root.winfo_screenwidth()
        screen_height: int= GUI.__root.winfo_screenheight()
        self.__window_width: int = width
        self.__window_height: int = height
        top_left_x: int = (screen_width // 2) - (self.__window_width // 2)
        top_left_y: int = (screen_height // 2) - (self.__window_height // 2)
        GUI.__root.geometry(f"{self.__window_width}x{self.__window_height}+{top_left_x}+{top_left_y}")

        # * Setting icon for the application switcher, the dock and the taskbar (Windows)
        small_logo_path: str = "assets/small-logo.png"
        large_logo_path: str = small_logo_path
        small_logo: tk.PhotoImage = tk.PhotoImage(file=small_logo_path).subsample(10)
        large_logo: tk.PhotoImage = tk.PhotoImage(file=large_logo_path)
        GUI.__root.iconphoto(False, small_logo, large_logo)

        # * Setting background color
        GUI.__root.configure(bg=Color.window_bg)

    def run(self):
        self._root_frame.place(x=0, y=0, width=250, height=250)
        self.change_menu("main")
        GUI.__root.mainloop()

if __name__ == "__main__":
    gui = GUI("0.2.0") # * Version can be obtained from Main's method get_version(). Therefore, when GUI is created inside Main, the method will be called as an argument (?).
    gui.run() # ? Should run be the only public method?