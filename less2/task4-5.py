import numpy as np
A = np.array([[10, 1], [20, 2]])
x = np.sum(A, axis = 0)
print(x)


import numpy as np
I = np.eye(2)
A = np.array([[0, 1], [1, 0]])
2
x = np.sum( np.dot(A, I) )
y = np.sum( A * I )
print(x, y)
