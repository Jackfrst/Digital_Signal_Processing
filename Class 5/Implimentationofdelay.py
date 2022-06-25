import numpy as np 
import matplotlib as mt 
import matplotlib.pyplot as mtp 
import scipy as sp 
from math import pi,pow

M = 20 
k = 4
N = 51

x = np.zeros(N)
for i in range(N):
	if i < 0:
		x[i] = 0
	elif i < 21:
		x[i] = i
	else:
		x[i] = 0			


y = np.zeros(N)
y_1 = np.zeros(N)
for i in range(N):
	t = i - k
	if t < 0:
		y[i] = 0
	else :
		y[i] = x[t]
	# t = i + k
	# if t < 0:
	# 	y_1[i] = 0
	# elif t > 50 :
	# 	break
	# else :
	# 	y_1[i] = x[t]
	if i + k >= N :
		y_1[i] = 0
	else :
		y_1[i] = x[i + k] 	

mtp.subplot(3,1,1)
mtp.stem(x)
mtp.subplot(3,1,2)
mtp.stem(y)	
mtp.subplot(3,1,3)
mtp.stem(y_1)	
mtp.show()
	



	