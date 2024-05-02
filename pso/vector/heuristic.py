"""
This module provides a Heuristic class that represents a vector with a heuristic value.

## Classes
Heuristic: A class that represents a vector with a heuristic value.

### Methods
_update (position): Updates the vector based on the given position vector.

#### Getters
get_heuristic_f(): Returns the heuristic function
"""

import numpy as np

from pso.vector.abstract_vector import Vector
from pso.vector.position import Position

def default_heuristic(position: Vector) -> float:
    return np.sum(np.square(position.get_coordinates()))

class Heuristic(Vector):
    """
    Represents a heuristic vector used in Particle Swarm Optimization.

    ## Parameters
    dimensions : int, optional
        The number of dimensions of the vector. Default is 3.
    heuristic : callable, optional
        The heuristic function used to calculate the heuristic value.
        Default is `default_heuristic`.

    ## Attributes
    dimensions : int
        The number of dimensions of the vector.
    heuristic : callable
        The heuristic function used to calculate the heuristic value.

    ## Methods
    __init__(self, dimensions=3, heuristic=default_heuristic)
        Initializes a new instance of the Heuristic class.
    _update(self, position)
        Updates the vector based on the given position.
    get_heuristic_f(self)
        Returns the heuristic function used by the vector.
    """

    def __init__(self, dimensions=3, heuristic=default_heuristic):
        super().__init__(dimensions)
        self._heuristic_f = heuristic
    
    def _update(self, position):
        """
        Updates the vector based on the given position and the 
        heuristic function

        ## Parameters
        position : Position
            The position object used to update the vector.
        """
        heuristic_value = self._heuristic_f(position)
        new_coordinates = self.get_coordinates().copy()
        for i in range(self.get_dimensions() - 1):
            new_coordinates[i] = position.get_coordinates().copy()[i]
        new_coordinates[self.get_dimensions() - 1] = heuristic_value
        self.set_coordinates(new_coordinates)
    
    def get_heuristic_f(self):
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