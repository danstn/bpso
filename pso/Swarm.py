import Particle

class Swarm:

	_particles = []
	_bestSwarmPosition = None

	def __init__(self, nbParticles):
		for nb in nbParticles:
			self._particles.append(Particle())
	
	def updateSwarm(self):

		bestFitness = 0
		for curParticle in self._particles:
			curParticle.update()
			curFitness = curParticle.calcutateFitness(None)
			if curFitness < bestFitness or bestFitness is 0:
				bestFitness = curFitness
				self._bestSwarmPosition = curParticle.bestPosition 
			
			

			
			

	