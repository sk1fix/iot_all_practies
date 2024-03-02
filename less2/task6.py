import numpy as np


def nonzero(arr: np.ndarray):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]!=0:
                return i,j

A = np.zeros((100,100))
A[56,70] = 1
print(nonzero(A))
