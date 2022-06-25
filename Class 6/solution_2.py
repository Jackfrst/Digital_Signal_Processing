import numpy as np 
import matplotlib as mp
import scipy as sp  
from matplotlib import pyplot as plt
from numpy.random import random 
from math import pi , pow
from scipy import signal

def delta (n):
	if n == 0 :
		return 1
	return 0

def system(M):
	N  = x.shape[0]
	y = np.zeros(N)
	for i in range(N):
		sum = 0
		for j in range(M):
			sum = sum + delta(i-j)
		y[i] = 1/M * sum  
	return y
		
N = 100
x = np.array([delta(n) for n in range(N)])
y = system(5)

plt.subplot(2,1,1)
plt.stem(x)
plt.subplot(2,1,2)
plt.stem(y)
plt.show()
