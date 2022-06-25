import numpy as np
from numpy.random import random
from math import pi
from matplotlib import pyplot as plt

def delta(n):
	if n == 0:
		return 1
	return 0

def system(M):
	N = x.shape[0]
	y = np.zeros(N)
	for i in range(N):
		for j in range(M):
			y[i] = y[i] + delta(i - j)
		y[i] = y[i] / M
	return y


N = 100
x = np.array([delta(n) for n in range(N)])
y = system(5)

plt.subplot(2, 1, 1)
plt.stem(x)
plt.subplot(2, 1, 2)
plt.stem(y)
plt.show()
