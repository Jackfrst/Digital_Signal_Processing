import numpy as np

def solve(A, y):
	det = A[0, 0]*A[1, 1] - A[0, 1]*A[1, 0]
	Adj = np.zeros((2, 2))
	Adj[0, 0] = A[1, 1]
	Adj[0, 1] = -A[0, 1]
	Adj[1, 0] = -A[1, 0]
	Adj[1, 1] = A[0, 0]
	A_inv = Adj * (1 / det)
	return A_inv.dot(y)

A = np.array([[2, 3], [1, 2]])
y = np.array([1, 2])
x = solve(A, y)
print(x)
print(A.dot(x))