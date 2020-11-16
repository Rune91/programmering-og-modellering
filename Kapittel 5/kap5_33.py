from pylab import *

def K(x):
    # Jeg regner med det er skrivefeil i K(x) i oppgaveteksten.
    # Bruker positivt første ledd istedenfor
    return 50*x**2 - 420*x - 50

def I(x):
    return 84*x

def P(x):
    return I(x) - K(x)

x = linspace(0, 15, 1000)
p = P(x)

x_max = 0
p_max = 0
for i, profitt in enumerate(p):
    if profitt > p_max:
        p_max = profitt
        x_max = x[i]

title("Profitt for laksesalg")
xlabel("Mengde laks [kg]")
ylabel("Profitt [kr]")
plot(x, p)
plot(x_max, p_max, "ro")