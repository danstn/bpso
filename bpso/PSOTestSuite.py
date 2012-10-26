#===============================================================================
# PSO Test functions
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