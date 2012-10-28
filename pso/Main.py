from Controllers import SwarmController
from Models import SwarmModel

from PSOTestSuite import *

#===============================================================================
# PROBLEM 1 SOLVING / PSO
#===============================================================================
print "Problem 1 Solving / CONTINUOUS"

# Problem parameters
solution 		= 750#pow([-3], 3)
numOfParticles 	= 50
dimensions 		= 1
generations		= 100
topology		= "lbest"

# Swarm Initialization
swarm = SwarmModel()
sc = SwarmController("continuous", solution)
sc.initSwarm(swarm, topology, numOfParticles, dimensions)

# Print
for i in range(generations):
	sc.updateSwarm(swarm)
	print "Generation", i+1,"\t-> BestPos:", swarm._bestPosition, "\tBestFitness:", swarm._bestPositionFitness

print (solution, swarm._bestPosition, swarm._bestPositionFitness)


#def binaryToDecimal(binaryArray):
#	result = 0
#	for i, bit in enumerate(binaryArray):
#		result += bit * np.power(2, i)
#	return result

#===============================================================================
# PROBLEM 2 SOLVING / BINARY
#===============================================================================

print "\n\nProblem 2 Solving / Binary"

# Problem parameters
#solution 		= pow([2], 2)
#solution = [1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#solution 		= [0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,1,1,1]
#solution 		= [1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
solution = [0,1,1,0]
popSize		 	= 50
dimensions 		= len(solution)
generations		= 10
topology		= "gbest"

# Swarm Initialization
swarm = SwarmModel()
sc = SwarmController("binary", solution)
sc.initSwarm(swarm, topology, popSize, dimensions)

# Print
fitness = 1
idx = 0
for i in range(generations):
	sc.updateSwarm(swarm)
	if swarm._bestPositionFitness < fitness:
		fitness = swarm._bestPositionFitness
		idx = i
	print "Generation", i+1,"\t-> BestPos:", swarm._bestPosition, "\tBestFitness:", swarm._bestPositionFitness

print "\n==================================================================="
print "Dimensions:\t", dimensions
print "Solution:\t", np.array(solution)
print "Best Result:\t", swarm._bestPosition
print "Best Fitness:\t", swarm._bestPositionFitness, "in %d" % idx, " iteration out of %d" % generations
print "Number of bits out of place: %d" % (dimensions * swarm._bestPositionFitness)
print "==================================================================="



