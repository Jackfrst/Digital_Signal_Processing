import numpy as np 
import matplotlib as mt 
import matplotlib.pyplot as mtp 
from math import pi, pow
import scipy as sp
from numpy.linalg import svd 

f = 1
n = 7
N = np.arange(n)
w = 2*pi*f/20
x = np.cos(w*N)

x_s = np.cos(w*(N+1))

mtp.subplot(2,1,1)
mtp.stem(x)
mtp.subplot(2,1,2)
mtp.stem(x_s)
mtp.show()