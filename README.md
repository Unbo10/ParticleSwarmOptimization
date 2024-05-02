# LaHerencia

``` mermaid
    classDiagram

    class Main{
        - int __dimensions
        - int __iterations
        - float __cognitive_coefficient
        - float __inertia_coefficient
        - float __social_coefficient
        - int __particle_amount
        - ParticleSwarm __swarm

        - heuristic(Position position)
        - optimize()
        - graph_heuristic(heuristic)
        - graph_particle(Particle)
        - get_cognitive_coefficient()
        - get_dimensions()
        - get_inertia_coefficient()
        - get_iterations()
        - get_social_coefficient()
        - get_particle_amount()
        - get_swarm()
    }

    Main o-- Vector
    Main --> ParticleSwarm : Uses

    class Vector {
        <!-- * Proposed class -->
        <!-- ! Since we need to use inheritance, we could consider each vector -velocity, heuristic and position-, to inherit from the vector class. I don't see many other classes were this could happen -->
        - np.ndarray _coordinates
        - dict _color
        <!-- * To distinguish between gbest and other particles -->
        - int _dimensions

        - initialize_randomly(float)
        - _update()
        - get_color() -> dict
        - get_coordinates() -> np.ndarray
        - get_dimensions() -> int
        - set_color(red: int, green: int, blue: int, alpha: int = 255)
        - set_coordinates(coordinates: np.ndarray)
        - set_dimensions(dimensions: int)  
    }


    class Velocity {
        - _update_velocity(velocity, gbest, cognitive_coefficient, social_coefficient, inertia, pbest, position, r_1, r_2) 
    }
    Velocity --|> Vector


    class Position{
        _update(Velocity: velocity)
    }
    Position --|> Vector
    Velocity --o Position

    class Heuristic{
        - callable heuristic
        - _update()
        - get_heuristic_f()
    }
    Heuristic --|> Vector

    class ParticleSwarm{
        - float __cognitive_coefficient
        - float __inertia_coefficient
        - float __social_coefficient
        - int __particle_amount
        - list[Particle] __particles
        - Position __gbest
        - callable _heuristic

        + _initialize_particles_randomly(int bound)
        + update_gbest(): None

        + get_cognitive_coefficient(): float
        + get_inertia(): float
        + get_social_coefficient(): float
        + get_particles_amount(): int
        + get_gbest(): Vector
        + get_particles: list[Particle]
        + get_heuristic(): callable

    }
    ParticleSwarm o-- Particle :The swarm contains Particles, but they can exist without the swarm (Aggreggation) 
    ParticleSwarm o-- Vector


    class Particle{
        <!-- ? Are r_1 and r_2 chosen for every iteration or at each iteration? -->
        - Heuristic __heuristic_value
        - Position __pbest
        - Position __position
        - Velocity __velocity

        - initialize_randomly(int bound)
        - update_heuristic(Vector)
        - update_position(position)
        - update_pbest(position)
        
        + get_position()
        + get_velocity()
        + get_pbest()
        + get_velocity()

        + set_position()
        + set_velocity()
        + set_pbest()
        + set_velocity()
    }
    Particle o-- Velocity
    Particle o-- Position
    ```
