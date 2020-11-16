from pylab import *

# Del 1
def f(x):
    return 2*x + 1

x = linspace(0, 5, 100)
y = f(x)

subplot(2,2,1)
xlabel("x")
ylabel("y")
title("f(x)=2x+1")
plot(x, y, "b--")

# Del 2
def f(x):
    return x**2 - 2*x

x = linspace(-10, 12, 100)
y = f(x)

subplot(2,2,2)
ylim(-10, 150)
xlabel("x")
ylabel("y")
title("f(x)=x**2-2x")
plot(x, y)

# Del 3
def G(t):
    return 1.05**t+10

x = linspace(0, 20, 20)
y = G(x)

subplot(2,2,3)
title("Gaupepopulasjon")
xlabel("Tid")
ylabel("Populasjon")
plot(x, y, "g.")



tight_layout()
# Denne kommandoen gjør at delplottene ikke overlapper.
# Ta den bort for å se uten