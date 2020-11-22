from pylab import *

def T(t):
    return 70*e**(-0.065*t)

def newton_kvotient(f, x):
    dx = 1e-10
    return (f(x+dx)-f(x))/dx

# Del 1
t = linspace(0, 60, 1000)

# Del 2
plot(t, T(t))
plot(t, newton_kvotient(T, t))
legend(["Temperatur", "Temperaturendring"])
xlabel("Tid [min]")
ylabel("Temperatur [C]")
title("Temperatur i nylig lagd te")

# Del 3
print(f"Ved element 42 i lista synker temperaturen med {newton_kvotient(T, t[41]):.2f} grader/min.")