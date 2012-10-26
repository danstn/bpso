from Models import SwarmModel
from Models import ParticleModel

import numpy as np

#===============================================================================
# Particle controller
#===============================================================================
class ParticleController:
    _solution = None
    
    def __init__(self, solution):
        self._solution = solution

    def initParticle(self, model, dimensions):
        # Create position array
        model._position = np.random.uniform(0, 10, dimensions)
        # Create Velocity array
        model._velocity = np.random.uniform(0, 1, dimensions)
        # Save best Position so far as current Position
        model._bestPosition = model._position
        self.updateFitness(model)

    def updateFitness(self, model):
        # Get Differences of vector
        diff = np.subtract(model._position, self._solution)
        # Get Norm of diff vector
        newFitness = np.linalg.norm(diff)
        # Save it as best position if its better than previous best
        if newFitness < model._fitness or model._fitness is None:
            model._bestPosition = model._position
            model._fitness = newFitness

    def updatePosition(self, model):
        # VELOCITY NEEDS TO BE CONSTRICTED WITH VMAX
        # Get random coefficients e1 & e2
        c = 2.0
        e1 = np.random.rand()
        e2 = np.random.rand()
        # Apply equation to each component of the velocity, add it to corresponding position component
        for i, velocity in enumerate(model._velocity):
            velocity = velocity + c * e1 * (model._bestPosition[i] - model._position[i]) + c * e2 * (model._nbBestPosition[i] - model._position[i])
            model._position[i] += velocity

#===============================================================================
# Swarm Controller
#===============================================================================
class SwarmController:    
    _particleController = None
    def __init__(self, solution):
        # Initialise ParticuleController
        self._particleController = ParticleController(solution)
    
    def initSwarm(self, swarm, nParticles = 1, dimensions = 1):
        # Create Swarm
        for i in range(nParticles):
            newParticle = ParticleModel()
            self._particleController.initParticle(newParticle, dimensions)
            swarm._particles.append(newParticle)    
        self.updateSwarmBestPosition(swarm)

    def updateSwarmBestPosition(self, swarm, topology = "gbest"):
        # Find swarm best position and save it in swarm
        if topology is "gbest":
            for curParticle in swarm._particles:
                if swarm._nbBestPositionFitness is None or curParticle._fitness < swarm._nbBestPositionFitness:
                    swarm._nbBestPositionFitness = curParticle._fitness
                    swarm._nbBestPosition = curParticle._bestPosition
            # Save swarms best position in particles nbBestPosition 
            for curParticle in swarm._particles:
                curParticle._nbBestPosition = swarm._nbBestPosition
        else:
            for idx, curParticle in enumerate(swarm._particles):
                previousParticle = None
                nextParticle = None
                if idx is 0:
                    # Previous is last, next is next
                    nextParticle = swarm._particles[idx + 1]
                    previousParticle = swarm._particles[len(swarm._particles - 1)]
                elif idx is len(swarm._particles) - 1:
                    # Previous is previous, next is first
                    nextParticle = swarm._particles[0]
                    previousParticle = swarm._particles[idx - 1]
                else:
                    # Previous is previous, next is next
                    nextParticle = swarm._particles[idx + 1]
                    previousParticle = swarm._particles[idx - 1]

                if nextParticle._fitness < curParticle._fitness and nextParticle._fitness < previousParticle._fitness:
                    # Next best than previous and current
                    curParticle.nbBestPosition = nextParticle._bestPosition
                elif previousParticle._fitness < curParticle._fitness and previousParticle._fitness < nextParticle._fitness:
                    # Previous is best than next and current
                    curParticle.nbBestPosition = previousParticle._bestPosition

    # Update all particles in the swarm 
    def updateSwarm(self, swarm):
        for curParticle in swarm._particles:
            self._particleController.updatePosition(curParticle)
            self._particleController.updateFitness(curParticle)
        self.updateSwarmBestPosition(swarm)
