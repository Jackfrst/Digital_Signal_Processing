import numpy as np 
import matplotlib as mt 
import matplotlib.pyplot as mtp 
from math import pi, pow
import scipy as sp

N = 7
x = np.array([1,2,3,4,3,2,1])
y = np.zeros(N)
s_t = 2

for n in range(N):
	t =  n - s_t
	if t < 0 :
		y[n] = 0
	else :
		y[n] = x[t]

mtp.subplot(2,1,1)
mtp.stem(x)	
mtp.subplot(2,1,2)
mtp.stem(y)	
mtp.show()