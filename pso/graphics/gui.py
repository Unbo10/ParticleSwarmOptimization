

import tkinter as tk

from pso.graphics.colors import Color

class GUI:
    def __init__(self) -> None:
        # * Will probably need to pass as a parameter the __optimizations attribute of Main.
        # * This is done in order to be able to do the actions stated in the main menu.
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
        pass

    def select_menu(self) -> None:
        pass

    def delete_menu(self) -> None:
        pass

    def exit_menu(self) -> None:
        self.root.quit()

    def main_on_click (self, event=None, button_type: str="") -> None:
        if button_type == "create":
            pass
        elif button_type == "select":
            self.select_menu()
        elif button_type == "delete":
            self.delete_menu()
        elif button_type == "exit":
            self.exit_menu()
        else:
            raise ValueError("Invalid button type.")

    def main_menu(self):

        # * Setting title
        main_title_height: int = 40
        main_title: tk.Label = tk.Label(self.root, 
                                        text="PSO manager",
                                        bg=Color.label_bg,
                                        font=("Ubuntu", 15),
                                        wraplength=450,
                                        anchor="center")
        main_title.place(x=0, y=0, width=self.__window_width, height=main_title_height)

        # * Setting bottom frame
        bottom_frame_height: int = 30
        bottom_frame: tk.Frame = tk.Frame(self.root, bg=Color.button_abg)
        bottom_frame.place(x=0, y=self.__window_height - bottom_frame_height, width=self.__window_width, height=30)

        # * Common settings for buttons
        BUTTON_WIDTH: int = 10
        BUTTON_PADDING: int = 10
        button_frame: tk.Frame = tk.Frame(self.root, height=self.__window_height - (main_title_height + bottom_frame_height), bg=Color.window_bg)
        button_frame.rowconfigure(0, weight=1)
        button_frame.rowconfigure(1, weight=1)
        button_frame.rowconfigure(2, weight=1)
        button_frame.rowconfigure(3, weight=1)
        button_frame.columnconfigure(0, weight=1)
        button_parameters: dict = {"bg": Color.button_bg, "fg": Color.button_fg, "relief": "flat", "font": ("Ubuntu", 10), "activebackground": Color.button_abg, "activeforeground": Color.button_afg, "highlightbackground": Color.button_hbg, "highlightcolor": Color.button_hbg, "highlightthickness": 1, "borderwidth": 1}
        create_button: tk.Button = tk.Button(button_frame,
                                             text="Create optimization",
                                             **button_parameters)
        create_button.bind("<Button-1>", lambda event: self.main_on_click("create"))
        create_button.grid(row=0, column=0, pady=BUTTON_PADDING, padx=4*BUTTON_PADDING, sticky="nsew")
        select_button: tk.Button = tk.Button(button_frame,
                                             text="Select optimization", 
                                             **button_parameters)
        select_button.bind("<Button-1>", lambda event: self.main_on_click("select"))
        select_button.grid(row=1, column=0, pady=(0,BUTTON_PADDING), padx=4*BUTTON_PADDING, sticky="nsew")
        delete_button: tk.Button = tk.Button(button_frame,
                                             text="Delete optimization", 
                                             **button_parameters)
        delete_button.bind("<Button-1>", lambda event: self.main_on_click("delete"))
        delete_button.grid(row=2, column=0, pady=(0,BUTTON_PADDING), padx=4*BUTTON_PADDING, sticky="nsew")
        exit_button: tk.Button = tk.Button(button_frame,
                                           text="Exit",
                                           **button_parameters)
        exit_button.bind("<Button-1>", lambda event: self.main_on_click(button_type="exit"))
        exit_button.grid(row=3, column=0, pady=(0,BUTTON_PADDING), padx=4*BUTTON_PADDING, sticky="nsew")
        # ? How do you add multiple suggestions to parameters like sticky does?
        button_frame.pack(fill="both", expand=True, pady=(main_title_height, bottom_frame_height))
                                           
        # Todo: Could think of a frame that adds a little menu at the bottom like the one in VsCode. It could contain the authors, info, version, etc. 

if __name__ == "__main__":
    gui = GUI()
    gui.run()