from math import sqrt

def g(x):
    return sqrt(x)

def u(x):
    return x**2 + 7

def f(g, u, x):
    return g( u(x) )

x = 3
print("f(x) = g(u(x)) = ", f(g,u,x), " for x = ", x)