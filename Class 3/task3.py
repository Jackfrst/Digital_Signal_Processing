import numpy as np
from matplotlib import pyplot as plt
from math import pi, pow

N = 40
z = 0.5 + 0.1j
mod_z = np.abs(z)
w = 6*pi / N
n = np.arange(0, N, 1)
x = np.exp(1j*w*n)

y = np.zeros(N)
for i in range(N):
	y[i] = pow(mod_z, n[i])

plt.subplot(3, 1, 1)
plt.stem(np.abs(x))
plt.subplot(3, 1, 2)
plt.stem(y)
plt.subplot(3, 1, 3)
plt.stem(np.abs(y*x))
plt.show()