import numpy as np


def closest(vecs, v,r):
    v_vecs=vecs[v]
    distnce=np.linalg.norm(vecs-v_vecs,axis=1)
    count=np.sum(distnce < r) -1
    return(count)


r = 2.5
v = 1
vecs = np.array([[1.0, 0.0, 2.0],
                 [-1.0, 0.5, 2.0],
                 [-2.0, 1.5, 0.0],
                 [2.5, -1.2, -0.5],
                 [1.5, 0.2, -0.2]
                 ]
                )
print(closest(vecs, v, r))  # Вернет 2
r = 0.1
v = 0
vecs = np.array([[0.71, 0.7, 0.22, 0.98, 0.01],
                 [0.25, 0.43, 0.78, 0.2, 0.86]])
vecs = np.array([[0.71, 0.7, 0.22, 0.98, 0.01]])


