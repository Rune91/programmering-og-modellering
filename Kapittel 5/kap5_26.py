from pylab import *

def f(x):
    return x**2

antall_x = 20

x = linspace(-1, 1, antall_x)
y = f(x)

plot(x[:antall_x//2], y[:antall_x//2], "r-.")
plot(x[antall_x//2-1:], y[antall_x//2-1:], "g:")