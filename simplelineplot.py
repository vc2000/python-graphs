import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_ylabel('volts')
ax.set_title('a sine wave')
t= np.arange(0.0,1.0,0.01)
s= np.sin(2*np.pi*t)
line = ax.plot(t,s,color='blue', lw=2)

plt.show()
