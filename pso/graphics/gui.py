

import tkinter as tk
import toml

from pso.graphics.colors import Color

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

        # * Setting title
        main_title_height: int = 40
        main_title: tk.Label = tk.Label(self.root, 
                                        text="PSO manager",
                                        bg=Color.optim_label_bg,
                                        font=("Ubuntu", 15),
                                        wraplength=450,
                                        anchor="center")
        main_title.place(x=0, y=0, width=self.__window_width, height=main_title_height)

        # * Setting bottom frame
        bottom_frame_height: int = 30
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
            "borderwidth": 0
            }
        # TODO: Consider loading the active image with a darker color over a lighter background
        info_image: tk.PhotoImage = tk.PhotoImage(file="assets/info.png").subsample(3)
        info_active_image: tk.PhotoImage = tk.PhotoImage(file="assets/info-active.png").subsample(3)
        info_button: tk.Button = tk.Button(
            bottom_frame,
            image=info_image,
            **bottom_button_parameters
            )
        info_button.grid(row=0, column=0, sticky="nsew")
        
        def info_on_enter(e) -> None:
            info_button.config(image=info_active_image)

        def info_on_leave(e) -> None:
            info_button.config(image=info_image)
        
        def info_on_click(e) -> None:
            pass

        info_button.bind("<Enter>", info_on_enter)
        info_button.bind("<Leave>", info_on_leave)
        info_button.bind("<Button-1>", info_on_click)
        help_image: tk.PhotoImage = tk.PhotoImage(file="assets/help.png").subsample(3)
        help_active_image: tk.PhotoImage = tk.PhotoImage(file="assets/help-active.png").subsample(3)
        help_button: tk.Button = tk.Button(
            bottom_frame,
            image=help_image,
            **bottom_button_parameters
            )
        help_button.grid(row=0, column=1, sticky="nsew")
        
        def help_on_enter(e) -> None:
            help_button.config(image=help_active_image)

        def help_on_leave(e) -> None:
            help_button.config(image=help_image)

        def help_on_click(e) -> None:
            pass

        help_button.bind("<Enter>", help_on_enter)
        help_button.bind("<Leave>", help_on_leave)
        help_button.bind("<Button-1>", help_on_click)

        # ! NEXT STEP
        # TODO: Configure the on click functions for each of the two buttons. They could display another window (might be the easiest to do) or a frame that contains the information, although a quit button would be needed.
        version_label: tk.Label = tk.Label(
            bottom_frame,
            text=f"V {self.__version}",
            bg=Color.bottom_button_bg,
            fg=Color.bottom_button_fg,
            font=("Ubuntu", 10, "bold")
            )
        # * To avoid being deleted by Python's garbage collector
        info_button.image = info_image
        help_button.image = help_image
        version_label.grid(row=0, column=2, sticky="nsew")
        bottom_frame.place(x=0, y=self.__window_height - bottom_frame_height, width=self.__window_width, height=30)

        # * Setting center (optimization) frame
        BUTTON_WIDTH: int = 10
        BUTTON_PADDING: int = 10
        button_frame: tk.Frame = tk.Frame(self.root, height=self.__window_height - (main_title_height + bottom_frame_height), bg=Color.window_bg)
        button_frame.rowconfigure(0, weight=1)
        button_frame.rowconfigure(1, weight=1)
        button_frame.rowconfigure(2, weight=1)
        button_frame.rowconfigure(3, weight=1)
        button_frame.columnconfigure(0, weight=1)
        optimization_button_parameters: dict = {
            "bg": Color.optim_button_bg,
            "fg": Color.optim_button_fg,
            "relief": "flat",
            "font": ("Ubuntu", 10),
            "activebackground": Color.optim_button_abg,
            "activeforeground": Color.optim_button_afg,
            "highlightbackground": Color.optim_button_hbg,
            "highlightcolor": Color.optim_button_hbg,
            "highlightthickness": 1,
            "borderwidth": 1
            }
        
        def menu_button_clicked(e, button: tk.Button) -> None:
            button.config(activebackground=Color.optim_button_cbg, activeforeground=Color.optim_button_cfg)

        def menu_button_released(self, e, button: tk.Button) -> None:
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
            lambda event: menu_button_clicked(event, create_button))
        create_button.bind("<ButtonRelease-1>",
            lambda event: menu_button_released(self, event, create_button))
        create_button.grid(row=0, column=0, pady=BUTTON_PADDING,
            padx=4*BUTTON_PADDING, sticky="nsew")
        select_button: tk.Button = tk.Button(
            button_frame,
            text="Select optimization", 
            **optimization_button_parameters
            )
        select_button.bind("<Button-1>",
            lambda event: menu_button_clicked(event, select_button))
        select_button.bind("<ButtonRelease-1>",
            lambda event: menu_button_released(self, event, select_button))
        select_button.grid(row=1, column=0, pady=(0,BUTTON_PADDING), padx=4*BUTTON_PADDING, sticky="nsew")
        delete_button: tk.Button = tk.Button(
            button_frame,
            text="Delete optimization", 
            **optimization_button_parameters
            )
        delete_button.bind("<Button-1>",
            lambda event: menu_button_clicked(event, delete_button))
        delete_button.bind("<ButtonRelease-1>",
            lambda event: menu_button_released(self, event, delete_button))
        delete_button.grid(row=2, column=0, pady=(0,BUTTON_PADDING), padx=4*BUTTON_PADDING, sticky="nsew")
        exit_button: tk.Button = tk.Button(
            button_frame,
            text="Exit",
            **optimization_button_parameters
            )
        exit_button.bind("<Button-1>",
            lambda event: menu_button_clicked(event, exit_button))
        exit_button.bind("<ButtonRelease-1>",
            lambda event: menu_button_released(self, event, exit_button))
        exit_button.grid(row=3, column=0, pady=(0,BUTTON_PADDING), padx=4*BUTTON_PADDING, sticky="nsew")
        # ? How do you add multiple suggestions to parameters like sticky does?
        button_frame.pack(fill="both", expand=True, pady=(main_title_height, bottom_frame_height))
                                           
        # Todo: Could think of a frame that adds a little menu at the bottom like the one in VsCode. It could contain the authors, info, version, etc. 

if __name__ == "__main__":
    gui = GUI("0.2.0") # * Version can be obtained from Main's method get_version(). Therefore, when GUI is created inside Main, the method will be called as an argument (?).
    gui.run()