import numpy as np

str0 = '몇시'
str1 = '지금은 한시'
len(str0)
len(str1)

def str2idx(string):
    
#    FIRST_INDEX = ord('가') - 1 # 44031
#    SPACE_INDEX = ord('힣') + 3 # 55206
#    SPACE_TOKEN = '<SPACE>'
    
    label = np.hstack([SPACE_TOKEN if x == ' ' else list(x) for x in string])
    
#    label = np.asarray([SPACE_INDEX - FIRST_INDEX if x == SPACE_TOKEN else ord(x) - FIRST_INDEX for x in label])
#    label = np.asarray([SPACE_INDEX if x == SPACE_TOKEN else ord(x) for x in label])
    label = np.asarray([char2idx[x] for x in label])
    
    return label

idx0 = str2idx(str0) # array([466,  29])
idx1 = str2idx(str1) # array([   8,  106,   15, 1206,   13,   29])

batch = [idx0, idx1]



def sparse_tuple_from(sequences, dtype = np.int32):
    """Create a sparse representation of x.
    Args:
        sequences : a list of lists of type dtype where each element is a sequence
    Returns:
        A tuple with (indices, values, shape)
    """
       
    indices = []
    values = []
    
    for n, seq in enumerate(sequences):
        
        indices.extend(zip([n]*len(seq), range(len(seq))))
        values.extend(seq)
        
    indices = np.asarray(indices, dtype = np.int64)
    values = np.asarray(values, dtype = dtype)
    shape = np.asarray([len(sequences), np.asarray(indices).max(0)[1]+1], dtype=np.int64)
    
    return indices, values, shape

indices, values, shape = sparse_tuple_from(batch)
print('indices:', indices)
print('values:', values)
print('shape:', shape)

"""
indices: 
[[0 0]
 [0 1]
 [1 0]
 [1 1]
 [1 2]
 [1 3]
 [1 4]
 [1 5]]
values: [ 466   29    8  106   15 1206   13   29]
shape: [2 6]
"""



def sparse_to_dense(indices, values, shape):

    s2d = np.zeros(shape, np.int32)

    for i in range(len(indices)):
        
        # indices[i] # shape : ex) indices[0] = [0,0], indices[1] = [0,1] 
        # s2d[indices[i][0], indices[i][1]] = values[i]
        
        s2d[tuple(indices[i])] = values[i]   
        
    return s2d

s2d = sparse_to_dense(indices, values, shape)
print(s2d)
"""
[[ 466   29    0    0    0    0]
 [   8  106   15 1206   13   29]]
"""
