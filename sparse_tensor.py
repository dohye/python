# sparse_tensor, tensorflow 2.0.0

import tensorflow as tf
indices = [[1,0],[1,1],[2,2],[3,1]]
values = [5,8,3,6]
dense_shape = [4,4]

# the sparse tensor
d2s = tf.sparse.SparseTensor(indices, values, dense_shape)

print(d2s)
"""
SparseTensor(
indices=tf.Tensor(
[[1 0]
 [1 1]
 [2 2]
 [3 1]], shape=(4, 2), dtype=int64), 
values=tf.Tensor([5 8 3 6], shape=(4,), dtype=int32), 
dense_shape=tf.Tensor([4 4], shape=(2,), dtype=int64))
"""

# represents the dense tensor

s2d = tf.sparse.to_dense(d2s)

print(s2d)
"""
tf.Tensor(
[[0 0 0 0]
 [5 8 0 0]
 [0 0 3 0]
 [0 6 0 0]], shape=(4, 4), dtype=int32)
"""
