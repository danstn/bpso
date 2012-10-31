#===============================================================================
# @author: Daniel V. Stankevich
# @organization: RMIT, School of Computer Science, 2012
#
# PSO Simple Test Functions
#===============================================================================

import numpy as np


# Square function
def square(vector):
    return np.multiply(vector, vector)


# Power function
def pow(vector, power):
    original = vector[:]
    for i in range(power-1): 
        vector = np.multiply(vector, original)
    return vector
