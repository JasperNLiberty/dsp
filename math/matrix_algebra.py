# Matrix Algebra

import numpy as np

alpha = 6
A = [[1, 2, 3], [2, 7, 4]]
B = [[1, -1], [0, 1]]
C = [[5, -1], [9, 1], [6, 0]]
D = [[3, -2, -1], [1, 2, 3]]
u = [6, 2, -3, 5]
v = [3, 5, -1, 4]
w = [[1], [8], [0], [5]]

#2
print(np.add(u, v))
print(np.subtract(u, v))
print(np.multiply(alpha, u))
print(np.dot(u, v))
print(np.linalg.norm(u))

#3.3
print(np.add(np.matrix.transpose(np.array(C)), np.multiply(3, D)))

#3.4
print(np.dot(B,A))

#3.8
print(np.dot(np.dot(np.dot(B, B), B), B))
