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
