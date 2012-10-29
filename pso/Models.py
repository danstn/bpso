#===============================================================================
# This file contains representations of the following models:
#  'Particle' - an atomic 
#  'Swarm' - a set of particles
#===============================================================================


#---- Particle representation
class ParticleModel:
    _position       = None
    _velocity       = None
    _bestPosition   = None
    _nbBestPosition = None
    _fitness        = None

#---- Swarm representation
class SwarmModel:
    _particles      = []
    _neighbourhoods = []
    _bestPosition   = None
    _bestPositionFitness = None
    
class NeighbourhoodModel:
    _particles = []
    _bestPosition = None
    _bestPositionFitness = None
    
    def __init__(self, particles):
        self._particles = particles
        
class KnapsackSolutionModel:
    _items = []
    _knapsackSize = None
    
    def __init__(self, items, size):
        self._items = items
        self._knapsackSize = size

class TSPSolutionModel:
    _edges       = {}
    _startNode   = None
    _numOfCities = None
    _bestPath    = []
    
    def __init__(self, edges, numOfCities, startNode):
        self._edges = edges
        self._numOfCities = numOfCities
        self._startNode = startNode