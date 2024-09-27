"""
This module defines the Particle class, which represents a particle in a swarm in the context of the Particle Swarm Optimization (PSO) algorithm.

## Classes
- Particle: Represents a particle in a swarm in the context of the PSO algorithm.

### Methods
- initialize_randomly(bound=10): Initializes the position, velocity, heuristic, and pbest of the particle randomly.
- _update_pbest(): Updates the best position of the particle (__pbest) comparing the heuristic value.

#### Getters and setters
- get_heuristic() -> Heuristic
- get_pbest() -> Position
- get_position() -> Position
- get_velocity() -> Velocity
- set_heuristic(heuristic: Vector) -> None
- set_pbest(pbest: Position) -> None
- set_position(position: Position) -> None
- set_velocity(velocity: Velocity) -> None
"""

import numpy as np

from psopackage.vector.base_vector import Vector
from psopackage.vector.heuristic import Heuristic
from psopackage.vector.position import Position
from psopackage.vector.velocity import Velocity

class Particle:
    """
    Particle class represents a particle in a swarm in the context of 
    the Particle Swarm Optimization (PSO) algorithm.

    ## Attributes
    
    ### Private
    - heuristic : Heuristic
        Fitness or heuristic value of the particle.
    - pbest : Position
        Position where the best heuristic value was found.
    - position : Position
        Current position of the particle.
    - velocity : Velocity
        Current velocity of the particle.
    
    ### Public
    - color : dict
        Color of the particle's heuristic.
    - has_gbest : bool
        If the particle has a global best position.

    ## Methods
    - initialize_randomly(bound=10)
        Initializes the position, velocity, heuristic and pbest of the particle randomly.

    ### Getters and setters

    - get_heuristic() -> Vector
        Returns the fitness or heuristic value of the particle.
    - get_pbest() -> Position
        Returns the position where the best heuristic value was found.
    - get_position() -> Position
        Returns the current position of the particle.
    - get_velocity() -> Velocity
        Returns the current velocity of the particle.
    - set_heuristic(heuristic: Vector) -> None
        Sets the fitness or heuristic value of the particle.
    - set_pbest(pbest: Position) -> None
        Sets the position where the best heuristic value was found.
    - set_position(position: Position) -> None
        Sets the current position of the particle.
    - set_velocity(velocity: Velocity) -> None
        Sets the current velocity of the particle.
    """
    # ! Update documentation

    def __init__(self, heuristic_f: callable, index: int, has_gbest: bool, cognitive_coefficient: float = 2.0, dimensions: int = 3, inertia_coefficient: float = 1.0, social_coefficient: float = 2.0) -> None:
        self.__cognitive_coefficient: float = cognitive_coefficient
        self.__index: int = index
        self.__inertia_coefficient: float = inertia_coefficient
        self.__social_coefficient: float = social_coefficient
        self.__position: Position = Position(dimensions-1)
        self.__pbest: Position = Position(dimensions-1)
        self.__heuristic: Heuristic = Heuristic(heuristic_f, dimensions)
        self.__heuristic._update(self.get_pbest())
        self.__velocity: Velocity = Velocity(dimensions-1)
        self.color : dict = {"r": 0, "g": 0, "b": 0}
        self.has_gbest = has_gbest

    def __repr__(self) -> str:
        return f"Particle at {self.__position.get_coordinates()} with pbest at {self.__pbest.get_coordinates()}, velocity {self.__velocity.get_coordinates()} and a heuristic value of {self.__heuristic.get_coordinates()}.\n"
    
    def initialize_randomly(self, bound: int = 10) -> None:
        """Initializes the (__)position, (__)velocity, (__)heuristic and (__)pbest of the particle randomly.
        
        ## Parameters
        bound : int
            The upper bound for the random initialization. Default is 10.
        """
        self.__position.initialize_randomly(bound, self.__position.get_dimensions())
        self.__velocity.initialize_randomly(bound / 5, self.__position.get_dimensions())
        self.__position._update(self.__velocity)
        self.__heuristic._update(self.__position)
        self.__pbest.set_coordinates(self.__position.get_coordinates().copy())

    def _update_velocity(self, gbest: Position) -> None:
        # ! There must be something wrong with this method: the operation is not being performed correctly.
        # * It may be correct, just the parameters not the ideal ones.
        """
        Updates the velocity vector based on the particle swarm optimization
        formula:
        v(i + 1) = w * v(i) + c1 * r1 * (pbest - x(i)) + c2 * r2 * (gbest - x(i))

        ### Notes
        - The `position`, `pbest`, and `gbest` constants should have the same shape as the velocity vector.
        - The `w` constant (inertia coefficient) ranges between 0 and 1.
        - The `c1` (cognitive coefficient) and `c2` (social coefficient) constants range between 1 and 3.
        - The `r1` and `r2` values are random numbers between 0 and 1.
        """

        x_i: np.ndarray = self.__position.get_coordinates()
        pbest: np.ndarray = self.__pbest.get_coordinates()
        initial_velocity: np.ndarray = self.__velocity.get_coordinates()
        r1: float = np.random.uniform(0, 1)
        r2: float = np.random.uniform(0, 1)
        w: float = self.__inertia_coefficient
        c1: float = self.__cognitive_coefficient
        c2: float = self.__social_coefficient
        final_velocity: np.ndarray = (w * initial_velocity) + (c1 * r1 * (pbest - x_i)) + (c2 * r2 * (gbest.get_coordinates() - x_i))
        final = np.clip(final_velocity, -5, 5)
        self.__velocity.set_coordinates(final)

    def _update_pbest(self) -> None:
        """Updates the best position of the particle (__pbest) comparing the heuristic
        value (last coordinate of the heuristic vector) of the current position 
        (__position) with the heuristic value of the best position found up to
        the i-th iteration (__pbest)."""
        heuristic_f = self.__heuristic.get_heuristic_f()
        if heuristic_f(self.__position) < heuristic_f(self.__pbest):
            self.__pbest.set_coordinates(self.__position.get_coordinates().copy())
    
    # * Getters and setters

    def get_heuristic(self) -> Heuristic:
        return self.__heuristic
    
    def get_index(self) -> int:
        return self.__index
    
    def get_pbest(self) -> Position:
        return self.__pbest
    
    def get_position(self) -> Position:
        return self.__position
    
    def get_velocity(self) -> Velocity:
        return self.__velocity
    
    def set_heuristic(self, heuristic: Vector) -> None:
        self.__heuristic = heuristic
    
    def set_pbest(self, pbest: Position) -> None:
        self.__pbest = pbest
    
    def set_position(self, position: Position) -> None:
        self.__position = position
    
    def set_velocity(self, velocity: Velocity) -> None:
        self.__velocity = velocity
        

if __name__ ==  "__main__":
    dimensions: int = 4
    p = Particle(0)
    print(p.get_heuristic().get_coordinates())
    print(p.get_pbest().get_coordinates())
    print(p.get_position().get_coordinates())
    print(p.get_velocity().get_coordinates())
