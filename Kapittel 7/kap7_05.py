from pylab import *

def x(t):
    return 3*t**2+4*t
def y(t):
    return 5*t+4

def newton_kvotient(f, x):
    dx = 1e-10
    return (f(x+dx)-f(x))/dx

t = linspace(0, 10, 1000)

plot(t, newton_kvotient(x, t))
plot(t, newton_kvotient(y, t))
legend(["Mot nord", "Mot øst"])
title("Fart til turgåer")
xlabel("Tid")
ylabel("Fart")