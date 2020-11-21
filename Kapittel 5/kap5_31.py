from pylab import *

def f(x, A, k, phi, d):
    return A*sin(k*x+phi) + d

x = linspace(0, 2*pi, 100)
y1 = f(x, 1, 1, 0, 0)
y2 = f(x, 2, 2, 0, 0)
y3 = f(x, 0.5, 4, pi/2, 5)

subplot(3,1,1)
title("sin(x)")
plot(x, y1, "b")

subplot(3,1,2)
title("2sin(2x)")
plot(x, y2, "r")

subplot(3,1,3)
title("0.5sin(4x+pi/2)+5")
plot(x, y3, "g")

tight_layout()