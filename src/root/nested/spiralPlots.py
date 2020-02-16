import numpy as np
import matplotlib.pyplot as plt

d = 0.25
t = np.arange(0.0, 10.0, 0.1)

plt.figure()
plt.subplot(211)
plt.plot(np.exp(-d * t) * np.cos(np.pi * t), np.exp(-d * t) * np.sin(np.pi * t), 'r--')
plt.xlabel('x(t)')
plt.ylabel('y(t)')

plt.tight_layout()
plt.show()
