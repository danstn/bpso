#===============================================================================
# @author: Daniel V. Stankevich
# @organization: RMIT, School of Computer Science, 2012
#
#
# This package contains different problems definitions
#  'PSOProblem'             - generic class for any problem
#  'CPSOProblem'            - continuous problem using standard PSO optimizer
#  'CBPSOProblem'           - continious problem using binary PSO optimizer
#  'BPSOKnapsackPromlem'    - Knapsack problem using BPSO optimizer
#  'BPSOTSPProblem'         - TSP problem using BPSO optimizer
#===============================================================================


#---- Required imports
from Models import *
from Controllers import *
from PSOTestSuite import *


#---- Generic PSO Problem
class PSOProblem(object):

    def __init__(self):
        pass
    
    def printResult(self):
        print "PSOProblem Result:"



#---- Continuous PSO Problem
class CPSOProblem(PSOProblem):

    def __init__(self):
        print "\nProblem Solving: Continuous"
        # Problem parameters
        solution1 = [42, 12, 490, -20]
        solution2 = [42]
        solution = solution2
        numOfParticles  = 50
        dimensions      = len(solution)
        generations     = 100
        topology        = "gbest"
        
        # Swarm Initialization
        swarm   = SwarmModel()
        sc      = SwarmController("continuous", solution)
        sc.initSwarm(swarm, topology, numOfParticles, dimensions)
        
        # Results Output
        for i in range(generations):
            print "Generation", i+1,"\t-> BestPos:", swarm._bestPosition, "\tBestFitness:", swarm._bestPositionFitness
            sc.updateSwarm(swarm)
        
#        print solution, swarm._bestPosition, swarm._bestPositionFitness

        print "\n==================================================================="
        print "Dimensions:\t", dimensions
        print "Solution:\t", np.array(solution)
        print "Best Result:\t", swarm._bestPosition
        print "Best Fitness:\t", swarm._bestPositionFitness
        print "==================================================================="


