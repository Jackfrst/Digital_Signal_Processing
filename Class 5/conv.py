import numpy as np
from matplotlib import pyplot as plt

n = np.arange(0, 49, 1)
M = 20
k = 4
N = n.shape[0]
x = np.zeros(N)
for n in range(M+1):
    x[n] = n

y1 = np.zeros(N)
y2 = np.zeros(N)

for n in range(N):
    if n - k < 0:
        y1[n] = 0
    else:
        y1[n] = x[n-k]

for n in range(N):
    if n + k >= N:
        y2[n] = 0
    else:
        y2[n] = x[n+k]

plt.subplot(3, 1, 1)
plt.stem(x)
plt.subplot(3, 1, 2)
plt.stem(y1)
plt.subplot(3, 1, 3)
plt.stem(y2)
plt.show()