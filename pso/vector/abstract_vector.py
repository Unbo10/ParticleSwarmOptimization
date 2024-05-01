"""
A module to represent a vector as a data type with added functionality.
Contains only the class Vector.

### Classes

(class) Vector:
    A class to represent a vector in a n-dimensional space and
    facilitate its graphical representation.
"""

from typing import Any

import numpy as np

class Vector:
    """A class to represent a vector in a n-dimensional space and
    facilitate its graphical representation.
    
    ## Attributes
    __color : dict
        A dictionary with the values of the color of the vector.
    __coordinates : np.ndarray
        An array with the coordinates of the vector.
    _dimensions : int
        The number of dimensions of the vector.
    
    ## Methods
    initialize_randomly(bound: float = 10)
        Initialize the coordinates of a vector randomly within 
        the interval [-bound, bound].
    __lt__(other)
        Overriding of the less than operator. Compares two vectors depending on their norm.
    _update()
        Abstract method.
    
    Getters and setters
        get_color() -> dict
        get_coordinates() -> np.ndarray
        get_dimensions() -> int
        set_color(red: int, green: int, blue: int, alpha: int = 255)
        set_coordinates(coordinates: np.ndarray)
        set_dimensions(dimensions: int) 
        
    """
    
    def __init__(self, dimensions = 3) -> None:
        self._color: dict = {"R": 0, "G": 0, "B": 0, "A": 255}
        self._coordinates: np.ndarray = np.zeros(dimensions)
        self._dimensions: int = dimensions

    def __repr__(self) -> str:
        return f"Vector with coordinates {self.get_coordinates()} and color {list(self.get_color().values())}."
    
    def initialize_randomly(self, bound: float = 10) -> None:
        """Initialize the coordinates of a vector randomly within 
        the interval [-bound, bound].

        Parameters
        ---
        bound (float): 
            The maximum absolute value of the coordinates in all of its dimmensions.
        """
        self._coordinates = np.random.uniform(low=0, high=np.nextafter(bound, bound + 1), size=self._dimensions)

    def _update() -> None:
        """Abstract method"""
        raise NotImplementedError("This method must be implemented in a subclass.")
    
    def __lt__(self, other) -> bool:
        if not isinstance(other, Vector):
            raise TypeError("The object to compare must be a Vector. The provided object is of type {}.".format(type(other)))
        return np.linalg.norm(self._coordinates) < np.linalg.norm(other._coordinates)

    # * Getters and setters
    def get_color(self) -> dict:
        return self._color
    
    def get_coordinates(self) -> np.ndarray:
        return self._coordinates
    
    def get_dimensions(self) -> int:
        return self._dimensions
    
    def set_color(self, red: int, green: int, blue: int, alpha: int = 255) -> None:
        self._color = {"R": red, "G": green, "B": blue, "A": alpha}

    def set_coordinates(self, coordinates: np.ndarray) -> None:
        self.__coordinates = coordinates
    
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