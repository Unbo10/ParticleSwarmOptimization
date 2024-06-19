

import tkinter as tk
import toml

from pso.graphics.colors import Color
from pso.graphics.fonts import Font

class GUI:
    def __init__(self, program_version: str = "Error") -> None:
        # * Will probably need to pass as a parameter the __optimizations attribute of Main.
        # * This is done in order to be able to do the actions stated in the main menu.
        self.__version: str = program_version
        self.root: tk.Tk = tk.Tk()
        self.__window_height: int = 0
        self.__window_width: int = 0

    def __initialize_root(self) -> None:
        self.root.title("Particle Swarm Optimization")

        # * Setting initial geometry (dimensions)
        self.root.resizable(False, False)
        screen_width: int = self.root.winfo_screenwidth()
        screen_height: int= self.root.winfo_screenheight()
        self.__window_width: int = 250
        self.__window_height: int = 250
        top_left_x: int = (screen_width // 2) - (self.__window_width // 2)
        top_left_y: int = (screen_height // 2) - (self.__window_height // 2)
        self.root.geometry(f"{self.__window_width}x{self.__window_height}+{top_left_x}+{top_left_y}")

        # * Setting icon for the application switcher, the dock and the taskbar (Windows)
        small_logo_path: str = "assets/small-logo.png"
        large_logo_path: str = small_logo_path
        small_logo: tk.PhotoImage = tk.PhotoImage(file=small_logo_path).subsample(10)
        large_logo: tk.PhotoImage = tk.PhotoImage(file=large_logo_path)
        self.root.iconphoto(False, small_logo, large_logo)

        # * Setting background color
        self.root.configure(bg=Color.window_bg)

    def run(self):
        self.__initialize_root()
        self.main_menu()
        self.root.mainloop()

    def create_menu(self) -> None:
        print("c")

    def select_menu(self) -> None:
        print("s")

    def delete_menu(self) -> None:
        print("d")

    def exit_menu(self) -> None:
        self.root.quit()

    def help_on_click (cls, e) -> None:
        pass

    def info_on_click (cls, e) -> None:
        pass

    def main_menu(self):
        # TODO: Style the hide button depending on the event triggered.

        # * Setting title
        main_title_height: int = 40
        main_title: tk.Label = tk.Label(self.root,
                                        text="PSO manager",
                                        bg=Color.optim_label_bg,
                                        font=(Font.title, 15),
                                        wraplength=450,
                                        anchor="center")
        main_title.place(x=0, y=0, width=self.__window_width, height=main_title_height)

        bottom_frame_height: int = 30

        # * Setting bottom frame
        bottom_frame: tk.Frame = tk.Frame(
            self.root,
            bg=Color.bottom_button_abg
            )
        bottom_frame.rowconfigure(0, weight=1)
        bottom_frame.columnconfigure(0, weight=1)
        bottom_frame.columnconfigure(1, weight=1)
        bottom_frame.columnconfigure(2, weight=1)

        bottom_button_parameters: dict = {
            "bg": Color.bottom_button_bg,
            "relief": "flat",
            "activebackground": Color.bottom_button_abg,
            "highlightbackground": Color.bottom_button_hbg,
            "highlightcolor": Color.bottom_button_hbg,
            "highlightthickness": 0,
            "borderwidth": 0,
            "cursor": "hand2"
            }
        # TODO: Consider loading the active image with a darker color over a lighter background

        info_image: tk.PhotoImage = tk.PhotoImage(file="assets/info.png").subsample(3)
        info_active_image: tk.PhotoImage = tk.PhotoImage(file="assets/info-active.png").subsample(3)
        help_image: tk.PhotoImage = tk.PhotoImage(file="assets/help.png").subsample(3)
        help_active_image: tk.PhotoImage = tk.PhotoImage(file="assets/help-active.png").subsample(3)
        images_str: dict = {
                "info_image": "pyimage5",
                "info_active_image": "pyimage7",
                "help_image": "pyimage9",
                "help_active_image": "pyimage11"
            }

        def bottom_button_on_enter(e, button:tk.Button) -> None:
            if button.cget("image") == images_str["info_image"]:
                button.config(image=info_active_image)
            else:
                button.config(image=help_active_image)

        def bottom_button_on_leave(e, button:tk.Button) -> None:
            if button.cget("image") == images_str["info_active_image"]:
                button.config(image=info_image)
            else:
                button.config(image=help_image)

        def bottom_button_on_click(e, button: tk.Button) -> None:
            if button.cget("image") == images_str["info_active_image"]:
                button.config(
                    image=info_image,
                    activebackground=Color.bottom_button_cbg,
                    activeforeground=Color.bottom_button_cfg
                    )
            else:
                button.config(
                    image=help_image,
                    activebackground=Color.bottom_button_cbg,
                    activeforeground=Color.bottom_button_cfg
                    )

        def bottom_button_on_release(e, button: tk.Button) -> None:
            if button.cget("image") == images_str["info_image"]:
                button.config(
                    image=info_active_image,
                    activebackground=Color.bottom_button_abg,
                    activeforeground=Color.bottom_button_afg
                    )
                if info_frame_state["visible"] == False:
                    info_frame.place(x=0, y=main_title_height, width=self.__window_width, height=INFO_FRAME_HEIGHT)
                    button_frame.pack_forget()
                    info_frame_state["visible"] = True
                else:
                    info_frame.pack_forget()
                    button_frame.pack(fill="both", expand=True, pady=(main_title_height, bottom_frame_height))
                    info_frame_state["visible"] = False
            else:
                button.config(
                    image=help_active_image,
                    activebackground=Color.bottom_button_abg,
                    activeforeground=Color.bottom_button_afg
                    )


        info_button: tk.Button = tk.Button(
            bottom_frame,
            image=info_image,
            **bottom_button_parameters
            )
        info_button.grid(row=0, column=0, sticky="nsew")
        info_button.bind("<Enter>", lambda event: bottom_button_on_enter(event, info_button))
        info_button.bind("<Leave>", lambda event: bottom_button_on_leave(event, info_button))
        info_button.bind("<Button-1>", lambda event: bottom_button_on_click(event, info_button))
        info_button.bind("<ButtonRelease-1>", lambda event: bottom_button_on_release(event, info_button))

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
            font=(Font.label, 10, "bold")
            )
        # * To avoid being deleted by Python's garbage collector
        info_button.image = info_image
        help_button.image = help_image
        version_label.grid(row=0, column=2, sticky="nsew")
        bottom_frame.place(x=0, y=self.__window_height - bottom_frame_height, width=self.__window_width,
                           height=bottom_frame_height)

        # * Setting information frame
        INFO_FRAME_HEIGHT: int = self.__window_height - (main_title_height + bottom_frame_height)
        HIDING_BUTTON_PADDING: int = 10
        info_frame_state: dict = {"visible": False}
        info_frame: tk.Frame = tk.Frame(self.root,
                                        height=INFO_FRAME_HEIGHT)
        info_frame.columnconfigure(0, weight=1)
        info_frame.columnconfigure(1, weight=0)
        info_frame.rowconfigure(0, weight=0)
        info_frame.rowconfigure(1, weight=1)

        hide_button_parameters: dict = {
            "bg": Color.hide_button_bg,
            "fg": Color.hide_button_fg,
            "activebackground": Color.hide_button_abg,
            "highlightbackground": Color.hide_button_hbg,
            "highlightcolor": Color.hide_button_hbg,
            "highlightthickness": 0,
            "font": (Font.label, 10, "bold"),
            "relief": "flat",
            "borderwidth": 0,
            "cursor": "hand2"
            }

        hide_button: tk.Button = tk.Button(info_frame,
                                                text="Hide",
                                                **hide_button_parameters)

        def hide_button_on_enter(e) -> None:
            hide_button.config(activebackground=Color.hide_button_abg,
                activeforeground=Color.hide_button_afg)

        def hide_button_on_leave(e) -> None:
            hide_button.config(activebackground=Color.hide_button_abg,
                activeforeground=Color.hide_button_afg)

        def hide_button_on_click(e) -> None:
            hide_button.config(activebackground=Color.hide_button_cbg,
                activeforeground=Color.hide_button_cfg)

        def hide_button_on_release(e) -> None:
            hide_button.config(activebackground=Color.hide_button_abg,
                activeforeground=Color.hide_button_afg)
            info_frame_state["visible"] = False
            info_frame.pack_forget()
            button_frame.pack(fill="both", expand=True, pady=(main_title_height, bottom_frame_height))

        hide_button.grid(row=0, column=0, columnspan=2, sticky="nsew")
        hide_button.bind("<Enter>", hide_button_on_enter)
        hide_button.bind("<Leave>", hide_button_on_leave)
        hide_button.bind("<Button-1>", hide_button_on_click)
        hide_button.bind("<ButtonRelease-1>", hide_button_on_release)
        info_scrollbar_parameters: dict = {
            "bg": Color.info_scrollbar_bg,
            "activebackground": Color.info_scrollbar_abg,
            "troughcolor": Color.info_scrollbar_trough,
            "highlightthickness": 0,
            "borderwidth": 0,
            "elementborderwidth": 0,
            "width": 10,
        }
        info_scrollbar: tk.Scrollbar = tk.Scrollbar(info_frame, **info_scrollbar_parameters)
        # * For now, the scrollbar will be left as it comes with the
        # * tkinter API. In later versions a migration to tools like
        # * CTtkinter or ttk will be considered.
        info_text_parameters: dict = {
            "bg": Color.info_label_bg,
            "font": (Font.label, 10),
            "wrap": "word",
            "padx": 5,
            "pady": 5,  
            "borderwidth": 0,
            "highlightthickness": 0
        }
        info_text: tk.Text = tk.Text(info_frame, **info_text_parameters)
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
        help_frame_state:dict = {"visible": False}
        help_frame:tk.Frame = tk.Frame(self.root, height=INFO_FRAME_HEIGHT,
            bg=Color.help_frame_bg) # ! bg might not be necessary
        help_frame.rowconfigure(0, weight=0)

        # * Setting center (optimization) frame
        OPTIM_BUTTON_PADDING: int = 10
        button_frame: tk.Frame = tk.Frame(self.root,height=self.__window_height - (main_title_height + bottom_frame_height), bg=Color.window_bg)
        button_frame.rowconfigure(0, weight=1)
        button_frame.rowconfigure(1, weight=1)
        button_frame.rowconfigure(2, weight=1)
        button_frame.rowconfigure(3, weight=1)
        button_frame.columnconfigure(0, weight=1)
        optimization_button_parameters: dict = {
            "bg": Color.optim_button_bg,
            "fg": Color.optim_button_fg,
            "relief": "flat",
            "font": (Font.button, 10),
            "activebackground": Color.optim_button_abg,
            "activeforeground": Color.optim_button_afg,
            "highlightbackground": Color.optim_button_hbg,
            "highlightcolor": Color.optim_button_hbg,
            "highlightthickness": 1,
            "borderwidth": 1,
            "cursor": "hand2"
            }

        def menu_button_on_click(e, button: tk.Button) -> None:
            button.config(activebackground=Color.optim_button_cbg, activeforeground=Color.optim_button_cfg)

        def menu_button_on_release(self, e, button: tk.Button) -> None:
            button.config(activebackground=Color.optim_button_abg, activeforeground=Color.optim_button_afg)
            button_text: str = button.cget("text")
            if button_text == "Create optimization":
                self.create_menu()
            elif button_text == "Select optimization":
                self.select_menu()
            elif button_text == "Delete optimization":
                self.delete_menu()
            elif button_text == "Exit":
                self.exit_menu()
            else:
                raise ValueError("Invalid button pressed.")

        create_button: tk.Button = tk.Button(
            button_frame,
            text="Create optimization",
            **optimization_button_parameters
            )
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

        # * Packing frames
        button_frame.pack(fill="both", expand=True, pady=(main_title_height, bottom_frame_height))


if __name__ == "__main__":
    gui = GUI("0.2.0") # * Version can be obtained from Main's method get_version(). Therefore, when GUI is created inside Main, the method will be called as an argument (?).
    gui.run()