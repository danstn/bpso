#===============================================================================
# @author: Daniel V. Stankevich
# @organization: RMIT, School of Computer Science, 2012
#
#
# This package contains representations of the following models:
#  'Particle'            - an atomic element
#  'Swarm'               - a set of particles
#  'Neighbourhood'       - particles topology
#  'KnapsackSolution'    - representation for solution of the problem
#  'TSPSolution'         - representation for solution of the problem
#===============================================================================



#===============================================================================
#                             GENERIC MODELS
#===============================================================================

#---- Particle representation
class ParticleModel:
    _position       = None
    _velocity       = None
    _bestPosition   = None
    _nbBestPosition = None
    _fitness        = None

    def __init__(self):
        self._position       = None
        self._velocity       = None
        self._bestPosition   = None
        self._nbBestPosition = None
        self._fitness        = None

#---- Swarm representation
class SwarmModel:
    _particles              = None
    _neighbourhoods         = None
    _bestPosition           = None
    _bestPositionFitness    = None
    
    def __init__(self):
        self._particles = []
        self._neighbourhoods        = None
        self._bestPosition          = None
        self._bestPositionFitness   = None
        

#---- Neighbourhood representation    
class NeighbourhoodModel:
    _particles              = []
    _bestPosition           = None
    _bestPositionFitness    = None
    
    def __init__(self, particles):
        self._particles             = particles
        self._bestPosition          = None
        self._bestPositionFitness   = None


#===============================================================================
#                            PROBLEM SPECIFIC MODELS
#===============================================================================

#---- Knapsack Problem Solution representation        
class KnapsackSolutionModel:
    _items          = [] 
    _knapsackSize   = None
    
    def __init__(self, items, size):
        self._items = items
        self._knapsackSize = size

#---- TSP Problem Solution representation
class TSPSolutionModel:
    _edges       = {}
    _startNode   = None
    _numOfCities = None
    _bestPath    = []
    
    def __init__(self, edges, numOfCities, startNode):
        self._edges = edges
        self._numOfCities = numOfCities
        self._startNode = startNode