
# ! An image class could also be made! There could really be all tk's widgets' classes!
# * This could make a future implementation with ttk or any other module much easier
import numpy as np
import tkinter as tk

from pso.graphics.colors import Color
from pso.optimization import Optimization
from pso.graphics.viewButton import ViewButton

class OptimizationFrame:
    def __init__(self, master: tk.Frame, optimization: Optimization, forget_select_menu: callable, initialize_window: callable, change_menu: callable, width: int, height: int, separation: int, scrollbar_width: int, frame_index: int) -> None:
        self.root: tk.Frame = tk.Frame(master, width=width, height=height)
        self.__width: int = width
        self.__height: int = height
        self.__scrollbar_width: int = scrollbar_width
        self.__separation: int = separation
        self.__index: int = frame_index
        self.__widget_parameters: dict = {
            "master": self.root,
            "bg": Color.select_label_optim_bg,
            "fg": Color.select_label_optim_fg
        }
        # TODO: Try to add the self.root in the dictionary
        # * Seems to be working just fine! Could be implemented in other menus if the master declaration is repeated many times.
        self.__name_label: tk.Label = tk.Label(text=f"Optimization {optimization.index}", **self.__widget_parameters)
        self.__function_label: tk.Label = tk.Label(text=optimization.function_choice, **self.__widget_parameters)
        self.__dimensions_label: tk.Label = tk.Label(text=f"Dimensions: {optimization.dimensions}", **self.__widget_parameters)
        self.__minima_indicator_label: tk.Label = tk.Label(text=f"Minima: ", **self.__widget_parameters)
        minima_coordinates: np.ndarray = np.round(optimization.swarm.get_gbest().get_coordinates(), 3)
        self.__minima_value_label: tk.Label = tk.Label(text=minima_coordinates, **self.__widget_parameters)
        self.__cognitive_coefficient_label: tk.Label = tk.Label(text=f"c1: {optimization.swarm.get_cognitive_coefficient()}", **self.__widget_parameters)
        self.__num_particles_label: tk.Label = tk.Label(text=f"N. of particles: {optimization.swarm.get_particle_amount()}", **self.__widget_parameters)
        self.__social_coefficient_label: tk.Label = tk.Label(text=f"c2: {optimization.swarm.get_social_coefficient()}", **self.__widget_parameters)

        view_button_image: tk.PhotoImage = tk.PhotoImage(file="graphics/assets/preview.png").subsample(4)
        view_button_active_image: tk.PhotoImage = tk.PhotoImage(file="graphics/assets/preview-active.png").subsample(4)
        self.view_button: ViewButton = ViewButton(master=self.root, image=view_button_image, active_image=view_button_active_image, forget_select_menu=forget_select_menu, initialize_window=initialize_window, change_menu=change_menu, optimization=optimization)
        self.__inertia_coefficient_label: tk.Label = tk.Label(text=f"Inertia: {optimization.swarm.get_inertia_coefficient()}", **self.__widget_parameters)
        self.__iterations_label: tk.Label = tk.Label(text=f"N. iterations: {optimization.iterations}", **self.__widget_parameters)

    def display(self, parent_width: int) -> None:
        # labels_list: list[tk.Label] = [attr for attr in dir(self) if attr[-5:] == "label"]
        # * There could be a better way of doing it using a list
        
        # * Sets the optimization frame in the parent frame
        for col in range(0, 5):
            self.root.columnconfigure(col, weight=1)
        for row in range(0, 3):
            self.root.rowconfigure(row, weight=1)
        self.__name_label.grid(row=0, column=0, sticky="nsew")
        self.__function_label.grid(row=1, column=0, sticky="nsew")
        self.__dimensions_label.grid(row=2, column=0, sticky="nsew")
        self.__minima_indicator_label.grid(row=0, column=1, sticky="nsew")
        self.__cognitive_coefficient_label.grid(row=1, column=1, sticky="nsew")
        self.__num_particles_label.grid(row=2, column=1, sticky="nsew")
        self.__minima_value_label.grid(row=0, column=2, sticky="nsew")
        self.__social_coefficient_label.grid(row=1, column=2, sticky="nsew")
        self.view_button.grid(row=0, column=3, sticky="nsew")
        self.__inertia_coefficient_label.grid(row=1, column=3, sticky="nsew")
        self.__iterations_label.grid(row=2, column=3, sticky="nsew")
        self.root.place(x=((parent_width - self.__width - self.__scrollbar_width)//2), y=self.__index*(self.__height + self.__separation) + self.__separation, width=self.__width, height=self.__height)
        # ? Maybe raise an error if the x- or y- coordinates do not make sense


if __name__ == "__main__":
    optim = OptimizationFrame(tk.Tk(), Optimization(1), 50, 30)
    optim.display()

