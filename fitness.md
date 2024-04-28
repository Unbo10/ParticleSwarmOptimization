# Fitness optimization
```python
import random
import numpy as np

class Particle:
    def __init__(self, position):
        self.position = position
        self.velocity = np.zeros_like(position)
        self.best_position = position
        self.best_fitness = float("inf")

class PSO:
    def __init__(self, D, maxT, objF, pop_size):
        self.D = D
        self.maxT = maxT
        self.objF = objF
        self.pop_size = pop_size

    def optimize(self):
        swarm_best_fitness = float("inf")
        swarm_best_position = None
        particles = []

        # Initialize particles
        for _ in range(self.pop_size):
            position = np.random.uniform(-0.5, 0.5, self.D)
            particle = Particle(position)
            particles.append(particle)

            fitness = self.objF(particle.position)

            # Update personal best
            if fitness < particle.best_fitness:
                particle.best_fitness = fitness
                particle.best_position = particle.position

            # Update global best
            if fitness < swarm_best_fitness:
                swarm_best_fitness = fitness
                swarm_best_position = particle.position

        # Iterations
        for _ in range(self.maxT):
            for particle in particles:
                w = 0.8
                c1 = 1.2
                c2 = 1.2
                r1 = random.random()
                r2 = random.random()

                # Update velocity and position
                particle.velocity = w * particle.velocity + c1*r1*(particle.best_position - particle.position) + c2*r2 * (swarm_best_position - particle.position)
                particle.position += particle.velocity

                fitness = self.objF(particle.position)

                # Update personal best
                if fitness < particle.best_fitness:
                    particle.best_fitness = fitness
                    particle.best_position = particle.position

                # Update global best
                if fitness < swarm_best_fitness:
                    swarm_best_fitness = fitness
                    swarm_best_position = particle.position

        return swarm_best_position, swarm_best_fitness

# Define function
def F1(x):
    return np.sum(x**2)

# Run PSO
pso = PSO(D=2, maxT=100, objF=F1, pop_size=10)
best_position, best_fitness = pso.optimize()

print("Best position: ", best_position)
print("Best fitness: ", best_fitness)
```
