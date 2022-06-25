import numpy as np
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
plt.stem(s)
plt.show()