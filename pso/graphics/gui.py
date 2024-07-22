
# TODO: When select, create and delete menus are implemented, documentation must be added to the gui, fonts and colors modules.

import tkinter as tk

from pso.graphics.colors import Color
from pso.graphics.fonts import Font
import numpy as np
import matplotlib.pyplot as plt
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GUI:
    """
    A class to initialize and display a Graphical User Interface (GUI) to interact visually with the optimization processes and the database. It is designed in a way it should be contained in a Main class to work. Therefore, any object client cannot modify anything apart from the version of the program.

    ## Attributes

    ### Private
    - `root` : tk.Tk
        The main window of the GUI.
    - `version `: str
        The version of the program. Assumed to be given as a string to the class constructor. Default is "Error".
    - `window_height` : int
        The height of the main window.
    - `window_width` : int
        The width of the main window.

    ## Methods
    - `__init__(program_version: str = "Error") -> None`
        Class constructor.
    
    ### Public
    - `display_create_menu() -> None`
        Displays the menu to create a new optimization.
    - `display_delete_menu() -> None`
        Displays the menu to delete an optimization.
    - `display_exit_menu() -> None`
        Displays a goodbye message and exits the program.
    - `display_main_menu() -> None`
        Displays the main menu of the program.
    - `display_select_menu() -> None`
        Displays the menu to select an optimization.
    - `run() -> None`
        Initializes the main window and runs the GUI.
    """
    __root: tk.Tk = tk.Tk()
    def __init__(self, program_version: str = "Error") -> None:
        # * Will probably need to pass as a parameter the __optimizations attribute of Main.
        # * This would be done in order to be able to do the actions stated in the main menu.
        # ? Future versions could include thread management. Could be an interesting way to start learning about parallelism and concurrency.
        self.__version: str = program_version
        self.__window_height: int = 0
        self.__window_width: int = 0

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
        goodby_text: tk.Text = tk.Text(goodbye_frame, bg=Color.goodbye_frame_bg, wrap="word", font=(Font.label, 25), fg=Color.goodbye_text_fg, background=Color.goodbye_text_bg, borderwidth=0, highlightthickness=0)
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
    # * Setting title
        main_title_height: int = 40
        main_title: tk.Label = tk.Label(GUI.__root, text="PSO manager",
            bg=Color.optim_label_bg, font=(Font.title, 15), wraplength=450,
            anchor="center")
        main_title.place(x=0, y=0, width=self.__window_width,
            height=main_title_height)

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
                    button_frame.place_forget()
                    help_frame.place_forget()
                    info_frame.place(x=0, y=main_title_height, width=self.__window_width, height=INFO_FRAME_HEIGHT)
                    info_frame_state["visible"] = True
                    help_frame_state["visible"] = False
                else:
                    info_frame.place_forget()
                    help_frame.place_forget()
                    button_frame.place(x=0, y=main_title_height, width=self.__window_width, height=self.__window_height - (main_title_height + bottom_frame_height))
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
                    help_frame.place(x=0, y=main_title_height, width=self.__window_width, height=INFO_FRAME_HEIGHT)
                    help_frame_state["visible"] = True
                    info_frame_state["visible"] = False
                else:
                    help_frame.place_forget()
                    info_frame.place_forget()
                    button_frame.place(x=0, y=main_title_height, width=self.__window_width, height=self.__window_height - (main_title_height + bottom_frame_height))
                    help_frame_state["visible"] = False
                    info_frame_state["visible"] = False
            
            else:
                raise ValueError("Invalid button pressed.")


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
            "highlightthickness": 0,
            "font": (Font.label, 10, "bold"),
            "relief": "flat",
            "borderwidth": 0,
            "cursor": "hand2",
            "text": "Hide"
            }

        info_hide_button: tk.Button = tk.Button(info_frame,
                                                **hide_button_parameters)

        def hide_button_on_click(e, button: tk.Button) -> None:
            button.config(activebackground=Color.hide_button_cbg,
                activeforeground=Color.hide_button_cfg)

        def hide_button_on_release(e, button: tk.Button) -> None:
            button.config(activebackground=Color.hide_button_abg,
                activeforeground=Color.hide_button_afg)
            if info_frame_state["visible"] == True:
                info_frame.place_forget()
                help_frame.place_forget()
                button_frame.place(x=0, y=main_title_height, width=self.__window_width, height=self.__window_height - (main_title_height + bottom_frame_height))
            elif help_frame_state["visible"] == True:
                help_frame.place_forget()
                info_frame.place_forget()
                button_frame.place(x=0, y=main_title_height, width=self.__window_width, height=self.__window_height - (main_title_height + bottom_frame_height))
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
            "font": (Font.label, 10),
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
            main_title.place_forget()
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

        button_frame.place(x=0, y=main_title_height, width=self.__window_width, height=self.__window_height - (main_title_height + bottom_frame_height))

    def __display_select_menu(self, optimizations_list: list = [[]]) -> None:
        """
        cognitive_coefficient = 2.05, inertia_coefficient=0.7, social_coefficient=2.05, particle_amount=13, dimensions=2, iterations=7, gbest_position=np.array([0, 0])
        """
        def default_optimization() -> None:
            """In case the user doesn't select any optimization, a default one will be displayed.
            """
            work = optimizations_list[0]
            work.append(2.05)
            work.append(0.7)
            work.append(2.05)
            work.append(13)
            work.append(2)
            work.append(7)
            work.append(np.array([0, 0]))
            
            x = np.arange(-5, 5.1, 0.2)
            y = np.arange(-5, 5.1, 0.2)
            X, Y = np.meshgrid(x, y)
            work.append(X**2 + Y**2)
            
            fig = plt.figure(figsize = (12,10))
            ax = plt.axes(projection='3d')
            Z = work[7]
            surf = ax.plot_surface(X, Y, Z, cmap = plt.cm.cividis)

            #graph gbest position
            ax.scatter(work[6][0], work[6][1], 0, c="red", marker="o", label="gbest position")
            
            # Set axes label
            ax.set_xlabel('x', labelpad=20)
            ax.set_ylabel('y', labelpad=20)
            ax.set_zlabel('z', labelpad=20)
            fig.colorbar(surf, shrink=0.5, aspect=8)
            
            frame = ttk.Frame(gui.__root)
            frame.pack(fill=tk.BOTH, expand=1)  
            canvas = FigureCanvasTkAgg(fig, master=frame)
            canvas.draw()

            #Creating a button that shows the 3d graph
            fig_button = tk.Button(GUI.__root, text="Show 3D graph", command=lambda: canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1), font=(Font.button, 10))
            fig_button.place(x=0, y=0, width=100, height=30)
            fig_button.config(bg=Color.optim_button_bg, fg=Color.optim_button_fg, relief="flat", activebackground=Color.optim_button_abg, activeforeground=Color.optim_button_afg, highlightbackground=Color.optim_button_hbg, highlightcolor=Color.optim_button_hbg, highlightthickness=1, borderwidth=1, cursor="hand2")
        
        if optimizations_list == [[]]:
            default_optimization()        

    def __initialize_root(self) -> None:
        GUI.__root.title("Particle Swarm Optimization")

        # * Setting initial geometry (dimensions)
        GUI.__root.resizable(False, False)
        screen_width: int = GUI.__root.winfo_screenwidth()
        screen_height: int= GUI.__root.winfo_screenheight()
        self.__window_width: int = 250
        self.__window_height: int = 250
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
        self.__initialize_root()
        self.__display_main_menu()
        GUI.__root.mainloop()

if __name__ == "__main__":
    gui = GUI("0.2.0") # * Version can be obtained from Main's method get_version(). Therefore, when GUI is created inside Main, the method will be called as an argument (?).
    gui.run() # ? Should run be the only public method?