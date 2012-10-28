from Models import SwarmModel
from Models import ParticleModel
from Models import NeighbourhoodModel
import scipy.spatial as spp

import numpy as np

#===============================================================================
# Particle controller
#===============================================================================
class BinaryParticleController:
    
    _solution = None
    
    def __init__(self, solution):
        self._solution = solution

    def initParticle(self, model, dimensions):
        # Create position array
        model._position = np.random.randint(2, size = dimensions)
        # Create Velocity array
        model._velocity = np.random.randint(2, size = dimensions)
        # Save best Position so far as current Position
        model._bestPosition = model._position
        self.updateFitness(model)

    def updateFitness(self, model):
        # Get Differences of vector
        hdist = spp.distance.hamming(model._position, self._solution)
        # Save it as best position if its better than previous best
        if hdist < model._fitness or model._fitness is None:
            model._bestPosition = np.copy(model._position)
            model._fitness = hdist

    def updatePosition(self, model):
        # VELOCITY NEEDS TO BE CONSTRICTED WITH VMAX
        # Get random coefficients e1 & e2
        c = 2.5
        e1 = np.random.rand()
        e2 = np.random.rand()
        vmax = 6
        # Apply equation to each component of the velocity, add it to corresponding position component
        for i, velocity in enumerate(model._velocity):
#            velocity = 0.72984 * (velocity + c * e1 * (model._bestPosition[i] - model._position[i]) + c * e2 * (model._nbBestPosition[i] - model._position[i]))
            velocity = velocity + c * e1 * (model._bestPosition[i] - model._position[i]) + c * e2 * (model._nbBestPosition[i] - model._position[i])
            if abs(velocity) > vmax and abs(velocity) is velocity: 
                velocity = vmax
            elif abs(velocity) > vmax:
                velocity = -vmax
            velocity = self.sigmoid(velocity)
#            print "vel:", velocity
            if np.random.rand(1) < velocity:
                model._position[i] = 1
            else:
                model._position[i] = 0
            
    def sigmoid(self, x):
        return 1.0/(1.0 + np.exp(-(x)))


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
            model._bestPosition = np.copy(model._position)
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
    _neighbourhoodController = None
    
    def __init__(self, type, solution):
        # Initialize ParticleController
        if type is "continuous":
            self._particleController = ParticleController(solution)
        else:
            self._particleController = BinaryParticleController(solution)            
        self._neighbourhoodController = NeighbourhoodController()
    
    def initSwarm(self, swarm, topology = "gbest" , nParticles = 1, dimensions = 1):
        # Create Swarm
        for i in range(nParticles):
            newParticle = ParticleModel()
            self._particleController.initParticle(newParticle, dimensions)
            swarm._particles.append(newParticle)    
        swarm._neighbourhoods = self._neighbourhoodController.initNeighbourhoods(swarm, topology)
        self.updateSwarmBestPosition(swarm)
            

    def updateSwarmBestPosition(self, swarm):
        # Find swarm best position and save it in swarm
        for nb in swarm._neighbourhoods:
            self._neighbourhoodController.updateNeighbourhoodBestPosition(nb)
            if swarm._bestPositionFitness is None or nb._bestPositionFitness < swarm._bestPositionFitness:
                swarm._bestPositionFitness = nb._bestPositionFitness
                swarm._bestPosition =  np.copy(nb._bestPosition)
    
    # Update all particles in the swarm 
    def updateSwarm(self, swarm):
        for curParticle in swarm._particles:
            self._particleController.updatePosition(curParticle)
            self._particleController.updateFitness(curParticle)
        self.updateSwarmBestPosition(swarm)
        
        
#===============================================================================
# Neighborhood Controller
#===============================================================================
class NeighbourhoodController:    

    def initNeighbourhoods(self, swarm, topology = "gbest"):
        if topology is "gbest":
            return [NeighbourhoodModel(swarm._particles)]
        elif topology is "lbest":
            neighbourhoods = []
            for idx, curParticle in enumerate(swarm._particles):
                previousParticle = None
                nextParticle = None
                if idx is 0:
                    # Previous is last, next is next
                    nextParticle = swarm._particles[idx + 1]
                    previousParticle = swarm._particles[len(swarm._particles) - 1]
                elif idx is len(swarm._particles) - 1:
                    # Previous is previous, next is first
                    nextParticle = swarm._particles[0]
                    previousParticle = swarm._particles[idx - 1]
                else:
                    # Previous is previous, next is next
                    nextParticle = swarm._particles[idx + 1]
                    previousParticle = swarm._particles[idx - 1]
                neighbourhoods.append(NeighbourhoodModel([previousParticle, curParticle, nextParticle]))
            return neighbourhoods

    def updateNeighbourhoodBestPosition(self, model):
        # Find the best one in the NB
        for curParticle in model._particles:
            if model._bestPositionFitness is None or curParticle._fitness < model._bestPositionFitness:
                model._bestPositionFitness = curParticle._fitness
                model._bestPosition = np.copy(curParticle._bestPosition)
        
        # Save nb best position in particles nbBestPosition 
        for curParticle in model._particles:
            curParticle._nbBestPosition = model._bestPosition
