
import numpy as np
from scipy.special import factorial

#### Newton

def Newton_Raphson(y, x, init_value, tolerance_limit):
    
    n = len(y)
    lambda0 = init_value
    CRIT = 1
    result = list()
    
    for a in range(n):
        U = sum(y)/lambda0 - n
        I = sum(y)/(lambda0)**2
        lambda1 = lambda0 + U/I
        CRIT = np.abs(lambda0-lambda1)
        liklihood = sum(y*np.log(lambda0) - lambda0 - np.log(factorial(y,exact=False)))
        lambda0 = lambda1
        result.append([lambda0,U,I,liklihood])
        if CRIT < tolerance_limit:
            break
    
    return result

y = np.array([6,5,4,6,6,3,12,7,4,2,6,7,4])
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])    
result_Newton = Newton_Raphson(y, x, 4, 5E-08)


#### Fisher 

def Fisher_scoring(y, x, init_value, tolerance_limit):
    
    n = len(y)
    lambda0 = init_value
    CRIT = 1
    result = list()
    
    for a in range(n):
        U = sum(y)/lambda0 - n
        I = n/lambda0
        lambda1 = lambda0 + U/I
        CRIT = np.abs(lambda0-lambda1)
        liklihood = sum(y*np.log(lambda0) - lambda0 - np.log(factorial(y,exact=False)))
        lambda0 = lambda1
        result.append([lambda0,U,I,liklihood])
        if CRIT < tolerance_limit:
            break
    
    return result

y = np.array([6,5,4,6,6,3,12,7,4,2,6,7,4])
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])    
result_scoring = Fisher_scoring(y, x, 4, 5E-08)



