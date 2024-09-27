"""
A module to represent the position vector in a Particle Swarm
Optimization (PSO) algorithm.
The Position class inherits from the Vector class and provides
methods for updating the position based on the velocity vector.

## Classes
Position: Represents the position vector in a PSO algorithm.
Child of Vector.

Vector: Inherited from the base_vector module.

Velocity: Inherited from the velocity module.

### Methods
- _update(velocity): Updates the position based on the given velocity
vector.
- Other getters and setters inherited from the base_vector module.
"""

from psopackage.vector.base_vector import Vector
from psopackage.vector.velocity import Velocity 
import numpy as np

# ! Is a position vector really needed? Could  it be only a Heuristic?
class Position(Vector):
    """
    Represents the position of an object in a multi-dimensional space.

    ## Parameters
    - dimensions : int, optional
        The number of dimensions of the vector. Default is 3.

    ## Attributes
    - _color : dict
        The color of the vector (inherited).
    - _coordinates: np.ndarray
        The coordinates of the vector (inherited).
    - _dimensions : int
        The number of dimensions of the vector (inherited).
    - _coordinates : ndarray
        The coordinates of the position vector.

    ## Methods
    - _update(velocity)
        Updates the position by adding the coordinates of the given 
        velocity vector.
    - Other getters and setters inherited.
    """

    def __init__(self, dimensions: int = 3) -> None:
        super().__init__(dimensions)
    
    def _update(self, velocity: Velocity) -> None:
        # ? Should it be public?
        """
        Updates the position by adding the coordinates of the given
        velocity vector.

        ## Parameters

        - velocity : Velocity
            The velocity vector that contains the coordinates to be added to
            the position.
        """
        self._coordinates += velocity.get_coordinates()

if __name__ ==  "__main__":
    p = Position(3)
    p.initialize_randomly(1)
    print(p.get_coordinates())
    v = Velocity(3)
    v.initialize_randomly(1)
    print(v.get_coordinates())
    p._update(v)
    print(p.get_coordinates())