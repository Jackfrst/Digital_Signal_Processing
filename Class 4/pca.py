import numpy as np
from numpy.linalg import svd
from matplotlib import pyplot as plt
from math import pi

X = np.zeros((10, 40))
n = np.arange(0, 40, 1)

for w in range(1, 11):
	X[w-1] = np.cos((2*pi*w) / 40 * n)

s = np.zeros(40)
for r in range(10):
	s = s + X[r]
s = s * (1 / 10)

C = np.zeros((40, 40))

for r in range(10):
	C = C + np.outer(X[r] - s, X[r] - s)
C = C * (1 / 10)

(U, S, V) = svd(C) #this is computation of eigen values and vectors

X_reduced = np.zeros((10, 20))
for r in range(10):
	X_reduced[r] = np.dot(X[r], V[0:20].T)

plt.subplot(2, 1, 1)
plt.stem(X[0])
plt.subplot(2, 1, 2)
plt.stem(X_reduced[0])
plt.show()