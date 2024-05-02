""""""
import numpy as np

from pso.swarm.particle import Particle
from pso.swarm.particle_swarm import ParticleSwarm
from pso.vector.position import Position

# ! Check initialization of particles: might be done more than once

class Main:
    def __init__(self, dimensions: int = 3, iterations: int = 20) -> None:
        self.__dimensions: int = dimensions
        self.__iterations: int = iterations
        self.__swarm: ParticleSwarm = ParticleSwarm()

    def graph_heuristic(self) -> None:
        pass

    def graph_particles(self) -> None:
        pass
    
    def heuristic(self, position: Position) -> float:
        """Heuristic function to be optimized."""
        return np.sum(np.square(position.get_coordinates()))
    
    def optimize(self, cognitive_coefficient: float = 2, inertia_coefficient: float = 1, social_coefficient: float = 2, particle_amount: int = 10) -> None:
        self.__swarm = ParticleSwarm(cognitive_coefficient, inertia_coefficient, social_coefficient, self.__dimensions, particle_amount, self.heuristic)
        self.__swarm._initialize_particles_randomly()
        self.__swarm.update_gbest()

        for _ in range(self.__iterations):
            for particle in self.__swarm.get_particles():    
                particle.get_velocity()._update(inertia_coefficient, cognitive_coefficient, social_coefficient, particle.get_position().get_coordinates().copy(), particle.get_pbest().get_coordinates().copy(), self.__swarm.get_gbest().get_coordinates().copy())

                particle.get_position()._update(particle.get_velocity())
                particle.get_heuristic()._update(particle.get_position())
                particle._update_pbest()
                print(particle, end="")
            self.__swarm.update_gbest()
            print(f"Global best: {self.__swarm.get_gbest()}\n")

    def get_swarm(self) -> ParticleSwarm:
        return self.__swarm

def run():
    pass

if __name__ == "__main__":
    main = Main(2, 20)
    main.optimize(1.2, 0.5, 1.2, 20)
    print(main.get_swarm().get_gbest())
