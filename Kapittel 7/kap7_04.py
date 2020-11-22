from pylab import *

def x(t):
    return t**3+1/3*t

def newton_kvotient(f, x):
    dx = 1e-10
    return (f(x+dx)-f(x))/dx

def newton_kvotient_2(f, x):
    dx = 1e-5
    return (f(x+dx)-2*f(x)+f(x-dx))/dx**2

t = linspace(0, 10, 1000)

subplot(1,3,1)
title("Posisjon")
plot(t, x(t))

subplot(1,3,2)
title("Hastighet")
plot(t, newton_kvotient(x, t))

subplot(1,3,3)
title("Akselerasjon")
plot(t, newton_kvotient_2(x, t))

tight_layout()