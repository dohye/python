"""
x, z : strings
"""

def WordErrorRate(x, z, debug=False):
        
    S = len(x)
    for i in range(len(x)):
        
        x_word, z_word = x[i].split(), z[i].split()
        ED = levenshtein(x_word, z_word)
            
        mean_norm = sum(ED/len(z_word))

        if debug : print("{}, {}, ED : {}".format(x_word, z_word, ED))
        
    WER = mean_norm / S
    
    return WER
    
