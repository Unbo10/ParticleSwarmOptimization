"""
# TODO: Add doc to this module
"""

from pso.vector.heuristic import default_heuristic
from pso.swarm.particle import Particle
from pso.vector.position import Position

class ParticleSwarm:
    """
    Represents a particle swarm optimization algorithm.

    ## Parameters
    - inertia_coefficient : float, optional
        The inertia coefficient used in the particle update equation. Default is 1.
    - cognitive_coefficient : float, optional
        The cognitive coefficient used in the particle update equation. Default is 2.
    - social_coefficient : float, optional
        The social coefficient used in the particle update equation. Default is 2.
    - dimensions : int, optional
        The number of dimensions in the search space. Default is 3.
    - particle_amount : int, optional
        The number of particles in the swarm. Default is 10.
    - heuristic : callable, optional
        The heuristic function to be optimized. Default is the default_heuristic function
        imported from the heuristic module.

    ## Attributes
    - __inertia_coefficient : float
        The inertia coefficient used in the particle update equation.
    - __cognitive_coefficient : float
        The cognitive coefficient used in the particle update equation.
    - __social_coefficient : float
        The social coefficient used in the particle update equation.
    - __particle_amount : int
        The number of particles in the swarm.
    - __particles : list[Particle]
        The list of particles in the swarm.
    - __gbest : Vector
        The global best position found by the swarm.
    - _heuristic_f : callable
        The heuristic function to be optimized.

    ## Methods
    - __repr__() 
        Returns a string representation of the particle swarm (overridden).
    - _initialize_particles_randomly(bound=10)
        Initializes the positions and velocities of particles randomly.
    - update_gbest()
        Updates the global best position found by the swarm.

    ### Getters
    - get_inertia_coefficient() -> float
        Returns the inertia coefficient.
    - get_cognitive_coefficient() -> float
        Returns the cognitive coefficient.
    - get_social_coefficient() -> float
        Returns the social coefficient.
    - get_particle_amount() -> int
        Returns the number of particles in the swarm.
    - get_particles() -> list[Particle]
        Returns the list of particles in the swarm.
    - get_gbest() -> Vector
        Returns the global best position found by the swarm.
    - get_heuristic() -> callable
        Returns the heuristic function to be optimized.
    """
    
    def __init__(self, inertia_coefficient: float = 1, cognitive_coefficient: float = 2, social_coefficient: float = 2, dimensions: int = 3, particle_amount: int = 10, heuristic: callable = default_heuristic) -> None:
        self.__inertia_coefficient: float = inertia_coefficient
        self.__cognitive_coefficient: float = cognitive_coefficient
        self.__social_coefficient: float = social_coefficient
        try:
            self.__particle_amount: int = particle_amount
            if self.__particle_amount < 1:
                raise ValueError("The amount of particles must be greater than zero.") # ! Maybe include a TypeError to deal with floats
        except ValueError as e:
            print(e)
            print("Amount defaulted to 10.")
            self.__particle_amount = 10
        # ? Should the following line be inside a finally block?
        self.__particles: list[Particle] = [Particle(dimensions, heuristic) for _ in range(self.__particle_amount)]
        self.__gbest: Position = Position(dimensions - 1)
        self._heuristic_f: callable = heuristic
    
    def __repr__(self) -> str:
        return f"Particle swarm with {self.get_particle_amount()} particles, cognitive coefficient {self.get_cognitive_coefficient()}, inertia coefficient {self.get_inertia_coefficient()}, social coefficient {self.get_social_coefficient()} and global best position {self.get_gbest().get_coordinates()}."

    def _initialize_particles_randomly(self, bound: float = 10) -> None:
        """Calls the initialize_randomly method of each particle in the
        swarm and then updates the global best position (__gbest).
        
        ## Parameters
        bound : float
            The bound used to delimit the values of the particles' positions. Default is 10.
        """
        for particle in self.__particles:
            particle.initialize_randomly(bound)
        self.__gbest.set_coordinates(self.__particles[0].get_position().get_coordinates().copy())
        print("BBBB", self.__gbest.get_coordinates())
        self.update_gbest()

    # ? Should gbest be an instance of another class for it to have its own update method?
    def update_gbest(self) -> None:
        """Compares each particles' position (accessed through get_position()) 
        with the global best position (__gbest)"""
        for particle in self.__particles:
            dimensions: int = particle.get_position().get_dimensions() # ? Might be a better way to do it
            if particle.get_heuristic().get_coordinates()[dimensions] < self._heuristic_f(self.__gbest):
                self.__gbest.set_coordinates(particle.get_position().get_coordinates().copy())

    # * Getters (setters not necessary for now)

    def get_inertia_coefficient(self) -> float:
        return self.__inertia_coefficient

    def get_cognitive_coefficient(self) -> float:
        return self.__cognitive_coefficient
    
    def get_social_coefficient(self) -> float:
        return self.__social_coefficient
    
    def get_particle_amount(self) -> int:
        return self.__particle_amount
    
    def get_particles(self) -> list[Particle]:
        return self.__particles
    
    def get_gbest(self) -> Position:
        return self.__gbest
    
    def get_heuristic(self) -> callable:
        return self._heuristic_f

if __name__ == "__main__":
    swarm = ParticleSwarm(1, 1, 1, 2, 5)
    swarm._initialize_particles_randomly(5)
    print(swarm.get_particles())
    print(swarm.get_gbest())
    swarm.update_gbest()
    print(swarm.get_gbest())
