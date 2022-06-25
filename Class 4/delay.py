import numpy as np
from matplotlib import pyplot as plt
N = 7
x = np.array([1, 2, 3, 4, 3, 2, 1])
y = np.zeros(N)
k = 2
for n in range(N):
	t = n - k
	if t < 0:
		y[n] = 0
	else:
		y[n] = x[n - k]

plt.subplot(2, 1, 1)
plt.stem(x)
plt.subplot(2, 1, 2)
plt.stem(y)
plt.show()