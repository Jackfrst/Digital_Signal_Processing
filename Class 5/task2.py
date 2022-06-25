import numpy as np
from matplotlib import pyplot as plt
from math import pi, floor

n = np.arange(0, 69, 1)
N = n.shape[0]
x = 3 * np.cos((6*pi*n) / N + 2*pi / 10)

y_up = np.zeros(2*N)
y_down = np.zeros(floor(N/2))

for n in range(2*N):
    if n % 2 == 0:
        y_up[n] = x[int(n/2)]
        
for n in range(floor(N/2)):
    y_down[n] = x[2*n]

plt.subplot(3, 1, 1)
plt.stem(x)
plt.subplot(3, 1, 2)
plt.stem(y_down)
plt.subplot(3, 1, 3)
plt.stem(y_up)
plt.show()