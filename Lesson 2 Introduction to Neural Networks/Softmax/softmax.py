import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    sum = 0
    
    for v in L:
        sum = sum + np.exp(v)
    
    return [np.exp(v) / sum for v in L]