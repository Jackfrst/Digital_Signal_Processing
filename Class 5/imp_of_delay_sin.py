import numpy as np 
import matplotlib as mt 
import matplotlib.pyplot as mtp 
import scipy as sp 
from math import pi,pow,floor

N = 70
# n = np.arange(69)
# x = 3*np.cos((6*pi*n/N) + (2*pi/10))
x = np.zeros(N)
for i in range(N):
		x[i] = 3*np.cos((6*pi*i/N) + (2*pi/10))


y = np.zeros(int(N/2))
for i in range(floor(N/2)):
	y[i] = x[2*i]

# for i in range(N):
# 	t = 2 * i
# 	if t > 69 :
# 		break
# 	else :
# 		y[i] = x[t]

y_1 = np.zeros(N*2)
for i in range(N*2):
	if i%2 == 0:
		y_1[i] = x[int(i/2)]

mtp.subplot(3,1,1)
mtp.stem(x)
mtp.subplot(3,1,2)
mtp.stem(y)	
mtp.subplot(3,1,3)	
mtp.stem(y_1)
mtp.show()