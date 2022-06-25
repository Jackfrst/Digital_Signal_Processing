import numpy as np
from numpy.random import random
from math import pi
from matplotlib import pyplot as plt

N = 100
n = np.arange(0, 100, 1)
x = 4 * np.sin(2*pi*n / N)
x_ = x + random(N)
M = 10
x_padded = np.zeros(N+M)
for i in range(N):
	x_padded[i] = x_[i]
y = np.zeros(N)
for i in range(N):
	for j in range(M):
		y[i] = y[i] + x_padded[i + j]
	y[i] = y[i] / M

plt.subplot(2, 1, 1)
plt.plot(x_padded)
plt.subplot(2, 1, 2)
plt.plot(y)
plt.show()