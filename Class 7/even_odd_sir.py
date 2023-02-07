import numpy as np
from matplotlib import pyplot as plt

N = 50
x = np.array([(n % 5) + 11 for n in range(N)])
e = np.zeros(N)
o = np.zeros(N)

for n in range(N):
    e[n] = 0.5 * (x[n] + x[-n % N])
    o[n] = 0.5 * (x[n] - x[-n % N])

plt.subplot(4, 1, 1)
plt.stem(x)
plt.subplot(4, 1, 2)
plt.stem(e)
plt.subplot(4, 1, 3)
plt.stem(o)
plt.subplot(4, 1, 4)
plt.stem(e + o)
plt.show()
