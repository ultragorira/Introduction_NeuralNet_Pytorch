import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.

def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    print (-np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P)))


cross_entropy([1, 1, 0], [0.8, 0.7, 0.1])