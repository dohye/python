"""
Label Error Rate(LER)
Reference : https://www.cs.toronto.edu/~graves/icml_2006.pdf
            https://lovit.github.io/nlp/2018/08/28/levenshtein_hangle/
"""

def LabelErrorRate(x,z, debug=False, jamo=False):
    
    if jamo:
        x, z = jamo_decompose(x), jamo_decompose(z)

    S = len(x)
    
    for i in range(len(x)):

        if jamo :
            ED = jamo_levenshtein(x[i], z[i])
        else:
            ED = levenshtein(x[i], z[i])
        
        mean_norm = sum(ED/len(z[i]))
        
        if debug : print("{}, {}, ED : {}".format(x[i] , z[i], ED))
    
    LER = mean_norm / S
    
    return LER
    
    
