
from copy import deepcopy
import tkinter as tk
from tkinter import font
from matplotlib.pyplot import Figure, Axes
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

from pso.graphics.colors import Color
from pso.graphics.fonts import FontName
from pso.graphics.backButton import BackButton
from pso.optimization import Optimization

class ViewFrame(tk.Frame):
    """ 
    Manages the view of an optimization by iterating through the positions of the particles.
    """
    def __init__(self, initialize_window: callable, change_menu: callable, optimization: Optimization, function_fig: Figure, bg: str = Color.test3_bg) -> "ViewFrame": # ! Correct the type hint in the other classes
        super().__init__(bg=bg)
        self.__initialize_window: callable = initialize_window
        self.__optimization: Optimization = optimization
        self.__function_fig: Figure = function_fig
        back_button_image: tk.PhotoImage = tk.PhotoImage(file="graphics/assets/arrow-back.png").subsample(4)
        back_button_active_image: tk.PhotoImage = tk.PhotoImage(file="graphics/assets/arrow-back-active.png").subsample(4)
        self.__title: tk.Label = tk.Label(self, text=f"Optimization {optimization.index}", height=2, bg=Color.select_title_bg, fg=Color.select_title_fg, font=font.Font(family=FontName.title, size=15))
        self.__back_button: BackButton = BackButton(self, image=back_button_image, active_image=back_button_active_image, width=50, height=50, change_menu=change_menu, change_menu_args={"menu_name": "select"})
        # self.__pause_button # * Could be a BackButton object
        # self.__reset_button # * Could be a BackButton object
        self.__fig_main_axis: Axes = self.__function_fig.get_axes()[0]
        self.__iteration_canvases: list[tk.Canvas] = [self.__create_iteration_canvas(iteration) for iteration in range(0, optimization.iterations + 1)]
        self.__exited_menu: bool = False

    def __create_iteration_canvas(self, iteration: int) -> tk.Canvas:
        fig: Figure = deepcopy(self.__function_fig)
        fig.set_size_inches(4.8, 4.8)
        fig_main_axis: Axes = fig.get_axes()[0]
        fig_main_axis.set_title(f"{self.__optimization.function_choice} - Iteration {iteration}")
        iteration_df_start: int = (iteration * self.__optimization.swarm.get_particle_amount()) + iteration
        iteration_df_end: int = iteration_df_start + self.__optimization.swarm.get_particle_amount()
        iteration_df: pd.DataFrame = self.__optimization.optimization_df["Position"].iloc[iteration_df_start:iteration_df_end]
        for coordinates in iteration_df:
            fig_main_axis.scatter(coordinates[0], coordinates[1], color="red")
        figure_canvas: FigureCanvasTkAgg = FigureCanvasTkAgg(figure=fig, master=self)
        figure_canvas.draw()
        return figure_canvas.get_tk_widget()
    
    def display_iteration_canvas(self, iteration: int) -> None:
        print(self.__exited_menu)
        if self.__exited_menu:
            return None
        try:
            self.__iteration_canvases[iteration-1].pack_forget()
        except IndexError:
            pass
        finally:
            self.__iteration_canvases[iteration].pack(fill="none", expand=True)
            if iteration < self.__optimization.iterations:
                self.after(1000, self.display_iteration_canvas, iteration + 1) # * Schedules the next iteration

    def display(self) -> None:
        for iteration_canvas in self.__iteration_canvases:
            iteration_canvas.pack_forget()
        self.__back_button.focus_set()
        self.__exited_menu = False
        self.__initialize_window(width=500, height=600, title=
        "View optimization - PSO")
        self.__title.pack(fill="x", anchor="e")
        self.__back_button.display(x=0, y=0)
        self.place(x=0, y=0, width=500, height=600)
        print(self.display_iteration_canvas(0)) # ! Weird calls to this function

    def forget(self) -> None:
        self.__exited_menu = True
        self.place_forget()
