#===============================================================================
# @author: Daniel V. Stankevich
# @organization: RMIT, School of Computer Science, 2012
#
# Main Project Script
#===============================================================================


from PSOProblems import *

#cpsoProblem 	= CPSOProblem()
#cbpsoProblem 	= CBPSOProblem()
knapsackProblem = BPSOKnapsackProblem()
#tspProblem      = BPSOTSPProblem()

#
##===============================================================================
## PROBLEM 1 SOLVING / PSO
##===============================================================================
##print "Problem 1 Solving / CONTINUOUS"
##
### Problem parameters
##solution 		= 750#pow([-3], 3)
##numOfParticles 	= 50
##dimensions 		= 1
##generations		= 100
##topology		= "lbest"
##
### Swarm Initialization
##swarm = SwarmModel()
##sc = SwarmController("continuous", solution)
##sc.initSwarm(swarm, topology, numOfParticles, dimensions)
##
### Print
##for i in range(generations):
##	sc.updateSwarm(swarm)
##	print "Generation", i+1,"\t-> BestPos:", swarm._bestPosition, "\tBestFitness:", swarm._bestPositionFitness
##
##print (solution, swarm._bestPosition, swarm._bestPositionFitness)
#
##def binaryToDecimal(binaryArray):
##	result = 0
##	for i, bit in enumerate(binaryArray):
##		result += bit * np.power(2, i)
##	return result
#
##===============================================================================
## PROBLEM 2 SOLVING / BINARY
##===============================================================================
#
##print "\n\nProblem 2 Solving / Binary"
#
## Problem parameters
##solution 		= pow([2], 2)
##solution = [1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
##solution 		= [0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,1,1,1]
##solution 		= [1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
##solution = [0,1,1,0]
##popSize		 	= 50
##dimensions 		= len(solution)
##generations		= 10
##topology		= "gbest"
##
### Swarm Initialization
##swarm = SwarmModel()
##sc = SwarmController("binary", solution)
##sc.initSwarm(swarm, topology, popSize, dimensions)
##
### Print
##fitness = 1
##idx = 0
##for i in range(generations):
##	sc.updateSwarm(swarm)
##	if swarm._bestPositionFitness < fitness:
##		fitness = swarm._bestPositionFitness
##		idx = i
##	print "Generation", i+1,"\t-> BestPos:", swarm._bestPosition, "\tBestFitness:", swarm._bestPositionFitness
##
##print "\n==================================================================="
##print "Dimensions:\t", dimensions
##print "Solution:\t", np.array(solution)
##print "Best Result:\t", swarm._bestPosition
##print "Best Fitness:\t", swarm._bestPositionFitness, "in %d" % idx, " iteration out of %d" % generations
##print "Number of bits out of place: %d" % (dimensions * swarm._bestPositionFitness)
##print "==================================================================="
##===============================================================================
## PROBLEM 3 SOLVING / KNAPSACK
##===============================================================================
##
##print "\n\nProblem 3 Solving / Combinatorial"
##
##
##knapsackWeights = [(4, 12), (2, 2), (2, 1), (10, 4), (1, 1)]
##knapsackSize = 16
##solution = KnapsackSolutionModel(knapsackWeights, knapsackSize)
##
##popSize		 	= 10
##dimensions 		= len(solution._items)
##generations		= 100
##topology		= "gbest"
##
### Swarm Initialization
##swarm = SwarmModel()
##sc = SwarmController("knapsack", solution)
##sc.initSwarm(swarm, topology, popSize, dimensions)
##
### Print
##fitness = 1
##idx = 0
###
##def getKnapsackResult(items, bestPosition):
##	res = ""
##	curValue = 0
##	curWeight = 0
##	for idx, (price, weight) in enumerate(items):
##		if bestPosition[idx] == 1:
##			curValue += price
##			curWeight += weight
##			if idx != 0:
##				res += ", "
##			res += "(%d $$, %d kg)" % (price, weight)
##	return (curValue, curWeight, res)
##
##for i in range(generations):
##	sc.updateSwarm(swarm)
##	if swarm._bestPositionFitness is not None and swarm._bestPositionFitness < fitness:
##		fitness = swarm._bestPositionFitness
##		idx = i
##	print "Generation", i+1,"\t-> BestPos:", swarm._bestPosition, "\tBestFitness:", swarm._bestPositionFitness
##
##result = getKnapsackResult(solution._items, swarm._bestPosition)
##
##print "\n==================================================================="
##print "Number of weights:\t", dimensions, "\nKnapsackSize:\t\t", knapsackSize, " kg"
##print "Solution Found:\t\t(", result[0], "$,", result[1], "kg)"
##print "Best Result:\t\t", swarm._bestPosition, " -> ", result[2]
##print "Best Fitness:\t\t", swarm._bestPositionFitness, "in %d" % idx, "th iteration out of %d" % generations
##print "Size left in knapsack: \t%d kg" % (knapsackSize - result[1])
##print "==================================================================="
#
#
#
#
##===============================================================================
## PROBLEM 4 SOLVING / TSP
##===============================================================================
#
#print "\n\nProblem 4 Solving / Combinatorial - TSP"
#
#def generateFullGraph(graph):
#	result = {}
#	for (start, dest) in graph:
#		result[(dest, start)] = graph[(start, dest)]
#	graph.update(result)
#	return graph
#
##graph = [(4, 12), (2, 2), (2, 1), (10, 4), (1, 1)]
#
## g0
#graph0 = { ("B", "A") : 1, ("B", "C") : 1, ("C", "A") : 1} 	
## g1
#graph1 = { ("B", "A") : 1, ("B", "C") : 10, ("C", "A") : 1} 
## g2
#graph2 = { ("B", "A") : 1, ("B", "C") : 1, ("C", "D") : 1,  ("B", "D") : 1} 
## g3
#graph3 = { ("E", "A") : 1, ("D", "C") : 1, ("B", "D") : 1,  ("B", "C") : 1,  ("A", "B") : 1} 
## g4
#graph4 = { ("A", "B") : 1, ("A", "C") : 1, ("A", "D") : 1,  ("A", "E") : 1} 
## g5
#graph5 = { ("A", "B") : 1, ("A", "C") : 10, ("A", "D") : 1,  ("C", "D") : 1,  ("B", "C") : 1} 
## g6
#graph6 = { ("A", "Z") : 75, ("A", "S") : 140, ("Z", "O") : 71,  ("O", "S") : 151,  ("A", "T") : 118, ("S", "F") : 99, ("T", "L") : 111, ("F", "B") : 211, ("L", "M") : 70, ("D", "C") : 120, ("M", "D") : 75, ("S", "R") : 80, ("R", "C") : 146, ("C", "P") : 138, ("R", "P") : 97, ("P", "B") : 101, ("B", "G") : 90, ("B", "U") : 85, ("N", "I") : 87, ("U", "V") : 142, ("I", "V") : 92, ("E", "H") : 86, ("U", "H") : 98} 															
#
#
#graph = generateFullGraph(graph6)
#numOfCities = 20
#
#solution = TSPSolutionModel(graph, numOfCities, "A")
#
#popSize		 	= 1000
#dimensions 		= len(solution._edges)
#generations		= 1000
#topology		= "gbest"
#
## Swarm Initialization
#swarm = SwarmModel()
#sc = SwarmController("tsp", solution)
#sc.initSwarm(swarm, topology, popSize, dimensions)
#
## Print
#fitness = 1000
#idx = 0
#
#def getTSPResult(solution, bestPosition):
#	res = ""
#	curWeight = 0
#	curPath   = []
#	pc = TSPParticleController(None)
#	for idx, node in enumerate(solution._edges):
#		if bestPosition[idx] == 1:
#			curWeight += solution._edges[node]
#			curPath.append(node)
#	curPath = pc.orderSolution(curPath, solution._startNode)
#	
#	for idx, (start, dest) in enumerate(curPath):
#		if idx == 0:
#			res += start + " -> " + dest
#		else:
#			res += " -> %s" % dest
#	return res
#
#for i in range(generations):
#	sc.updateSwarm(swarm)
#	if swarm._bestPositionFitness is not None and swarm._bestPositionFitness < fitness:
#		fitness = swarm._bestPositionFitness
#		idx = i
#	print "Generation", i+1,"\t-> BestPos:", swarm._bestPosition, "\tBestFitness:", swarm._bestPositionFitness
#
#print "\n==================================================================="
#print "Number of edges:\t", dimensions / 2, "\nNum of cities:\t\t", numOfCities
#if swarm._bestPositionFitness is not None:
#	path = getTSPResult(solution, swarm._bestPosition)
#	print "Best Result:\t\t", swarm._bestPosition, " Path: ", path
#	print "Best Length:\t\t", swarm._bestPositionFitness, "in %d" % idx, " iteration out of %d" % generations
#else:
#	print "Path was not found"
#print "==================================================================="
#
