import numpy as np
from matplotlib import pyplot as plt
from math import pi,pow

N = 50
n = np.arange(N)
x = 2*np.cos(6*pi*n/N) + np.random.random(N)

f = np.zeros((N, N))

for i in range(N):
    for j in range(N):
        f[i][j] = np.exp(-1j*2*pi*i*j/N)
        
X = f.dot(x)   

plt.subplot(1,1,1)
plt.stem(X)
plt.show()

     