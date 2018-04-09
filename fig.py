import matplotlib.pyplot as plt
import numpy as np
"""plt.figure(1)
plt.subplot(211)
plt.plot([1,2,3])
plt.subplot(212)
plt.plot([4,5,6])"""

plt.figure(2)
plt.plot([4,5,6])

plt.figure(1)
plt.subplot(211)
plt.title('Easy as 1,2,3')


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

def figures_and_axes_2():
    t1 = np.arange(0.0,5.0,0.1)
    t2 = np.arange(0.0,5.0,0.02)

    plt.figure(1)
    plt.subplot(211)
    plt.plot(t1,f(t1),'bo',t2,f(t2),'g')

    plt.subplot(212)
    plt.plot(t2, np.cos(2*np.pi*t2),'r--')
    plt.show()
    return()

figures_and_axes_2()
