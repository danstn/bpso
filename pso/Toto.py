from Controllers import *

list = [('B', 'A'), ('C', 'D'), ('D', 'B'), ('D', 'C'), ('A', 'B'), ('B', 'D')]
c = TSPParticleController(None)
result = c.orderSolution(list, "A")

print result
