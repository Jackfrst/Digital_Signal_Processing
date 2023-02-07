import numpy as np
from matplotlib import pyplot as plt
from math import pi,pow

N = 100
n = np.arange(N)
w = 4 * pi / N
Z = 0.4 + 4j
mod_Z = np.abs(Z)

r = np.power(mod_Z,n)
i = np.exp(1j*w*n)

x = r*i

m = np.sqrt(np.power(r,2),np.power(i,2))
ang = np.arctan(i / r)

plt.subplot(3,1,1)
plt.title("Ploting X")
plt.stem(x)
plt.subplot(3,1,2)
plt.title("Magnitude")
plt.stem(m)
plt.subplot(3,1,3)
plt.title("Angle")
plt.stem(ang)
plt.show()
