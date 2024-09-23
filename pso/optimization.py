"""
A module to run the Particle Swarm Optimization (PSO) algorithm.

## Classes
Main: Main class to run the Particle Swarm Optimization (PSO) algorithm.

### Methods
- graph_heuristic() -> None
- graph_particles() -> None
- heuristic(position: Position) -> float
- optimize() -> None

#### Getters
- get_cognitive_coefficient() -> float
- get_dimensions() -> int
- get_inertia_coefficient() -> float
- get_iterations() -> int
- get_particle_amount() -> int
- get_social_coefficient() -> float
- get_swarm() -> ParticleSwarm
"""
import math
from matplotlib.pyplot import Figure

import numpy as np
import pandas as pd

from pso.swarm.particle_swarm import ParticleSwarm
from pso.vector.position import Position
from pso.database.data import Data

class Optimization:
    def __init__(self, index: int, function_fig: Figure, function_choice: str = "Sphere", data: Data = Data("test"), cognitive_coefficient: float = 2.05, inertia_coefficient: float = 0.7, social_coefficient: float = 2.05, particle_amount: int = 10, dimensions: int = 3, iterations: int = 20) -> None:
        self.__data: Data = data
        # ? Might need to make a heuristic function class or at least a
        # ? heuristic function attribute to display it in the select menu of the GUI.
        self.__iterations: int = iterations
        # * So it doesn't create two particle swarms with different dimensions
        self.__function_choice: str = function_choice
        self.__swarm: ParticleSwarm = ParticleSwarm(self.heuristic(function_choice), inertia_coefficient, cognitive_coefficient, social_coefficient, dimensions, particle_amount)
        self.__index: int = index
        self._dimensions: int = dimensions
        self.function_fig: Figure = function_fig
        self.__optimization_df: pd.DataFrame = None
        self.bound: float = 0

    @property
    def optimization_df(self) -> pd.DataFrame:
        return self.__optimization_df

    def sphere_f(self, position: Position):
        return np.sum(np.square(position.get_coordinates()))
    
    def booth_f(self, position: Position):
        x = position.get_coordinates()[0]
        y = position.get_coordinates()[1]
        return (x + 2*y - 7)**2 + (2*x + y - 5)**2
    
    def goldstein_price_f(self, position: Position):
        x = position.get_coordinates()[0]
        y = position.get_coordinates()[1]
        return((1 + (x+y+1)**2 * (19 - 14 * x + 3 * x**2 - 14 * y + 6*x*y + 3*y**2)) * (30 + (2*x - 3*y)**2 * (18 - 32 * x + 12 * x**2 + 48 * y - 36*x*y + 27 * y**2)))

    def rastrigin_f(self, position: Position):
        return 20 + np.sum(np.square(position.get_coordinates()) - 10*np.cos(2 * np.pi *position.get_coordinates()))
    
    def heuristic(self, selection: str) -> callable:
        """Heuristic function to be optimized."""
        # TODO: Make a better implementation of choosing the desired function, at the moment it's done manually, by modifying the variable selection through the parameters
        # TODO: Implement the second function to the dimension that the user selects. It is set to two dimensions. ? A dimension parameter in the heuristic ? 
        # * Agree, but what should be then the type of the heuristic_value? A list or maybe an ndarray?
        # * Already solved

        if selection == "Sphere":
            self.bound = 2
            return self.sphere_f
        
        if selection == "Booth": #(1,3)
            self.bound = 10
            return self.booth_f
        
        if selection == "Goldstein-Price": #(0,-1)
            self.bound = 2
            return self.goldstein_price_f
        
        elif selection == "Rastrigin":
            self.bound = 5.12
            return self.rastrigin_f
                                
        else:
            raise NotImplementedError(f"Function {selection} not implemented")
        
    def optimize(self) -> None:
        """Optimizes the heuristic function using the PSO algorithm."""
        self.heuristic(self.__function_choice) # * So the bounds are initialized correctly.
        swarm = self.__swarm
        swarm._initialize_particles_randomly(bound=self.bound)
        swarm.update_gbest()
        swarm_gbest_index: list[int] = []
        optimization_df: pd.DataFrame = pd.DataFrame(columns = ["Heuristic",
                                            "Position", "Velocity", "Pbest"])
        # * A df of nan's is created to separate optimizations more evidently when passing them to the database and when showing them in the GUI
        nan_df = pd.DataFrame(([np.nan] * 4), index = ["Heuristic", "Position",
                                                       "Velocity", "Pbest"]).T

        for iteration_num in range(self.__iterations + 1):
            iteration_data: dict = {"Heuristic": [], "Position": [],
                                    "Velocity": [], "Pbest": []}
            for particle in swarm.get_particles():
                if iteration_num > 0: 
                    # * To record the initial states of the particles before optimizing them
                    particle._update_velocity(swarm.get_gbest())
                    particle.get_position()._update(particle.get_velocity())
                    particle.get_velocity().set_coordinates(np.clip(particle.get_position().get_coordinates(), -5, 5))
                    
                    new_position = particle.get_position().get_coordinates()
                    new_position = np.clip(new_position, -10, 10)
                    particle.get_position().set_coordinates(new_position) 
                    
                    # ! Gbest is not actually gbest
                    # * Seems to be solved
                    
                    # ! Check if the boundaries are necessary or correct, seems to graph prettier at least.
                    particle.get_heuristic()._update(particle.get_position())
                    particle._update_pbest()
                    particle.get_velocity().set_coordinates(np.clip(particle.get_position().get_coordinates(), -5, 5))
                    new_position = particle.get_position().get_coordinates()
                    new_position = np.clip(new_position, -10, 10)
                    particle.get_position().set_coordinates(new_position) 
                    

                # * Append the data of each particle after a certain iteration
                # * to a temporary dictionary
                # ? Should the np.ndarrays be copies?
                iteration_data["Heuristic"].append(np.round(particle.
                    get_heuristic().get_coordinates().copy(), 2))
                iteration_data["Position"].append(np.round(particle.
                    get_position().get_coordinates().copy(), 2))
                iteration_data["Velocity"].append(np.round(particle.
                    get_velocity().get_coordinates().copy(), 2))
                iteration_data["Pbest"].append(np.round(particle.
                    get_pbest().get_coordinates().copy(), 2))

            # * Append the last iteration's data and the index of the particle
            # * with the best heuristic to the database.
            swarm.update_gbest()
            # print(swarm.get_gbest())
            optimization_df = pd.concat([optimization_df, pd.DataFrame(iteration_data)])
            # TODO: Check the logic behind the if.
            # * Seems to be working fine
            if iteration_num != self.__iterations:
                optimization_df = pd.concat([optimization_df, nan_df])
            print(f"Global best: {swarm.get_gbest()}, Heuristic value:{swarm.get_heuristic()(swarm.get_gbest())}\n")

        # * Append the indexes of the particles with the best heuristic to the
        # * database and create a spreadsheet with the optimization results.
        self.__data.append_gbest_indexes(swarm_gbest_index)
        self.__data.append_optimization(optimization_df)
        self.__optimization_df = optimization_df
    
    @property
    def function_choice(self) -> str:
        return self.__function_choice

    # TODO: Make this getters' attributes properties
    # * Done
    @property
    def dimensions(self) -> int:
        return self._dimensions
    
    @property
    def index(self) -> int:
        return self.__index
    
    @property
    def iterations(self) -> int:
        return self.__iterations

    @property
    def swarm(self) -> ParticleSwarm:
        return self.__swarm
    
if __name__ == "__main__":
    data = Data(excel_file_name="session1_results")
    main = Optimization(0, data=data, cognitive_coefficient=1.5, inertia_coefficient=0.4, social_coefficient=1.5, particle_amount=20, dimensions=3, iterations=100) # ! CHECK: Minimum dimension
    main.optimize()
    print(main.get_swarm().get_gbest())
