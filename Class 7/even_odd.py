import numpy as np
import matplotlib as mpt
from matplotlib import pyplot as plt
import scipy as sp

N = 50
x = np.zeros(50)
e = np.zeros(50)
o = np.zeros(50)

for i in range(N):
	x[i] = (i % 5) - 11

# x1 = np.flip(x)

for i in range(N):
	e[i] = 0.5*(x[i] + x[-i % N])

for i in range(N):
	o[i] = 0.5*(x[i] - x[-i % N])

x1 = e + o 

plt.subplot(2,2,1)
plt.stem(x)
plt.subplot(2,2,2)
plt.stem(x1)
plt.subplot(2,2,3)
plt.stem(e)
plt.subplot(2,2,4)
plt.stem(o)

plt.show()

