""""""
import numpy as np

from pso.swarm.particle import Particle
from pso.swarm.particle_swarm import ParticleSwarm
from pso.vector.position import Position

class Case:
    def __init__(self, dimensions: int = 3, iterations: int = 20) -> None:
        self.__dimensions: int = dimensions
        self.__iterations: int = iterations
        self.__swarm: ParticleSwarm = ParticleSwarm()

    def graph_heuristic(self) -> None:
        pass

    def graph_particles(self) -> None:
        pass
    
    def heuristic(self, position: Position) -> float:
        return np.sum(np.square(position.get_coordinates()))
    
    def optimize(self, cognitive_coefficient: float = 2, inertia_coefficient: float = 1, social_coefficient: float = 2, dimensions: int = 3, particle_amount: int = 10) -> None:
        self.__swarm = ParticleSwarm(cognitive_coefficient, inertia_coefficient, social_coefficient, dimensions, particle_amount)
        self.__swarm._initialize_particle_randomly()
        self.__swarm.update_gbest()

        for _ in range(self.__iterations):
            for particle in self.__swarm.get_particles():
                particle.get_velocity()._update(inertia_coefficient, cognitive_coefficient, social_coefficient, particle.get_pbest(), self.__swarm.get_gbest())
                particle.get_position()._update(particle.get_velocity())
                particle._update_pbest()
                print(particle, end="")
            self.__swarm.update_gbest()
            print(f"Global best: {self.__swarm.get_gbest()}\n")

    def get_swarm(self) -> ParticleSwarm:
        return self.__swarm

if __name__ == "__main__":
    case = Case(3, 5)
    case.optimize(2, 1, 2, 2, 10)
    print(case.get_swarm().get_gbest())
