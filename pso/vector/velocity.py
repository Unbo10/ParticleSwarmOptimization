"""
A module to represent the velocity vector in a Particle Swarm
Optimization (PSO) algorithm.
The Velocity class inherits from the Vector class and provides 
methods for updating the velocity based on the particle's best
position (pbest) and the global best position (gbest).

## Classes
Velocity: Represents the velocity vector in a PSO algorithm.
Child of Vector.

Vector: Inherited from the base_vector module.

### Methods
- _update(w, c1, c2, pbest, gbest): Updates the velocity
vector based on the given parameters.
- Other getters and setters inherited from the 
base_vector module.
"""

import numpy as np

from pso.vector.base_vector import Vector

class Velocity(Vector):
    """
    Represents the velocity vector in a particle swarm optimization
    algorithm.

    This class inherits from the Vector class and provides additional
    methods for updating the velocity based on the particle's best
    position (pbest) and the global best position (gbest).

    ## Parameters
    - dimensions : int, optional
        The number of dimensions of the velocity vector. Default is 3.

    ## Attributes
    - _coordinates : numpy.ndarray
        The coordinates of the velocity vector (inherited but redefined).
    - _color : dict
        The color of the velocity vector (inherited).
    - _dimensions : int
        The number of dimensions of the velocity vector (inherited).

    ## Methods
    - __repr__() -> str
        Overwrites the __repr__ method to return a string with the
        coordinates of the vector (inherited).
    - initialize_randomly(bound: float = 10)
        Initialize the coordinates of a vector randomly within 
        the interval [-bound, bound] (inherited).
    - Other getters and setters inherited.
    """

    def __init__(self, dimensions: int = 3) -> None:
        super().__init__(dimensions)
    
if __name__ ==  "__main__":
    v = Velocity(3)
    v.initialize_randomly(1)
    print(v.get_coordinates())
    # ! Correct
    # v._update(w=0.7, c1=2.05, c2=2.05, pbest=np.ndarray(np.array(3), ), gbest=Vector(3))
    print(v.get_coordinates())