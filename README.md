# LaHerencia

``` mermaid
classDiagram

    ParticleSwarm o-- Particle :The swarm contains Particles, but they can exist without the swarm (Aggreggation) 
    

    class Main{
        -float cognitive_coefficient
        -float social_coefficient
        -float inertia_weight_constant
        -ParticleSwarm swarm
        -function
        -int iterations
        -int dimension
        -int particles_number
        -PSO(cognitive_coefficient, social_coefficient, inertia_weight_constant, Swarm, function, iterations)
        -graph_group_best_by_iteration(group_best)
        -graph_function(function)
        -graph_particle_position(particle)

    }

    class ParticleSwarm{
      -list particles
      -list group_best
      -update_group_best(particles)

    }

    class Particle{
      -list position
      -list velocity
      -list personal_best
      -float r_1
      -float r_2
      -compute_new_velocity(velocity, group_best, cognitive_coefficient, social_coefficient, inertia_weight_constant, personal_best, position, r_1, r_2)
      -evaluate_function(position)
      -update_position(position)
      -update_personal_best(position)
    }

```
