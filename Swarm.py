import numpy as np

class Particle:
	_position = np.array([])
	_velocity = np.array([])
	_bestPosition = np.array([])
	_nbBestPosition = np.array([])
	
	def __init__(self, dimensions):
		for i in range(dimensions):
			self._position = np.append(self._position, np.random.uniform(0, 100))
			self._velocity = np.append(self._velocity, np.random.uniform(0, 10))
			self._bestPosition = np.append(self._bestPosition, np.random.uniform(0, 100))

	def updatePosition(self):
# range Velocity with vMax
		c = 2.0
		e1 = np.random.rand()
		e2 = np.random.rand()
		for i, velocity in enumerate(self._velocity):
			velocity += c * e1 * (self._bestPosition[i] - self._position[i]) + c * e2 * (self._nbBestPosition[i] - self._position[i])
			self._position[i] += velocity
		

	def calculateFitness(self, solution):
		diff = np.subtract(self._position, solution)
		magnitude = np.linalg.norm(diff)
		return magnitude


class Swarm:

	_dimestion = 1
	_particles = []
	_bestSwarmPosition = None
	_fitnessFunction = None
	_solution = None

	def __init__(self, nParticles, dimension, fitnessFunction, solution):
		self._dimestion = dimension
		self._fitnessFunction = fitnessFunction
		self._solution = solution
		# create particles
		for i in range(nParticles):
			self._particles.append(Particle(self._dimestion))
		# find the best
		self.findSwarmBestPosition()
		# init nbest 
		for particle in self._particles:
			particle._nbBestPosition = self._bestSwarmPosition
			
	def findSwarmBestPosition(self):
		bestFitness = None
		for particle in self._particles:
			curFitness = particle.calculateFitness(self._fitnessFunction(self._solution))
#			print be
			if curFitness < bestFitness or bestFitness is None:
				bestFitness = curFitness
				self._bestSwarmPosition = particle._bestPosition

	# todo: ring topology
	def updateSwarm(self):
		for curParticle in self._particles:
			curParticle.updatePosition()
		self.findSwarmBestPosition()
			
####			

def square(vector):
	return np.multiply(vector, vector)
	
s = Swarm(1, 1, square, [100])
for i in range(200):
	s.updateSwarm()
	
print s._bestSwarmPosition