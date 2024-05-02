""""""

import numpy as np

from pso.vector.abstract_vector import Vector
from pso.vector.position import Position

def default_heuristic(position: Vector) -> float:
    return np.sum(np.square(position.get_coordinates()))

class Heuristic(Vector):
    def __init__(self, dimensions: int = 3, heuristic: callable = default_heuristic) -> None:
        super().__init__(dimensions)
        self._heuristic_f: callable = heuristic
    
    def _update(self, position: Position) -> None:
        heuristic_value: float = self._heuristic_f(position)
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