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
            X[k] += x[n] * np.exp((1j*2*pi*k*n)/N)  
    return (1/N *X)

      
N = 100
n = np.arange(N)
x = np.cos((2*pi*4*n)/N) + np.random.random(N)
M = 5
h = np.array([1/M for n in range(M)])
a = N + M - 1
X = dft(x)
X_ = in_dft(X)
x_p = np.zeros(a)
h_p = np.zeros(a)

for n in range(N):
    x_p[n] = x[n]
for n in range(N):
    h_p[n] = h[n]

X_p = dft(x_p)    
H_p = dft(h_p)
G_p = X_p * H_p
g_p = np.real(in_dft(G_p)) 

g = np.zeros(N)
for b in range(N):
    g[n] = g_p[n]
    
plt.subplot(3,1,1)
plt.stem(x)
plt.subplot(3,1,2)
plt.stem(h)
plt.subplot(3,1,3)
plt.stem(X_)
plt.show()

def delta(n):
    if n == 0:
        return 1
    else:
        return 0
            
def system():
    N = 2
    y = np.zeros(N)
    for n in range(N):
        y[n] = delta(n) - delta(n-1)
    return y 