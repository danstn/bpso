from Controllers import SwarmController
from Models import SwarmModel

from PSOTestSuite import *
from CodeWarrior.CodeWarrior_suite import target
from asyncore import write

#===============================================================================
# PROBLEM 1 SOLVING
#===============================================================================

# Problem parameters
solution 		= square([4])
numOfParticles 	= 50
dimensions 		= 1
populations		= 100

# Swarm Initialization
swarm = SwarmModel()
sc = SwarmController(solution)
sc.initSwarm(swarm, numOfParticles, dimensions)

# Print
for i in range(populations):
	print "\nGeneration", i+1
	print swarm._nbBestPosition, swarm._nbBestPositionFitness
	sc.updateSwarm(swarm)

print "Solution : %f BestPosition found : %f, BestPositionFitness %f" % (solution, swarm._nbBestPosition, swarm._nbBestPositionFitness)
