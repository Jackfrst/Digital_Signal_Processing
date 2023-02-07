import numpy as np
from math import pi, fabs, exp
from matplotlib import pyplot as plt
from numpy.random import random

def dft(x):
    N = x.shape[0]
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp((-1j*2*pi*n*k) / N)
    return X

def idft(x):
    N = x.shape[0]
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp((1j*2*pi*n*k) / N)
    return (1 / N) * X

N = 100
n = np.arange(0, N, 1)
x = np.cos((2 * pi * 4 * n) / N) + random(N)
h = np.array([1 / 10 for n in range(10)])
M = 10
a = M + N - 1
x_p = np.zeros(a)
h_p = np.zeros(a)

for n in range(N):
    x_p[n] = x[n]
for n in range(M):
    h_p[n] = h[n]

X_p = dft(x_p)
H_p = dft(h_p)
G_p = X_p * H_p
g_p = np.real(idft(G_p))
g = np.zeros(N)

for n in range(N):
    g[n] = g_p[n]

plt.subplot(3, 1, 1)
plt.stem(h_p)
plt.subplot(3, 1, 2)
plt.plot(x_p)
plt.subplot(3, 1, 3)
plt.plot(g)
plt.show()