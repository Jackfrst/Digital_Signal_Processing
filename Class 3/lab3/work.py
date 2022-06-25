import numpy as np 
import matplotlib as mt
import matplotlib.pyplot as plt 
import scipy as sp 
import scipy.linalg as spln

def unit_impulse(n):
    delta =[]
    for sample in n:
        if sample == 0:
            delta.append(1)
            return delta            
    return 0
   
u = 50
l = -50
n = np.arange(l, u, 1)
d = unit_impulse(n)
plt.plot(n,d)
plt.plot(n,d)
plt.show()