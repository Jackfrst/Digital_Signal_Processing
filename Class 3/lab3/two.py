import numpy as np 
import matplotlib as mt
import matplotlib.pyplot as plt 
import scipy as sp 
import scipy.linalg as spln

def unit_ramp(n):
    ramp =[]
    for sample in n:
        if sample>0:
            ramp.append(sample)
        else:
            ramp.append(0)
    return ramp
   
u = 50
l = -50
n = np.arange(l, u, 1)
d = unit_ramp(n)
plt.plot(n,d)
plt.show()