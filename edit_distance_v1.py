"""
Levenshtein Distance(=edit distance)

This version(edit_distance_v1) is to implement the algorithm's basic rules.
It is slower than edit_distance_v2

"""

import numpy as np

def EditDistance(s1, s2, debug = False):

    if len(s1) < len(s2):
        return EditDistance(s2, s1)
    
    if len(s2) == 0:
        return len(s1)
    
    d = np.zeros((len(s1),len(s2)))
    
    for i,c1 in enumerate(s1):
        for j,c2 in enumerate(s2):
            #print(i,j)
            
            if c1 == c2:
                sub_cost = 0
            else:
                sub_cost = 1
                
            if i == j == 0:
                d[i,j] = sub_cost
                
            elif i == 0 and j > 0:
                d[0,j] = d[0, j-1] + 1
            
            elif i > 0 and j == 0:
                d[i,0] = d[i-1, 0] + 1
            
            else:
                d[i,j] = min(d[i-1,j-1]  + sub_cost, 
                             d[i,j-1]  + 1, 
                             d[i-1,j] + 1)
    
    if debug == True:
        print(d.astype(np.int32))
        
    return d[-1][-1].astype(np.int32)
    
