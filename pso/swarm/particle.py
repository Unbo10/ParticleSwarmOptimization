""""""

import numpy as np

from pso.vector.abstract_vector import Vector
from pso.vector.position import Position
from pso.vector.velocity import Velocity

class Particle:
    """
    Particle class represents a particle in a swarm in the context of 
    the Particle Swarm Optimization (PSO) algorithm.

    ## Attributes
    
    All are private.
    __heuristic_vector : Vector
        Fitness or heuristic value of the particle.
    __pbest : Position
        Position where the best heuristic value was found.
    __position : Position
        Current position of the particle.
    __velocity : Velocity
        Current velocity of the particle.

    ## Methods
    get_heuristic_vector() -> Vector
        Returns the fitness or heuristic value of the particle.
    get_pbest() -> Position
        Returns the position where the best heuristic value was found.
    get_position() -> Position
        Returns the current position of the particle.
    get_velocity() -> Velocity
        Returns the current velocity of the particle.
    set_heuristic_vector(heuristic_vector: Vector) -> None
        Sets the fitness or heuristic value of the particle.
    set_pbest(pbest: Position) -> None
        Sets the position where the best heuristic value was found.
    set_position(position: Position) -> None
        Sets the current position of the particle.
    set_velocity(velocity: Velocity) -> None
        Sets the current velocity of the particle.
    """

    def __init__(self, dimensions: int = 3) -> None:
        self.__heuristic_vector: Vector = Vector(dimensions)
        self.__pbest: Position = Position(dimensions-1)
        self.__position: Position = Position(dimensions-1)
        self.__velocity: Velocity = Velocity(dimensions-1)

    def __repr__(self) -> str:
        return f"Particle at {self.__position.get_coordinates()} with pbest at {self.__pbest.get_coordinates()}, velocity {self.__velocity.get_coordinates()} and a heuristic value of {self.__heuristic_vector.get_coordinates()}.\n"
    
    def initialize_randomly(self, bound: int = 10) -> None:
        self.__heuristic_vector.initialize_randomly(bound)
        self.__position.initialize_randomly(bound)
        self.__pbest = self.__position
        self.__velocity.initialize_randomly(bound)

    def _update_pbest(self) -> None:
        if self.__position < self.__pbest:
            self.__pbest.set_coordinates(self.__pbest.get_coordinates())
    
    # * Getters and setters

    def get_heuristic_vector(self) -> Vector:
        return self.__heuristic_vector
    
    def get_pbest(self) -> Position:
        return self.__pbest
    
    def get_position(self) -> Position:
        return self.__position
    
    def get_velocity(self) -> Velocity:
        return self.__velocity
    
    def set_heuristic_vector(self, heuristic_vector: Vector) -> None:
        self.__heuristic_vector = heuristic_vector
    
    def set_pbest(self, pbest: Position) -> None:
        self.__pbest = pbest
    
    def set_position(self, position: Position) -> None:
        self.__position = position
    
    def set_velocity(self, velocity: Velocity) -> None:
        self.__velocity = velocity
        

if __name__ ==  "__main__":
    dimensions: int = 4
    p = Particle()
    print(p.get_heuristic_vector().get_coordinates())
    print(p.get_pbest().get_coordinates())
    print(p.get_position().get_coordinates())
    print(p.get_velocity().get_coordinates())
