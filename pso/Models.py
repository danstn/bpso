'''
Created on 26/10/2012

@author: cuva
'''
class ParticleModel:
    _position = None
    _velocity = None
    _bestPosition = None
    _nbBestPosition = None
    _fitness = None

class SwarmModel:
    _particles = []
    _nbBestPosition = None
    _nbBestPositionFitness = None
