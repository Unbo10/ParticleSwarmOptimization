# LaHerencia

``` mermaid
    classDiagram

    <!-- TODO: Figure out exaclty what the heuristic is: a vector, a function or a class-->

    class Test{
        - int dimensions
        <!-- ? Could this be defined inside a Heuristic class?>
        - int iterations
        - Vector heuristic 
        <!-- * function -->

        - start_test(heuristic, iterations)
        - graph_heuristic(heuristic)
        - graph_particle(Particle)
    }

    Test o-- Vector
    Test --> ParticleSwarm : Uses

    class Vector {
        <!-- * Proposed class -->
        <!-- ! Since we need to use inheritance, we could consider each vector -velocity, heuristic and position-, to inherit from the vector class. I don't see many other classes were this could happen -->
        - ~float~ coordinates
        - ~int~ color
        <!-- * To distinguish between gbest and other particles -->

        - initialize()

        + get_coordinates(): ~float~
    }

    class ParticleSwarm{
        - float cognitive_coefficient
        - float inertia
        - float social_coefficient
        - int particles_amount
        <!-- * Taken from class Test -->
        - ~Particle~ particles
        - Vector gbest

        - update_gbest(particles)

        + get_cognitive_coefficient(): float
        + get_inertia(): float
        + get_social_coefficient(): float
        + get_particles_amount(): int
        + get_gbest(): Vector

    }
    ParticleSwarm o-- Particle :The swarm contains Particles, but they can exist without the swarm (Aggreggation) 
    ParticleSwarm o-- Vector

    class Particle{
        - float r_1
        - float r_2
        <!-- ? Are r_1 and r_2 chosen for every iteration or at each iteration? -->
        - Vector heuristic
        <!-- ? Is this name okay? This is the vector that will define if a position is gbest or pbest, therefore 'rewarding' or 'punishing' each particle based on its position-->
        - Vector pbest
        - Vector position
        - Vector velocity

        - update_velocity(velocity, gbest, cognitive_coefficient, social_coefficient, inertia, pbest, position, r_1, r_2) 
        - update_heuristic(Vector) <!-- * Previously evaluate_function-->
        - update_position(position)
        - update_pbest(position)
        
        + get_position()
        + get_velocity()
        + get_pbest()

        + set_position()
        + set_velocity()
        + set_pbest()
    }
    Particle o-- Vector

    ```
