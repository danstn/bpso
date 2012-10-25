import numpy
import Swarm

class Particle:
    _position = None
    _velocity = None
    _bestPosition = None

    _test = Swarm()
    
    def __init__(self):
        _position = numpy.random.uniform(0, 100)
        _velocity = numpy.random.uniform(0, 10)


    def update(self):
        pass
    
    def updatePosition(self):
        i = 0

        # range Velocity with vMax

        for item in self._velocity:
            self._position[i] += item;
            ++i

    def calculateFitness(self, func):
        pass
