# LaHerencia

``` mermaid
    classDiagram
    direction TB

    class Main{
        - float cognitive_coefficient
        - int dimensions
        - float inertia_coefficient
        - int iterations
        - int particle_amount
        - float social_coefficient
        - ParticleSwarm swarm

        - graph_heuristic(heuristic)
        - graph_particle(Particle)
        - heuristic(Position position)
        - optimize()

        - get_cognitive_coefficient()
        - get_dimensions()
        - get_inertia_coefficient()
        - get_iterations()
        - get_social_coefficient()
        - get_particle_amount()
        - get_swarm()
    }
    Main --o ParticleSwarm
    Main --o Data

    class Data {
        - ~~~float/str~~~ history
        <!-- * Contains three pd.DataFrame, corresponding to the last three attempts -->
        <!-- ? Should it be the last three attempts or the last n-attempts? -->
        <!-- ! Before creating any .xslx file it should check for existent ones and change the file's name if that happens. -->
    }

    class ParticleSwarm{
        - float cognitive_coefficient
        - float inertia_coefficient
        - float social_coefficient
        - int particle_amount
        - list[Particle] particles
        - Position gbest
        + callable heuristic_f

        - __repr__() : str
        # initialize_particles_randomly(int bound)
        + update_gbest(): None

        + get_cognitive_coefficient(): float
        + get_inertia(): float
        + get_social_coefficient(): float
        + get_particles_amount(): int
        + get_gbest(): Vector
        + get_particles(): ~Particle~
        + get_heuristic(): callable
    }
    ParticleSwarm o-- Particle

    class Particle{
        <!-- ? Are r_1 and r_2 chosen for every iteration or at each iteration? -->
        + dict color
        - Heuristic heuristic
        - Position pbest
        - Position position
        - Velocity velocity

        # update_pbest(position)
        + initialize_randomly(int bound)
        
        + get_pbest()
        + get_position()
        + get_velocity()

        + set_pbest()
        + set_position()
        + set_velocity()
    }
    Particle o-- Heuristic
    Particle o-- Position
    Particle o-- Velocity


    class Vector {
        # np.ndarray coordinates
        # int dimensions

        - __repr__() : str
        + initialize_randomly(float)
        # update()
        
        + get_color() : dict
        + get_coordinates() : np.ndarray
        + get_dimensions() : int
        + set_color(red: int, green: int, blue: int, alpha: int = 255)
        + set_coordinates(coordinates: np.ndarray)
        + set_dimensions(dimensions: int)  
    }

    class Heuristic{
        <!-- ? Should the inherited attributes be kept in the child class?-->
        <!-- ? Should ndarrays be simply called arrays since the fact they are np has to do more with the implementation? -->
        # callable heuristic
        # update()
        + get_heuristic_f()
    }
    Heuristic --|> Vector

    class Position{
        # update(Velocity: velocity)
    }
    Position --|> Vector

    class Velocity {
        # update_velocity(velocity, gbest, cognitive_coefficient, social_coefficient, inertia, pbest, position, r_1, r_2) 
    }
    Velocity --|> Vector

    ```
