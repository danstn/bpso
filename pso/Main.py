from Controllers import SwarmController
from Models import SwarmModel
import numpy as np

def square(vector):
	return np.multiply(vector, vector)

swarm = SwarmModel()
solution = square([2])
sc = SwarmController(solution)
sc.initSwarm(swarm)

for i in range(100):
	sc.updateSwarm(swarm)

print "Solution : %f BestPosition found : %f, BestPositionFitness %f" % (solution, swarm._nbBestPosition, swarm._nbBestPositionFitness)
