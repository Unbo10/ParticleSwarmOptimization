"""
This module provides a Heuristic class that represents a vector with a 
heuristic value.

## Classes
Heuristic: A class that represents a vector with a heuristic value.

Vector: Inherited from the base_vector module

### Methods
_update (position): Updates the vector based on the given position vector.

Other methods inherited from the Vector class of the base_vector module.

#### Getters
get_heuristic_f(): Returns the heuristic function

Other getters inherited from the Vector class of the base_vector module.
"""

import numpy as np
import math
from psopackage.vector.base_vector import Vector
from psopackage.vector.position import Position

class Heuristic(Vector):
    """
    Represents a heuristic vector used in Particle Swarm Optimization.

    ## Parameters
    - dimensions : int, optional
        The number of dimensions of the vector. Default is 3.
    - heuristic : callable, optional
        The heuristic function used to calculate the heuristic value.
        Default is `default_heuristic`.

    ## Attributes
    - _color : dict
        The color of the vector (inherited).
    - _coordinates: np.ndarray
        The coordinates of the vector (inherited).
    - _dimensions : int
        The number of dimensions of the vector (inherited).
    - _heuristic : callable
        The heuristic function used to calculate the heuristic value.

    ## Methods
    - _update(self, position)
        Updates the vector based on the given position (overriden).
    - get_heuristic_f(self) -> callable
        Returns the heuristic function used by the vector.
    - Other getters and setters inherited.
    """

    def __init__(self, heuristic_f, dimensions=3):
        super().__init__(dimensions=dimensions)
        self._heuristic_f: callable = heuristic_f
    
    def _update(self, position: Position):
        """
        Updates the vector based on the given position and the 
        heuristic function

        ## Parameters
        position : Position
            The position object used to update the vector.
        """
        heuristic_value: Position = self._heuristic_f(position) # TODO: Static type to be defined
        # ? I think Position works
        new_coordinates: np.ndarray = self.get_coordinates().copy()
        for i in range(self.get_dimensions() - 1):
            new_coordinates[i] = position.get_coordinates().copy()[i]
        new_coordinates[self.get_dimensions() - 1] = heuristic_value
        self.set_coordinates(new_coordinates)
    
    def get_heuristic_f(self) -> callable:
        return self._heuristic_f

if __name__ == "__main__":
    h = Heuristic(3)
    h.initialize_randomly(10)
    print(h.get_coordinates())
    vect = Vector(2)
    vect.initialize_randomly(10)
    print(vect)
    h._update(vect)
    print(h.get_coordinates())