#---- Continuous Binary PSO Problem
class CBPSOProblem(PSOProblem):

    def __init__(self):
        print "\nProblem Solving: Binary"
        # Problem parameters
        solution1 = pow([2], 3)
        solution2 = [1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        solution3 = [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1]
        solution4 = [1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
        solution5 = [0, 1, 1, 0]
        solution  = solution2

        popSize     = 50
        dimensions  = len(solution)
        generations = 100
        topology    = "gbest"
        
        # Swarm Initialization
        swarm   = SwarmModel()
        sc      = SwarmController("binary", solution)
        sc.initSwarm(swarm, topology, popSize, dimensions)
        
        # Output Results
        fitness = 1
        idx = 0
        for i in range(generations):
            sc.updateSwarm(swarm)
            if swarm._bestPositionFitness < fitness:
                fitness = swarm._bestPositionFitness
                idx = i
            print "Generation", i+1,"\t-> BestPos:", swarm._bestPosition, "\tBestFitness:", 1 - swarm._bestPositionFitness
        
        print "\n==================================================================="
        print "Dimensions:\t", dimensions
        print "Solution:\t", np.array(solution)
        print "Best Result:\t", swarm._bestPosition
        print "Best Fitness:\t", 1 - swarm._bestPositionFitness, "in %d" % idx, " iteration out of %d" % generations
        print "Number of bits out of place: %d" % (dimensions * swarm._bestPositionFitness)
        print "==================================================================="
        
        
        
class BPSOKnapsackProblem(PSOProblem):

        __KNAPSACK_WEIGHTS_1 = [(4, 12), (2, 2), (2, 1), (10, 4), (1, 1)]
        
        def __init__(self):
            print "\nProblem Solving: Combinatorial - Knapsack"
            knapsackSize = 16
            solution = KnapsackSolutionModel(self.__KNAPSACK_WEIGHTS_1, knapsackSize)
            popSize     = 50
            dimensions  = len(solution._items)
            generations = 100
            topology    = "gbest"
            
            # Swarm Initialization
            swarm   = SwarmModel()
            sc      = SwarmController("knapsack", solution)
            sc.initSwarm(swarm, topology, popSize, dimensions)
            
            # Output Results
            fitness = 1
            idx     = 0
            
            for i in range(generations):
                sc.updateSwarm(swarm)
                if swarm._bestPositionFitness is not None and swarm._bestPositionFitness < fitness:
                    fitness = swarm._bestPositionFitness
                    idx = i
                print "Generation", i+1,"\t-> BestPos:", swarm._bestPosition, "\tBestFitness:", swarm._bestPositionFitness
            
            result = self.getKnapsackResult(solution._items, swarm._bestPosition)
            
            print "\n==================================================================="
            print "Number of weights:\t", dimensions, "\nKnapsackSize:\t\t", knapsackSize, " kg"
            print "Solution Found:\t\t(", result[0], "$,", result[1], "kg)"
            print "Best Result:\t\t", swarm._bestPosition, " -> ", result[2]
            print "Best Fitness:\t\t", swarm._bestPositionFitness, "in %d" % idx, "th iteration out of %d" % generations
            print "Size left in knapsack: \t%d kg" % (knapsackSize - result[1])
            print "==================================================================="
    
        def getKnapsackResult(self, items, bestPosition):
                res = ""
                curValue = 0
                curWeight = 0
                for idx, (price, weight) in enumerate(items):
                    if bestPosition[idx] == 1:
                        curValue += price
                        curWeight += weight
                        if idx != 0:
                            res += ", "
                        res += "(%d $$, %d kg)" % (price, weight)
                return (curValue, curWeight, res)



#---- TSP BPSO Problem
class BPSOTSPProblem(PSOProblem):
    
    __GRAPH_1 = { ("B", "A") : 1, ("B", "C") : 1, ("C", "A") : 1}
    __GRAPH_2 = { ("B", "A") : 1, ("B", "C") : 10, ("C", "A") : 1}
    __GRAPH_3 = { ("B", "A") : 1, ("B", "C") : 1, ("C", "D") : 1,  ("B", "D") : 1}
    __GRAPH_4 = { ("E", "A") : 1, ("D", "C") : 1, ("B", "D") : 1,  ("B", "C") : 1,  ("A", "B") : 1}
    __GRAPH_5 = { ("A", "B") : 1, ("A", "C") : 10, ("A", "D") : 1,  ("C", "D") : 1,  ("B", "C") : 1}
    __GRAPH_6 = { ("A", "Z") : 75, ("A", "S") : 140, ("Z", "O") : 71,  ("O", "S") : 151,  ("A", "T") : 118, ("S", "F") : 99, ("T", "L") : 111, ("F", "B") : 211, ("L", "M") : 70, ("D", "C") : 120, ("M", "D") : 75, ("S", "R") : 80, ("R", "C") : 146, ("C", "P") : 138, ("R", "P") : 97, ("P", "B") : 101, ("B", "G") : 90, ("B", "U") : 85, ("N", "I") : 87, ("U", "V") : 142, ("I", "V") : 92, ("E", "H") : 86, ("U", "H") : 98}
    
    def __init__(self):        
        print "\nProblem Solving: Combinatorial - TSP"
        graph       = self.generateFullGraph(self.__GRAPH_5)
        numOfCities = 4
        solution    = TSPSolutionModel(graph, numOfCities, "A")
        popSize     = 50
        dimensions  = len(solution._edges)
        generations = 100
        topology    = "gbest"
        
        # Swarm Initialization
        swarm   = SwarmModel()
        sc      = SwarmController("tsp", solution)
        sc.initSwarm(swarm, topology, popSize, dimensions)
        
        # Output Results
        fitness = 1000
        idx     = 0
        for i in range(generations):
            sc.updateSwarm(swarm)
            if swarm._bestPositionFitness is not None and swarm._bestPositionFitness < fitness:
                fitness = swarm._bestPositionFitness
                idx = i
            print "Generation", i+1,"\t-> BestPos:", swarm._bestPosition, "\tBestFitness:", swarm._bestPositionFitness
        
        print "\n==================================================================="
        print "Number of edges:\t", dimensions / 2, "\nNum of cities:\t\t", numOfCities
        if swarm._bestPositionFitness is not None:
            path = self.getTSPResult(solution, swarm._bestPosition)
            print "Best Result:\t\t", swarm._bestPosition, " Path: ", path
            print "Best Length:\t\t", swarm._bestPositionFitness, "in %d" % idx, " iteration out of %d" % generations
        else:
            print "Path was not found"
        print "==================================================================="   
        
        
    def generateFullGraph(self, graph):
        result = {}
        for (start, dest) in graph:
            result[(dest, start)] = graph[(start, dest)]
        graph.update(result)
        return graph

    def getTSPResult(self, solution, bestPosition):
        res         = ""
        curWeight   = 0
        curPath     = []
        pc = TSPParticleController(None)
        for idx, node in enumerate(solution._edges):
            if bestPosition[idx] == 1:
                curWeight += solution._edges[node]
                curPath.append(node)
        curPath = pc.orderSolution(curPath, solution._startNode)
        
        for idx, (start, dest) in enumerate(curPath):
            if idx == 0:
                res += start + " -> " + dest
            else:
                res += " -> %s" % dest
        return res