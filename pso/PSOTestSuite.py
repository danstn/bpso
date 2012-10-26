#===============================================================================
# PSO Test functions
#===============================================================================

import numpy as np

# Square function
def square(vector):
    return np.multiply(vector, vector)

# Power function
def pow(vector, power):
    for i in range(power): 
        np.multiply(vector, vector)