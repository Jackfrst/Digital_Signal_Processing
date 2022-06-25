import numpy as np 
import matplotlib as mp
import scipy as sp  
from matplotlib import pyplot as plt
from numpy.random import random 
from math import pi , pow

N = 100
n = np.arange(100)
x = np.sin(2*pi*n / N)
x_ = x + random(N)
M = 10
x_padded = np.zeros(N+M)
for i in range(N):
	x_padded[i] = x_[i]

y = np.zeros(N)
for i in range(N):
	sum = 0
	for j in range(M):
		sum = sum + x_padded[i+j] 
	y[i] = (1/M) * sum

plt.subplot(3,1,1)
plt.plot(x)
plt.subplot(3,1,2)
plt.plot(x_padded)
plt.subplot(3,1,3)
plt.plot(y)
plt.show()
