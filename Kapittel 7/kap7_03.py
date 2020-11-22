from pylab import *

def N(t):
    return 0.2*e**t+90

def newton_symmetrisk(f, x):
    dx = 1e-10
    return (f(x+dx)-f(x-dx))/(2*dx)

t = linspace(0, 5, 1000)

plot(t, N(t))
plot(t, newton_symmetrisk(N, t))
legend(["Populasjon", "Populasjonsendring"])
xlabel("Tid")
ylabel("Antall planter")
title("Plantepopulasjon over tid")