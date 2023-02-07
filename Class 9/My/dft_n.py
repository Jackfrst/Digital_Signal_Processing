import numpy as np
from matplotlib import pyplot as plt
from math import pi,fabs,exp

def dft(x):
    N = x.shape[0]
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] +=  x[n] * np.exp((-1j*2*pi*k*n)/N)  
    return X

def in_dft(x):
    N = x.shape[0]
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += 1/N * x[n] * np.exp((1j*2*pi*k*n)/N)  
    return X
        

N = 100
n = np.arange(N)
x = np.cos((2*pi*4*n)/N)

X = dft(x)
X_ = in_dft(X)

plt.subplot(3,1,1)
plt.stem(x)
plt.subplot(3,1,2)
plt.stem(np.abs(X))
plt.subplot(3,1,3)
plt.stem(X_)
plt.show()