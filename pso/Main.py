from Controllers import SwarmController
from Models import SwarmModel

from PSOTestSuite import *

#===============================================================================
# PROBLEM 1 SOLVING
#===============================================================================

# Problem parameters
solution 		= 750#pow([-3], 3)
numOfParticles 	= 50
dimensions 		= 1
generations		= 100
topology		= "lbest"

# Swarm Initialization
swarm = SwarmModel()
sc = SwarmController(solution)
sc.initSwarm(swarm, topology, numOfParticles, dimensions)

# Print
for i in range(generations):
	sc.updateSwarm(swarm)
	print "Generation", i+1,"\t-> BestPos:", swarm._bestPosition, "\tBestFitness:", swarm._bestPositionFitness

print (solution, swarm._bestPosition, swarm._bestPositionFitness)

