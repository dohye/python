import numpy as np

def min_max_train_normalize(x):
    train_min = np.min(x, axis=0)
    train_max = np.max(x, axis=0)
    normalize = (x-train_min) / (train_max - train_min)
    return normalize, train_min, train_max


def min_max_test_normalize(test, train_min, train_max):
    return (test - train_min) / (train_max - train_min)


def return_scale(pred, min_max):
    
    train_min, train_max = min_max
    y_hat = pred * (train_max[0] - train_min[0]) + train_min[0]
    
    return y_hat
    
