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

from pso.vector.abstract_vector import Vector
from pso.vector.heuristic import Heuristic, default_heuristic
from pso.vector.position import Position
from pso.vector.velocity import Velocity

class Particle:
    """
    Particle class represents a particle in a swarm in the context of 
    the Particle Swarm Optimization (PSO) algorithm.

    ## Attributes
    
    All are private.
    __heuristic : Heuristic
        Fitness or heuristic value of the particle.
    __pbest : Position
        Position where the best heuristic value was found.
    __position : Position
        Current position of the particle.
    __velocity : Velocity
        Current velocity of the particle.

    ## Methods
    initialize_randomly(bound=10)
        Initializes the position, velocity, heuristic and pbest of the particle randomly.

    ### Getters and setters

    get_heuristic() -> Vector
        Returns the fitness or heuristic value of the particle.
    get_pbest() -> Position
        Returns the position where the best heuristic value was found.
    get_position() -> Position
        Returns the current position of the particle.
    get_velocity() -> Velocity
        Returns the current velocity of the particle.
    set_heuristic(heuristic: Vector) -> None
        Sets the fitness or heuristic value of the particle.
    set_pbest(pbest: Position) -> None
        Sets the position where the best heuristic value was found.
    set_position(position: Position) -> None
        Sets the current position of the particle.
    set_velocity(velocity: Velocity) -> None
        Sets the current velocity of the particle.
    """

    def __init__(self, index: int, has_gbest: bool, dimensions: int = 3, heuristic: callable = default_heuristic) -> None:
        self.__index: int = index
        self.__position: Position = Position(dimensions-1)
        self.__pbest: Position = Position(dimensions-1)
        self.__heuristic: Heuristic = Heuristic(dimensions, heuristic)
        self.__heuristic._update(self.get_pbest())
        self.__velocity: Velocity = Velocity(dimensions-1)
        self.has_gbest = False

    def __repr__(self) -> str:
        return f"Particle at {self.__position.get_coordinates()} with pbest at {self.__pbest.get_coordinates()}, velocity {self.__velocity.get_coordinates()} and a heuristic value of {self.__heuristic.get_coordinates()}.\n"
    
    def initialize_randomly(self, bound: int = 10) -> None:
        """Initializes the (__)position, (__)velocity, (__)heuristic and (__)pbest of the particle randomly.
        
        ## Parameters
        bound : int
            The upper bound for the random initialization. Default is 10.
        """
        self.__position.initialize_randomly(bound, self.__position.get_dimensions())
        self.__heuristic._update(self.__position)
        self.__pbest.set_coordinates(self.__position.get_coordinates().copy())
        self.__velocity.initialize_randomly(np.linalg.norm(self.__position.get_coordinates().copy()), self.__velocity.get_dimensions())

    def _update_pbest(self) -> None:
        """Updates the best position of the particle (__pbest) comparing the heuristic
        value (last coordinate of the heuristic vector) of the current position 
        (__position) with the heuristic value of the best position found up to the i-th
        iteration (__pbest)."""
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
