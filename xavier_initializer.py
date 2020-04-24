"""
200324_initializer
"""

import numpy as np

def xavier_init(shape, uniform = True):
    if uniform:
        init_range = 4.0 * np.sqrt(6.0 / (np.sum(shape)))
        weights = np.random.uniform(low = - init_range, high = init_range, size = shape)
    
    else: # normal
        sigma = np.sqrt(2.0 / (np.sum(shape)))
        weights = np.random.normal(loc = 0, scale = sigma, size = shape)
        
    return weights

def normal_init(shape):
    return np.random.normal(size = shape)

xavier_init((2,3), uniform=True) # xavier uniform
xavier_init((2,3), uniform=False) # xavier normal
normal_init((2,3)) # noraml

