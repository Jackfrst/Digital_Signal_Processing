import numpy as np 
import matplotlib as mt
import matplotlib.pyplot as plt 
import scipy as sp 
import scipy.linalg as spln
from math import pi

X = np.zeros((10,40))
N = 40
n = np.arange(0,40,1)
s = np.zeros(11)

for w in range(1,11):
	X[w-1] = np.cos((2*pi*w) / 40 * n)
	
for r in range(10):
	s = s + X[r]

s = s*(1/10)

plt.stem(s)
plt.stem(X[1])
plt.show()





