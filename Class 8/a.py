import re
import numpy as np
from matplotlib import pyplot as plt
from math import pi,pow

def delta (n):
    if n == 0:
        return 1
    else :
        return 0
    
def system(M):
    N = 50
    
    if M == 1:
        y = np.zeros(N)
        for i in range(N):
            y[i] = 0.3*delta(i) + 0.1*delta(i-1) + 0.25*delta(i-2)
        return y
    
    if M == 2:
        y = np.zeros(N)
        for i in range(N):
            y[i] = 0.21*delta(i) - 0.5*delta(i-1) 
        return y
   
h = system(1) 
h1 = system(2) 

plt.subplot(2,1,1)
plt.title("Impulse of system 1")
plt.stem(h)
plt.subplot(2,1,2)
plt.title("Impulse of system 2")
plt.stem(h1)
plt.show()
  
    
    