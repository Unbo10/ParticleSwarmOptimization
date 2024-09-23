from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import colors
import numpy as np
import tkinter as tk
from tkinter import font

from pso.graphics.backButton import BackButton
from pso.graphics.colors import Color
from pso.graphics.fonts import FontName
from pso.graphics.createMenu.createInput import CreateInput
from pso.graphics.createMenu.functionChoiceMenu import FunctionChoiceMenu
from pso.graphics.createMenu.createButton import CreateButton
from pso.optimization import Optimization
from pso.database.data import Data

class CreateMenu:
    """
    This class manages all the inputs, buttons and the graph display for the create optimization menu.
    """
    def __init__(self, master_frame, initialize_window: callable, change_menu: callable, optimization_history: list[Optimization], data: Data, window_width: int, window_height: int):
        self.__initialize_window: callable = initialize_window
        self.__change_menu: callable = change_menu
        self.__optimization_history: list[Optimization] = optimization_history
        self.__data: Data = data
        self.__width: int = window_width
        self.__height: int = window_height
        self.root: tk.Frame = tk.Frame(master_frame)
        # ! Inheritance could also be applied with title -it's literally the same save the text
        self.__title_height: int = 2
        self.__title: tk.Label = tk.Label(self.root, text="Create optimization", font=font.Font(family=FontName.title, size=15), height=self.__title_height, bg=Color.select_title_bg, fg=Color.select_title_fg)
        back_button_image: tk.PhotoImage = tk.PhotoImage(file="graphics/assets/arrow-back.png").subsample(4)
        back_button_active_image: tk.PhotoImage = tk.PhotoImage(file="graphics/assets/arrow-back-active.png").subsample(4)
        self.__back_button: BackButton = BackButton(self.root, image=back_button_image, active_image=back_button_active_image, width=self.__title_height * 25, height=self.__title_height * 25, change_menu=change_menu, change_menu_args={"menu_name": "main"})

        self.__inputs_frame: tk.Frame = tk.Frame(self.root, bg=Color.test1_bg)
        entry_width: int = 20
        self.__w_coefficient_input: CreateInput = CreateInput(self.__inputs_frame, default_value="0.7", text="Intertia coefficiet",width=entry_width)
        self.__cog_coefficient_input: CreateInput = CreateInput(self.__inputs_frame, default_value=2, text="Cognitive coefficient", width=entry_width)
        self.__soc_coefficient_input: CreateInput = CreateInput(self.__inputs_frame, default_value=2, text="Social coefficient", width=entry_width)
        self.__function_option: FunctionChoiceMenu = FunctionChoiceMenu(self.__inputs_frame, text="Choose a function", options=["Sphere", "Booth", "Goldstein-Price", "Rastrigin"], display_graph=self.display_graph)
        self.__particle_amount_input: CreateInput = CreateInput(self.__inputs_frame, default_value="1", text="Particle amount", width=entry_width)
        self.__iterations_input: CreateInput = CreateInput(self.__inputs_frame, default_value="1", text="Iterations", width=entry_width)
        self.__inputs: list[CreateInput] = [self.__w_coefficient_input, self.__cog_coefficient_input, self.__soc_coefficient_input, self.__function_option, self.__particle_amount_input, self.__iterations_input]

        self.__buttons_frame: tk.Frame = tk.Frame(self.root, bg=Color.test2_bg)
        self.__run_view_button: CreateButton = CreateButton(parent_frame=self.__buttons_frame, text1="Run optimization", text2="View optimization", callable1=self.__run_optimization, callable2=self.__view_optimization, padx=20, pady=20)
        self.__reset_button: CreateButton = CreateButton(parent_frame=self.__buttons_frame, text1="Reset", text2="New optimization", callable1=self.__reset_parameters, callable2=self.__reset_parameters, padx=20, pady=20)
        
        self.__figs: dict = {"Sphere": self.__create_fig("Sphere"), "Booth": self.__create_fig("Booth"), "Goldstein-Price": self.__create_fig("Goldstein-Price"), "Rastrigin": self.__create_fig("Rastrigin")}
        self.__plot_canvases: dict = {"Sphere": self.__create_fig_canvas(self.__figs["Sphere"]), "Booth": self.__create_fig_canvas(self.__figs["Booth"]), "Goldstein-Price": self.__create_fig_canvas(self.__figs["Goldstein-Price"]), "Rastrigin": self.__create_fig_canvas(self.__figs["Rastrigin"])}

    def __run_optimization(self) -> None:
        new_optimization = Optimization(index=len(self.__optimization_history) + 1, function_fig=self.__figs[self.__function_option.get_choice()], function_choice=self.__function_option.get_choice(), data=self.__data, cognitive_coefficient=float(self.__cog_coefficient_input.get_input()), inertia_coefficient=float(self.__w_coefficient_input.get_input()), social_coefficient=float(self.__soc_coefficient_input.get_input()), particle_amount=int(self.__particle_amount_input.get_input()), dimensions=3, iterations=int(self.__iterations_input.get_input()))
        new_optimization.optimize()
        self.__optimization_history.append(new_optimization)

    def __reset_parameters(self) -> None:
        # * Resets all the inputs to their default values
        self.__w_coefficient_input.entry.delete(0, "end")
        self.__cog_coefficient_input.entry.delete(0, "end")
        self.__soc_coefficient_input.entry.delete(0, "end")
        self.__particle_amount_input.entry.delete(0, "end")
        self.__iterations_input.entry.delete(0, "end")
        self.__function_option.choice = "Sphere"
        self.__w_coefficient_input.entry.focus_set()
        self.__run_view_button.config(text=self.__run_view_button.text1)

    def __view_optimization(self) -> None:
        self.__change_menu("select")

    def run_or_view_optimization(self, e, create_optimization: bool) -> None:
        if create_optimization == True:
            self.__run_optimization()
        else:
            self.__view_optimization()

    def __create_contour_levels(self, levels_boundaries: list[float]) -> np.linspace:
        # * Creates the levels for the contour plot based on the boundaries of the test functions
        i = 1
        levels: np.ndarray = np.linspace(start=levels_boundaries[0], stop=levels_boundaries[1], num=10) # * So that levels isn't empty and can be concatenated
        while i < len(levels_boundaries) - 1:
            levels = np.concatenate((levels, np.linspace(start=levels_boundaries[i] + (levels_boundaries[i]/10), stop=levels_boundaries[i + 1], num=10)))
            i += 1
        return levels
    
    def __create_x_y_values(self, bound: int) -> tuple[np.ndarray]:
        x: np.ndarray = np.linspace(start=-bound, num=100, stop=bound)
        y: np.ndarray = np.linspace(start=-bound, num=100, stop=bound)
        return np.meshgrid(x, y)

    def __create_fig(self, option: str) -> Figure:
        # * Generates the figure for the contour plot for each test function
        fig = Figure(figsize=(5,5))
        plot = fig.add_subplot(111)
        levels_boundaries: list[float] = []
        z: np.ndarray = None
        contour = None

        if option == "Sphere":
            x, y = self.__create_x_y_values(bound=2)
            z = x**2 + y**2
            levels_boundaries = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            levels = self.__create_contour_levels(levels_boundaries)
            contour = plot.contourf(x, y, z, levels=levels, cmap="viridis") # * Sets the different colors for different z-values.
            plot.set_title("Sphere function")

        if option == "Booth":
            x, y = self.__create_x_y_values(bound=10)
            z = (x + 2*y - 7)**2 + (2*x + y - 5)**2
            levels_boundaries = [0.1, 1, 10, 100, 1000, 10000] # * Ticks or labels in the colorbar following the test functions graphs
            levels = self.__create_contour_levels(levels_boundaries)
            norm = colors.LogNorm(vmin=levels_boundaries[0], vmax=levels_boundaries[len(levels_boundaries) - 1]) # * Applying a logaritmic normalization to the colorbar
            contour = plot.contourf(x, y, z, levels=levels, cmap="viridis", norm=norm)
            plot.set_title("Booth function")

        if option == "Goldstein-Price":
            x, y = self.__create_x_y_values(bound=2)
            z = (1 + (x+y+1)**2 * (19 - 14 * x + 3 * x**2 - 14 * y + 6*x*y + 3*y**2)) * (30 + (2*x - 3*y)**2 * (18 - 32 * x + 12 * x**2 + 48 * y - 36*x*y + 27 * y**2))
            levels_boundaries = [1, 10, 100, 1000, 10000, 100000, 1000000]
            levels = self.__create_contour_levels(levels_boundaries)
            norm = colors.LogNorm(vmin=levels_boundaries[0], vmax=levels_boundaries[len(levels_boundaries) - 1])
            contour = plot.contourf(x, y, z, levels=levels, cmap="viridis", norm=norm)
            plot.set_title("Goldstein-Price function")

        if option == "Rastrigin":
            x, y = self.__create_x_y_values(bound=5.12)
            z = 10*2 + (x**2 - 10*np.cos(2 * np.pi * x)) + (y**2 - 10*np.cos(2 * np.pi * y))
            levels_boundaries = [0, 10, 20, 30, 40, 50, 60, 70, 80]
            levels = self.__create_contour_levels(levels_boundaries)
            contour = plot.contourf(x, y, z, levels=levels, cmap="viridis")
            plot.set_title("Rastrigin function")

        fig.colorbar(contour, ax=plot, ticks=levels_boundaries)
        plot.set_xlabel("X axis")
        plot.set_ylabel("Y axis")
        fig.subplots_adjust(left=0.225, right=0.90, top=0.825, bottom=0.225) # * Centers the graph
        return fig
    
    def __create_fig_canvas(self, fig: Figure) -> tk.Canvas:
        fig_canvas: FigureCanvasTkAgg = FigureCanvasTkAgg(figure=fig, master=self.root)
        fig_canvas.draw()
        return fig_canvas.get_tk_widget()

    def display_graph(self, option: str):
        for canvas in self.__plot_canvases.values():
            canvas.pack_forget()

        self.__plot_canvases[option].pack(fill="x", expand=True, anchor="ne", side="right", padx=10, pady=(10, 10))

    def display(self):
        self.__initialize_window(width=self.__width, height=self.__height, title="Create Optimization (PSO)")
        self.__title.pack(fill="x", anchor="n", side="top")
        self.__back_button.focus_set()
        for row in range(6):
            self.__inputs_frame.grid_rowconfigure(row, weight=1)
        self.__inputs_frame.columnconfigure(0, weight=1)
        self.__inputs_frame.columnconfigure(1, weight=1)
        i = 0
        for input in self.__inputs:
            input.grid(label_row=i, column=0, sticky="nsew")
            i += 1
        self.__inputs_frame.pack(fill="both", expand=True, anchor="sw", side="left", padx=(10, 0), pady=(10, 10))
        self.__buttons_frame.rowconfigure(0, weight=1)
        self.__buttons_frame.columnconfigure(0, weight=1)
        self.__buttons_frame.columnconfigure(1, weight=1)
        self.__run_view_button.grid_display(row=0, column=0, sticky="nsew")
        self.__reset_button.grid_display(row=0, column=1, sticky="nsew")
        self.__buttons_frame.pack(fill="both", expand=True, anchor="se", side="bottom", pady=(0, 10))
        self.__back_button.display(x=0, y=0)
        self.display_graph("Sphere")
        self.root.place(x=0, y=0, width=self.__width, height=self.__height)

    def forget(self) -> None:
        self.root.focus_set()
        self.root.place_forget()
        self.__title.pack_forget()
        self.__inputs_frame.pack_forget()
        self.__buttons_frame.pack_forget()
        self.__back_button.forget()