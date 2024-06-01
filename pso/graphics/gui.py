

import tkinter as tk

class GUI:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.__window_bg = "#f0f0f0"
    
    def __initialize_root(self) -> None:
        self.root.title("Particle Swarm Optimization")

        # * Setting initial geometry (dimensions)
        self.root.resizable(False, False)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        WINDOW_WIDTH = 500
        WINDOW_HEIGHT = 500
        top_left_x = (screen_width // 2) - (WINDOW_WIDTH // 2)
        top_left_y = (screen_height // 2) - (WINDOW_HEIGHT // 2)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{top_left_x}+{top_left_y}")

        # * Setting icon for the application switcher and the dock (Ubuntu)
        small_logo_path = "assets/small-logo.png"
        large_logo_path = small_logo_path
        small_logo = tk.PhotoImage(file=small_logo_path).subsample(10)
        large_logo = tk.PhotoImage(file=large_logo_path)
        self.root.iconphoto(False, small_logo, large_logo)

        # * Setting background color
        # self.root.configure(bg=self.__window_bg)

    def run(self):
        self.__initialize_root()
        self.main_menu()
        self.root.mainloop()

    def main_menu(self):
        main_title = tk.Label(self.root, text="Welcome to the Particle Swarm Optimization program!", font=("Ubuntu", 15), wraplength=450)
        main_title.pack(pady=10, padx=10)


if __name__ == "__main__":
    gui = GUI()
    gui.run()