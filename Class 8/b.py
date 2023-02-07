import numpy as np
from matplotlib import pyplot as plt
from math import pi,pow

def delta (n):
    if n == 0:
        return 1
    else :
        return 0
    
def system():
    N = 50
    y = np.zeros(N)
    for i in range(N):
        y[i] = 0.21*delta(i) - 0.5*delta(i-1) 
    return y

def conv(x,h):
    N,M = x.shape[0], h.shape[0]
    L = M + N - 1
    y = np.zeros(L)
    for n in range(L):
        for k in range(N):
            if n - k >= 0 and n - k < M:
                y[n] += x[k] * h[n-k]          
    return y 

N = 100
n = np.arange(N)
x = np.divide(np.power(1.6,(-n % N)),(1 - pow(1.6,N)))

h = system()
y = conv(x,h)

plt.subplot(3,1,1)
plt.title("Signal")
plt.stem(x)
plt.subplot(3,1,2)
plt.title("Impulse of system")
plt.stem(h)
plt.subplot(3,1,3)
plt.title("Convolution Result")
plt.stem(y)
plt.show()