import numpy as np 
import matplotlib as mt 
import matplotlib.pyplot as mtp 
from math import pi, pow
import scipy as sp
from numpy.linalg import svd 

X = np.zeros((10,40))
n = np.arange(0,40)

for w in range(1,11):
	X[w-1] =  np.cos((2*pi*w)/40*n)

s = np.zeros(40)

for r in range(10):
	s = s + X[r]

s = s / 10

X1 = np.mean(X)

C = np.zeros((40,40))

for r in range(10):
	C = C + np.outer(X[r]-s,X[r]-s)

C = C / 10

(U,S,V) = svd(C)

X_r = np.zeros((10,20))

for r in range(10):
	X_r[r] = np.dot(X[r],V[0:20].T)

mtp.subplot(2,1,1)
mtp.stem(X[2])	
mtp.subplot(2,1,2)
mtp.stem(X_r[2])	
mtp.show()
