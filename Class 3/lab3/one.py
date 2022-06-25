import numpy as np 
import matplotlib as mt
import matplotlib.pyplot as plt 
import scipy as sp 
import scipy.linalg as spln


def unit_impulse(a, n):
    delta =[]
    for sample in n:
        if sample == a:
            delta.append(1)
        else:
            delta.append(0)
              
    return delta
  
a = 0    
u = 50
l = -50
n = np.arange(l, u, 1)
d = unit_impulse(a, n)
plt.plot(n,d)
plt.stem(n, d)
plt.show()