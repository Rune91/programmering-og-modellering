from pylab import *

def X(t):
    return 3*t**3

def Y(t):
    return 2*t+5

t = linspace(0, 12, 100)
x = X(t)
y = Y(t)

plot(x, y)