
# ! An image class could also be made! There could really be all tk's widgets' classes!
# * This could make a future implementation with ttk or any other module much easier
"""
This module defines the OptimizationFrame class, which represents a frame displaying the optimization details.

## Classes
- OptimizationFrame: Represents a frame displaying optimization details.

### Attributes
- frame: tk.Frame - The main frame for the optimization details.
- __width: int - The width of the frame.
- __height: int - The height of the frame.
- __scrollbar_width: int - The width of the scrollbar.
- __separation: int - The separation between frames.
- __index: int - The index of the frame.
- __widget_parameters: dict - Parameters for the widgets.
- __name_label: tk.Label - Label displaying the name of the optimization.
- __function_label: tk.Label - Label displaying the function of the optimization.
- __dimensions_label: tk.Label - Label displaying the dimensions of the optimization.
- __minima_indicator_label: tk.Label - Label indicating the minima.
- __minima_value_label: tk.Label - Label displaying the minima coordinates.
- __cognitive_coefficient_label: tk.Label - Label displaying the cognitive coefficient.
- __num_particles_label: tk.Label - Label displaying the number of particles.
- __social_coefficient_label: tk.Label - Label displaying the social coefficient.
- __preview_image: tk.PhotoImage - Image for the preview button.
- __preview_active_image: tk.PhotoImage - Active image for the preview button.
- __preview_button: tk.Button - Button for previewing the optimization.
- __inertia_coefficient_label: tk.Label - Label displaying the inertia coefficient.
- __iterations_label: tk.Label - Label displaying the number of iterations.

### Methods
- display(parent_width: int) -> None: Displays the optimization frame and configures the labels and buttons.
- __enter_preview_button(e): Changes the background and image of the preview button when the cursor enters.
- __leave_preview_button(e): Restores the background and image of the preview button when the cursor leaves.
- __click_preview_button(e): Changes the background and image of the preview button when clicked.
- __release_preview_button(e): Placeholder for actions when the preview button is released.
"""
import numpy as np
import tkinter as tk
from tkinter import font

from pso.graphics.colors import Color
from pso.optimization import Optimization

class OptimizationFrame:
    def __init__(self, root: tk.Frame, optimization: Optimization, width: int, height: int, separation: int, scrollbar_width: int, frame_index: int) -> None:
        self.frame: tk.Frame = tk.Frame(root, width=width, height=height)
        self.__width: int = width
        self.__height: int = height
        self.__scrollbar_width: int = scrollbar_width
        self.__separation: int = separation
        self.__index: int = frame_index
        self.__widget_parameters: dict = {
            "bg": Color.select_label_optim_bg,
            "fg": Color.select_label_optim_fg
        }
        # TODO: Try to add the self.frame in the dictionary
        self.__name_label: tk.Label = tk.Label(self.frame, text=f"Optimization {optimization.get_index()}", **self.__widget_parameters)
        self.__function_label: tk.Label = tk.Label(self.frame, text=f"Function: TO BE DECIDED", **self.__widget_parameters)
        self.__dimensions_label: tk.Label = tk.Label(self.frame, text=f"Dimensions: {optimization.get_dimensions()}", **self.__widget_parameters)
        self.__minima_indicator_label: tk.Label = tk.Label(self.frame, text=f"Minima: ", **self.__widget_parameters)
        minima_coordinates: np.ndarray = np.round(optimization.get_swarm().get_gbest().get_coordinates(), 3)
        self.__minima_value_label: tk.Label = tk.Label(self.frame, text=minima_coordinates, **self.__widget_parameters)
        self.__cognitive_coefficient_label: tk.Label = tk.Label(self.frame, text=f"c1: {optimization.get_swarm().get_cognitive_coefficient()}", **self.__widget_parameters)
        self.__num_particles_label: tk.Label = tk.Label(self.frame, text=f"N. of particles: {optimization.get_swarm().get_particle_amount()}", **self.__widget_parameters)
        self.__social_coefficient_label: tk.Label = tk.Label(self.frame, text=f"c2: {optimization.get_swarm().get_social_coefficient()}", **self.__widget_parameters)
        self.__preview_image: tk.PhotoImage = tk.PhotoImage(file="assets/preview.png").subsample(4)
        self.__preview_active_image: tk.PhotoImage = tk.PhotoImage(file="assets/preview-active.png").subsample(4)

        # TODO: Check the naming of immages across files

        self.__preview_button: tk.Button = tk.Button(self.frame, image=self.__preview_image, **self.__widget_parameters)
        self.__inertia_coefficient_label: tk.Label = tk.Label(self.frame, text=f"Inertia: {optimization.get_swarm().get_inertia_coefficient()}", **self.__widget_parameters)
        self.__iterations_label: tk.Label = tk.Label(self.frame, text=f"N. iterations: {optimization.get_iterations()}")

    def display(self, parent_width: int) -> None:
        # labels_list: list[tk.Label] = [attr for attr in dir(self) if attr[-5:] == "label"]
        # * There could be a better way of doing it using a list
        for col in range(0, 5):
            self.frame.columnconfigure(col, weight=1)
        for row in range(0, 3):
            self.frame.rowconfigure(row, weight=1)
        self.__preview_button.bind("<Enter>", self.__enter_preview_button)
        self.__preview_button.bind("<Leave>", self.__leave_preview_button)
        self.__preview_button.bind("<Button-1>", self.__click_preview_button)
        self.__preview_button.bind("ButtonRelease-1", self.__release_preview_button)
        self.__name_label.grid(row=0, column=0, sticky="nsew")
        self.__function_label.grid(row=1, column=0, sticky="nsew")
        self.__dimensions_label.grid(row=2, column=0, sticky="nsew")
        self.__minima_indicator_label.grid(row=0, column=1, sticky="nsew")
        self.__cognitive_coefficient_label.grid(row=1, column=1, sticky="nsew")
        self.__num_particles_label.grid(row=2, column=1, sticky="nsew")
        self.__minima_value_label.grid(row=0, column=2, sticky="nsew")
        self.__social_coefficient_label.grid(row=1, column=2, sticky="nsew")
        self.__preview_button.grid(row=0, column=3, sticky="nsew")
        self.__inertia_coefficient_label.grid(row=1, column=3, sticky="nsew")
        self.__iterations_label.grid(row=2, column=3, sticky="nsew")
        self.frame.place(x=((parent_width - self.__width - self.__scrollbar_width)//2), y=self.__index*(self.__height + self.__separation) + self.__separation, width=self.__width, height=self.__height)
        # ? Maybe raise an error if the x- or y- coordinates do not make sense

    def __enter_preview_button(self, e):
        self.__preview_button.config(bg=Color.preview_button_abg, image=self.__preview_active_image)

    def __leave_preview_button(self, e):
        self.__preview_button.config(bg=Color.preview_button_bg, image=self.__preview_image)

    def __click_preview_button(self, e):
        self.__preview_button.config(bg=Color.preview_button_cbg, image=self.__preview_image)

    def __release_preview_button(self, e):
        pass


if __name__ == "__main__":
    optim = OptimizationFrame(tk.Tk(), Optimization(1), 50, 30)
    optim.display()

