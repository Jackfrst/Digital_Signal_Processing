import numpy as np
from math import pi, fabs, exp
from matplotlib import pyplot as plt
from numpy.random import random
from scipy.fftpack import fft, ifft, fftshift

N = 100
n = np.arange(0, N, 1)
x = np.cos((2 * pi * 4 * n) / N) + random(N)
a = 2 * N
x_p = np.zeros(a)
for n in range(N):
    x_p[n] = x[n]
H = np.zeros(a)
for n in range(a):
    H[n] = 1 / (1 + (fabs(n - N) / 30) ** 4)
H = 1 - H
X_p = fftshift(fft(x_p))
G_p = X_p * H
g_p = np.real(ifft(fftshift(G_p)))
g = np.zeros(N)
for n in range(N):
    g[n] = g_p[n]

plt.subplot(3, 1, 1)
plt.stem(np.abs(H))
plt.subplot(3, 1, 2)
plt.plot(x)
plt.subplot(3, 1, 3)
plt.plot(g)
plt.show()