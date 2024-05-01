""""""

import numpy as np

from pso.vector.abstract_vector import Vector

class Velocity(Vector):
    """
    Represents the velocity vector in a particle swarm optimization algorithm.

    This class inherits from the Vector class and provides additional methods
    for updating the velocity based on the particle's best position (pbest) and
    the global best position (gbest).

    Args:
        dimensions (int): The number of dimensions of the velocity vector. Default is 3.

    Attributes:
        _coordinates (numpy.ndarray): The coordinates of the velocity vector.

    Methods:
        _update(w, c1, c2, pbest, gbest): Updates the velocity vector based on the given parameters.

    """

    def __init__(self, dimensions: int = 3) -> None:
        super().__init__(dimensions)
    
    def _update(self, w: float, c1: float, c2: float, pbest: Vector, gbest: Vector) -> None:
        """
        Updates the velocity vector based on the given parameters.

        The velocity vector is updated using the particle swarm optimization formula:
        v = w * v + c1 * r1 * (pbest - v) + c2 * r2 * (gbest - v)

        Args:
            w (float): The inertia weight.
            c1 (float): The cognitive weight.
            c2 (float): The social weight.
            pbest (Vector): The particle's best position.
            gbest (Vector): The global best position.

        Returns:
            None

        """
        r1: float = np.random.random()
        r2: float = np.random.random()
        self._coordinates = w * self._coordinates + c1 * r1 * (pbest._coordinates - self._coordinates) + c2 * r2 * (gbest._coordinates - self._coordinates)
    
if __name__ ==  "__main__":
    v = Velocity(3)
    v.initialize_randomly(1)
    print(v.get_coordinates())
    v._update(w=0.7, c1=2.05, c2=2.05, pbest=Vector(3), gbest=Vector(3))
    print(v.get_coordinates())