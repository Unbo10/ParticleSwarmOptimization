"""
A module to represent a vector as a data type with added functionality.
Contains the class Vector and its related attributes and methods.
It is intended to be an abstract class to be inherited by other classes.

## Classes
Vector: A class to represent a vector in a n-dimensional space and
    facilitate its graphical representation.

### Methods
- initialize_randomly(bound: float = 10): Initialize the coordinates of a
vector randomly within
- _update(): Abstract method.

#### Getters and setters
- get_coordinates() -> np.ndarray
- get_dimensions() -> int
- set_coordinates(coordinates: np.ndarray)
- set_dimensions(dimensions: int)

"""

from typing import Any

import numpy as np

class Vector:
    """A class to represent a vector in a n-dimensional space and
    facilitate its graphical representation.

    ## Parameters
    - dimensions : int
        The number of dimensions of the vector. Default is 3.
    
    ## Attributes
    - _coordinates : np.ndarray
        An array with the coordinates of the vector.
    - _dimensions : int
        The number of dimensions of the vector.
    
    ## Methods
    - __repr__() -> str
        Overwrites the __repr__ method to return a string with the
        coordinates of the vector.
    - initialize_randomly(bound: float = 10)
        Initialize the coordinates of a vector randomly within 
        the interval [-bound, bound].
    
    Getters and setters
    - get_color() -> dict
    - get_coordinates() -> np.ndarray
    - get_dimensions() -> int
    - set_color(red: int, green: int, blue: int, alpha: int = 255)
    - set_coordinates(coordinates: np.ndarray)
    - set_dimensions(dimensions: int) 
        
    """
    
    def __init__(self, dimensions = 3) -> None:
        self._coordinates: np.ndarray = np.zeros(dimensions)
        self._dimensions: int = dimensions

    def __repr__(self) -> str:
        return f"Vector with coordinates {self.get_coordinates()}."
    
    def initialize_randomly(self, bound: float = 10, dimensions: int = 2) -> None:
        """Initialize the coordinates of a vector randomly within 
        the interval [-bound, bound].

        ## Parameters
        bound (float): 
            The maximum absolute value of the coordinates in all of its dimmensions.
        """
        self._coordinates = np.random.uniform(low=-bound, high=np.nextafter(bound, bound + 1), size=dimensions)
    
    # def __lt__(self, other) -> bool:
    #     if not isinstance(other, Vector):
    #         raise TypeError("The object to compare must be a Vector. The provided object is of type {}.".format(type(other)))
    #     print(other.get_dimensions(), self._dimensions)
    #     return self._coordinates[self._dimensions - 1] < other._coordinates[self._dimensions - 1]

    # * Getters and setters
    
    def get_coordinates(self) -> np.ndarray:
        return self._coordinates
    
    def get_dimensions(self) -> int:
        return self._dimensions

    def set_coordinates(self, coordinates: np.ndarray) -> None:
        self._coordinates = coordinates
    
    def set_dimensions(self, dimensions: int) -> None:
        self._dimensions = dimensions
    
    # It is another option to access the attributes of the class, but it may
    # not be what we want to do since it violates private access
    # def __getattribute__(self, name: str) -> Any:
    #     attributes: dict = {
    #         "color": super().__getattribute__("_Vector_color"), 
    #         "coordinates": super().__getattribute__("_Vector_coordinates"), 
    #         "dimensions": super().__getattribute__("_Vector_dimensions")
    #     }
    #     if name in attributes:
    #         return attributes[name]
    #     else:
    #         return super().__getattribute__(name)
    
    # def __setattr__(self, name: str, value: Any) -> None:
    #     attributes: dict = {
    #         "color": "_Vector_color", 
    #         "coordinates": "_Vector_coordinates", 
    #         "dimensions": "_Vector_dimensions"
    #     }
    #     if name in attributes:
    #         super().__setattr__(attributes[name], value)
    #     else:
    #         super().__setattr__(name, value)
        
if __name__ == "__main__":
    vect1: Vector = Vector(3)
    print("Dimensions (set to 3):", vect1.get_dimensions())

    vect1.initialize_randomly(np.random.randint(1, 11))
    print("Coordinates randomly initialized:", vect1.get_coordinates())
    vect1.set_coordinates(np.array([1, 2, 3]))
    print("Coordinates set to [1, 2, 3]:", vect1.get_coordinates())

    red: int = np.random.randint(0, 256)
    green: int = np.random.randint(0, 256)
    blue: int = np.random.randint(0, 256)
    vect1.set_color(red, green, blue)
    print("Set random colors with default alpha:", vect1.get_color())