from BinaryControllers import SwarmController
from BinaryModels import SwarmModel

from PSOTestSuite import *
import numpy as np

def binaryToDecimal(binaryArray):
	result = 0
	for i, bit in enumerate(binaryArray):
		result += bit * np.power(2, i)
	return result

#===============================================================================
# PROBLEM 1 SOLVING
#===============================================================================

# Problem parameters
#solution 		= pow([2], 2)
#solution = [1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
solution 		= [0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,1,1,1]
#solution 		= [1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
popSize		 	= 50
dimensions 		= len(solution)
generations		= 100
topology		= "lbest"

# Swarm Initialization
swarm = SwarmModel()
sc = SwarmController(solution)
sc.initSwarm(swarm, topology, popSize, dimensions)

# Print
for i in range(generations):
	sc.updateSwarm(swarm)
	print "Generation", i+1,"\t-> BestPos:", swarm._bestPosition, "\tBestFitness:", swarm._bestPositionFitness

print "Solution:\t", np.array(solution)
print "Result:\t\t", swarm._bestPosition
print "Fitness:\t", swarm._bestPositionFitness
print "Dimensions:\t", dimensions

