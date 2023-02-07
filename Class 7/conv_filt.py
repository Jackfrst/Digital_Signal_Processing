import numpy as np
from matplotlib import pyplot as plt
from math import pi
def conv(x, h):
    N, M = x.shape[0], h.shape[0]
    L = N + M - 1
    y = np.zeros(L)
    for n in range(L):
        for k in range(N):
            if n - k >= 0 and n - k < M:
                y[n] += x[k] * h[n-k]
    return y

N = 50
n = np.array([_ for _ in range(N)])
x = np.cos((6 * pi * n) / N) + np.random.random(N)
h = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
y = conv(x, h)

plt.subplot(2, 1, 1)
plt.plot(x)
plt.subplot(2, 1, 2)
plt.plot(y)
plt.show()