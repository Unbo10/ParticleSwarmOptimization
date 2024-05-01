""""""

import numpy as np

from pso.vector.abstract_vector import Vector
from pso.swarm.particle import Particle

class ParticleSwarm:
    """
    Represents a particle swarm optimization algorithm.

    ## Parameters
    cognitive_coefficient : float
        The cognitive coefficient used in the particle update equation.
    inertia_coefficient : float
        The inertia coefficient used in the particle update equation.
    social_coefficient : float
        The social coefficient used in the particle update equation.
    dimensions : int
        The number of dimensions in the search space.
    particle_amount : int, optional
        The number of particles in the swarm (default is 10).

    ## Attributes
    __cognitive_coefficient : float
        The cognitive coefficient used in the particle update equation.
    __inertia_coefficient : float
        The inertia coefficient used in the particle update equation.
    __social_coefficient : float
        The social coefficient used in the particle update equation.
    __particle_amount : int
        The number of particles in the swarm.
    __particles : list[Particle]
        The list of particles in the swarm.
    __gbest : Vector
        The global best position found by the swarm.

    ## Methods
    _initialize_particles_randomly(bound=10)
        Initializes the positions and velocities of particles randomly.
    update_gbest()
        Updates the global best position found by the swarm.

    ### Getters
    get_cognitive_coefficient()
        Returns the cognitive coefficient.
    get_inertia_coefficient()
        Returns the inertia coefficient.
    get_social_coefficient()
        Returns the social coefficient.
    get_particle_amount()
        Returns the number of particles in the swarm.
    get_particles()
        Returns the list of particles in the swarm.
    get_gbest()
        Returns the global best position found by the swarm.
    """
    
    def __init__(self, cognitive_coefficient: float = 2, inertia_coefficient: float = 1, social_coefficient: float = 2, dimensions: int = 3, particle_amount: int = 10) -> None:
        self.__cognitive_coefficient: float = cognitive_coefficient
        self.__inertia_coefficient: float = inertia_coefficient
        self.__social_coefficient: float = social_coefficient
        try:
            self.__particle_amount: int = particle_amount
            if self.__particle_amount < 1:
                raise ValueError("The amount of particles must be greater than zero.")
        except ValueError as e:
            print(e)
            print("Amount defaulted to 10.")
            self.__particle_amount = 10
        # ? Should the following line be inside a finally block?
        self.__particles: list[Particle] = [Particle(dimensions) for _ in range(self.__particle_amount)]
        self.__gbest: Vector = self.__particles[0].get_position()
    
    def __repr__(self) -> str:
        return f"Particle swarm with {self.get_particle_amount()} particles, cognitive coefficient {self.get_cognitive_coefficient()}, inertia coefficient {self.get_inertia_coefficient()}, social coefficient {self.get_social_coefficient()} and global best position {self.get_gbest().get_coordinates()}."

    def _initialize_particle_randomly(self, bound: float = 10) -> None:
        for particle in self.__particles:
            particle.initialize_randomly(bound)

    # ? Should gbest be an instance of another class for it to have its own update method?
    def update_gbest(self) -> None:
        for particle in self.__particles:
            if particle.get_position() < self.__gbest:
                self.__gbest = particle.get_position()

    # * Getters (setters not necessary for now)

    def get_cognitive_coefficient(self) -> float:
        return self.__cognitive_coefficient
    
    def get_inertia_coefficient(self) -> float:
        return self.__inertia_coefficient
    
    def get_social_coefficient(self) -> float:
        return self.__social_coefficient
    
    def get_particle_amount(self) -> int:
        return self.__particle_amount
    
    def get_particles(self) -> list[Particle]:
        return self.__particles
    
    def get_gbest(self) -> Vector:
        return self.__gbest
    
if __name__ == "__main__":
    swarm = ParticleSwarm(1, 1, 1, 2, 5)
    swarm._initialize_particles_randomly(5)
    print(swarm.get_particles())
    print(swarm.get_gbest())
    swarm.update_gbest()
    print(swarm.get_gbest())
