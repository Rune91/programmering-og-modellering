from pylab import *

m = 2.75 # kg
g = 9.81 # m/s**2

def y(t):
    global g
    return -0.5*g*t**2 + 33

def v(t):
    global g
    return -g*t

def E_k(t):
    global m
    return 0.5*m*v(t)**2

def E_p(t):
    global m, g
    return m*g*y(t)

t = linspace(0, sqrt(66/g), 100)
ek = E_k(t)
ep = E_p(t)
et = E_k(t) + E_p(t)

title("Energi til et legeme som faller fra en klippe")
xlabel("Tid [s]")
ylabel("Energi [J]")
plot(t, ek)
plot(t, ep)
plot(t, et)
legend( ["Kinetisk energi", "Potensiell energi", "Mekanisk energi"] )

# Kan se at den mekaniske energien er bevart ved at total mekanisk energi er konstant