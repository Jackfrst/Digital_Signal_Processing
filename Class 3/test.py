import numpy as np
from matplotlib import pyplot as plt
from math import pi

n = np.array([_ for _ in range(40)])
x = np.sin((2*pi/40)*n)

plt.subplot(2, 2, 1)
plt.plot(x)
plt.subplot(2, 2, 2)
plt.stem(x)
plt.show()