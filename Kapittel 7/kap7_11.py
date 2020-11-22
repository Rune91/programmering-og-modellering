from pylab import *

def f(x):
    return (100*x**2 + 1000) / (1.07*x**3 + 45)

def newton_symmetrisk(f, x):
    dx = 1e-7
    return (f(x+dx)-f(x-dx))/(2*dx)

X = linspace(0, 100, 1000)
F = f(X)
dF = newton_symmetrisk(f, X)

# Del 1
plot(X, F)
plot(X, dF)
title("Dyrebestand i et avgrenset område")
legend(["Bestand", "Endring i bestand"])
xlabel("Tid [år]")
ylabel("Antall dyr")

# Del 2 og 3
x_max = 0
df_max = 0
for aar, endring in enumerate(dF):
    if endring > df_max:
        df_max = endring
        x_max = aar

print(f"Dyrebestanden vokste mest i år {x_max}.")