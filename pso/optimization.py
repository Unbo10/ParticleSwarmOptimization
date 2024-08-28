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

import numpy as np
import pandas as pd

from pso.swarm.particle_swarm import ParticleSwarm
from pso.vector.position import Position
from pso.database.data import Data

class Optimization:
    """Main class to run the Particle Swarm Optimization (PSO) algorithm.
    
    ## Parameters
    - cognitive_coefficient : float, optional
        The cognitive coefficient used in the PSO algorithm. Default is 2.
    - inertia_coefficient : float, optional
        The inertia coefficient used in the PSO algorithm. Default is 1.
    - social_coefficient : float, optional
        The social coefficient used in the PSO algorithm. Default is 2.
    - particle_amount : int, optional
        The number of particles in the swarm. Default is 10.
    - dimensions : int, optional
        The number of dimensions in the search space. Default is 3.
    - iterations : int, optional
        The number of iterations to run the algorithm. Default is 20.
    
    ## Attributes
    - __cognitive_coefficient : float
        The cognitive coefficient used in the PSO algorithm.
    - __dimensions : int
        The number of dimensions in the search space.
    - __inertia_coefficient : float
        The inertia coefficient used in the PSO algorithm.
    - __iterations : int
        The number of iterations to run the algorithm.
    - __particle_amount : int
        The number of particles in the swarm.
    - __social_coefficient : float
        The social coefficient used in the PSO algorithm.
    - __swarm : ParticleSwarm
        The particle swarm used in the optimization process.
    
    ## Methods
    - heuristic(position: Position) -> float
        Heuristic function to be optimized.
    - optimize() -> None
        Optimizes the heuristic function using the PSO algorithm.

    ### Getters
    - get_cognitive_coefficient() -> float
        Returns the cognitive coefficient.
    - get_dimensions() -> int
        Returns the number of dimensions.
    - get_inertia_coefficient() -> float
        Returns the inertia coefficient.
    - get_iterations() -> int
        Returns the number of iterations.
    - get_particle_amount() -> int
        Returns the number of particles.
    - get_social_coefficient() -> float
        Returns the social coefficient.
    - get_swarm() -> ParticleSwarm
        Returns the particle swarm used in the optimization process.
    """
    def __init__(self, index: int, data: Data = Data("test"), cognitive_coefficient: float = 2.05, inertia_coefficient: float = 0.7, social_coefficient: float = 2.05, particle_amount: int = 10, dimensions: int = 3, iterations: int = 20) -> None:
        self.__data: Data = data
        self.__cognitive_coefficient: float = cognitive_coefficient
        self.__dimensions: int = dimensions
        # ? Might need to make a heuristic function class or at least a
        # ? heuristic function attribute to display it in the select menu of the GUI.
        self.__index: int = index # ! Left to add in docs
        self.__inertia_coefficient: float = inertia_coefficient
        self.__iterations: int = iterations
        self.__particle_amount: int = particle_amount
        self.__social_coefficient: float = social_coefficient
        # * So it doesn't create two particle swarms with different dimensions
        self.__swarm: ParticleSwarm = ParticleSwarm(inertia_coefficient, cognitive_coefficient, social_coefficient, dimensions, particle_amount, self.heuristic)
        self.__data = data
    
    def heuristic(self, position: Position, selection: int = 2) -> float:
        """Heuristic function to be optimized."""
        # TODO: Make a better implementation of choosing the desired function, at the moment it's done manually, by modifying the variable selection through the parameters
        # TODO: Implement the second function to the dimension that the user selects. It is set to two dimensions. ? A dimension parameter in the heuristic ? 
        # * Agree, but what should be then the type of the heuristic_value? A list or maybe an ndarray?
        
        if selection == "1":
            return np.sum(np.square(position.get_coordinates()))
        
        elif selection == "2":
            return 20 + np.sum(np.square(position.get_coordinates()) - 10*math.cos(2 * math.pi *position.get_coordinates()))
        
        elif selection == "3":
            x = position.get_coordinates()[0]
            y = position.get_coordinates()[1]
            return((1 + (x+y+1)**2 * (19 - 14 * x + 3 * x**2 - 14 * y + 6*x*y + 3*y**2)) * (30 + (2*x - 3*y)**2 * (18 - 32 * x + 12 * x**2 + 48 * y - 36*x*y + 27 * y**2)))
        
        elif selection == "4":
            x = position.get_coordinates()[0]
            y = position.get_coordinates()[1]
            return (x + 2*y - 7)**2 + (2*x + y - 5)**2
        
        else:
            return np.sum(np.square(position.get_coordinates()))
        
    def optimize(self) -> None:
        """Optimizes the heuristic function using the PSO algorithm."""
        # ! CHECK: Optimization not working properly. Might have to do with
        # ! how the data is being passed.
        swarm = self.__swarm
        swarm._initialize_particles_randomly()
        swarm.update_gbest()
        swarm_gbest_index: list[int] = []
        optimization_df: pd.DataFrame = pd.DataFrame(columns = ["Heuristic",
                                            "Position", "Velocity", "Pbest"])
        nan_df = pd.DataFrame(([np.nan] * 4), index = ["Heuristic", "Position",
                                                       "Velocity", "Pbest"]).T

        for iteration_num in range(self.__iterations + 1):
            iteration_data: dict = {"Heuristic": [], "Position": [],
                                    "Velocity": [], "Pbest": []}
            for particle in swarm.get_particles():
                if iteration_num > 0: 
                    particle._update_velocity(swarm.get_gbest())
                    particle.get_position()._update(particle.get_velocity())
                    # ! Gbest is not actually gbest
                    particle.get_heuristic()._update(particle.get_position())
                    particle._update_pbest()

                # * Append the data of each particle after a certain iteration
                # * to a temporary dictionary
                # ? Should the np.ndarrays be copies?
                iteration_data["Heuristic"].append(np.round(particle.
                    get_heuristic( ).get_coordinates().copy(), 2))
                iteration_data["Position"].append(np.round(particle.
                    get_position().get_coordinates().copy(), 2))
                iteration_data["Velocity"].append(np.round(particle.
                    get_velocity().get_coordinates().copy(), 2))
                iteration_data["Pbest"].append(np.round(particle.
                    get_pbest().get_coordinates().copy(), 2))

                # print(particle, end="")

            # * Append the last iteration's data and the index of the particle
            # * with the best heuristic to the database.
            swarm.update_gbest()
            print(swarm.get_gbest())
            optimization_df = pd.concat([optimization_df, pd.DataFrame(iteration_data)])
            # TODO: Check the logic behind the if
            if iteration_num != self.__iterations:
                optimization_df = pd.concat([optimization_df, nan_df])
            print(f"Global best: {swarm.get_gbest()}\n")

        # * Append the indexes of the particles with the best heuristic to the
        # * database and create a spreadsheet with the optimization results.
        self.__data.append_gbest_indexes(swarm_gbest_index)
        self.__data.append_optimization(optimization_df)
        # self.__data.print_optimization(0)
            

    # * Getters
    # ! -they might not be needed though
    def get_cognitive_coefficient(self) -> float:
        return self.__cognitive_coefficient

    def get_dimensions(self) -> int:
        return self.__dimensions
    
    def get_index(self) -> int:
        return self.__index

    def get_inertia_coefficient(self) -> float:
        return self.__inertia_coefficient

    def get_iterations(self) -> int:
        return self.__iterations

    def get_particle_amount(self) -> int:
        return self.__particle_amount

    def get_social_coefficient(self) -> float:
        return self.__social_coefficient

    def get_swarm(self) -> ParticleSwarm:
        return self.__swarm

def run():
    pass

if __name__ == "__main__":
    data = Data(excel_file_name="session1_results")
    main = Optimization(0, data=data, cognitive_coefficient=2.05, inertia_coefficient=0.8, social_coefficient=2.05, particle_amount=13, dimensions=2, iterations=7) # ! CHECK: Minimum dimension
    main.optimize()
    # print(main.get_swarm().get_gbest())
