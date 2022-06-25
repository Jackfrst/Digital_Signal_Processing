import numpy as np
import scipy.linalg as spli

def poly_interpolate(t, a):
	v0 = 0
	for i in range(4):
		v0 = v0 + (a[i] * (t ** i))
	return v0

A = [[1, 0, 0, 0], [1, 10, 10**2, 10**3], [1, 15, 15**2, 15**3], [1, 25, 25**2, 25**3]]
A = np.array(A)
v = np.array([0, 32, 40, 60])
a = spli.solve(A, v)
print(a)
print(poly_interpolate(20, a))