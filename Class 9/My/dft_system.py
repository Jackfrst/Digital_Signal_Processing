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
    return (1 / N) * X
        
def delta(n):
    if n == 0:
        return 1
    else:
        return 0
            
def system(N):
    y = np.zeros(N)
    for n in range(N):
        y[n] = delta(n) - delta(n-1)
    return y 

N = 100
n = np.arange(N)
x = np.cos((2*pi*4*n)/N) + np.random.random(N)
M = 2
# h = np.array([1/M for n in range(M)])
h = system(M)
h = 1 - h
a = N + M - 1
X = dft(x)
X_ = in_dft(X)
x_p = np.zeros(a)
h_p = np.zeros(a)

for n in range(N):
    x_p[n] = x[n]
for n in range(M):
    h_p[n] = h[n]

X_p = dft(x_p)    
H_p = dft(h_p)
G_p = X_p * H_p
g_p = np.real(in_dft(G_p)) 

g = np.zeros(N)
for n in range(N):
    g[n] = g_p[n]

plt.subplot(3,1,1)
plt.stem(h_p)
plt.subplot(3,1,2)
plt.plot(x_p)
plt.subplot(3,1,3)
plt.plot(g)
plt.show()