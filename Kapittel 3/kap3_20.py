# Program 1
def f(x):
    return 1/(2*x) + 1
print("f() = ", f(4))

# Program 2
from pylab import cos
def f(x):
    return 3*x + cos(x)
y = float( input("Skriv inn en verdi for x: ") )
print("f(x) = ", f(y))

# Program 3
def G(t):
    a = t**2 - 2
    return a
t = 1
print(G(t))