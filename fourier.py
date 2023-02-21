import numpy as np
import matplotlib.pyplot as plt


def fourier_sum(n, a, b, c0, T, start):
    def func(t): return c0 + sum([
       a(k+start)*np.cos((k+start)*t*2*np.pi/T) +b(k+start)*np.sin((k+start)*t*np.pi/T)
          for k in range(n)
    ])
    return func



def plot_part_func(i1, i2, f):
    interval = np.linspace(i1, i2, 2000)
    vals = [f(interval[i]) for i in range(len(interval))]
    plt.figure(dpi = 120)
    plt.plot(interval, vals)
    plt.show()


a = lambda k: (1/k**2)*((-1)**k-1)
b = lambda k: 0

a2= lambda k: 1/(-2*np.pi) *(((-1)**(k+1)-1)/(k+1) + ((-1)**(1-k)-1)/(1-k))
a3= lambda k: 2*((-1)**k)*np.sin(2*k)/k

fs = fourier_sum(150, a, b , 8/4, 8, 1)
fs2 = fourier_sum(100, a2, b, 0, 2*np.pi, 2)

fs3 = fourier_sum(100, a3, b,2, 2*np.pi, 1)
plot_part_func(-16, 16, fs2)
#plot_part_func(-4,4, fs)
