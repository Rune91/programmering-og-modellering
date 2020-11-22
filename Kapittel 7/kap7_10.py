from pylab import *

def u(x):
    return x**3 + 3*x
def v(x):
    return sqrt(log(x)+x**2)
def u_ganger_v(x):
    return u(x) * v(x)
def u_delt_v(x):
    return u(x) / v(x)
def dfdx(f, x):
    dx = 1e-7
    return (f(x+dx)-f(x))/dx

x = 7

# Del 1
v1 = dfdx(u_ganger_v, x)
h1 = dfdx(u,x)*v(x) + dfdx(v,x)*u(x)
print(f"Venstre side: {v1:5g}\nHøyre side:   {h1:7g}")

# Del 2
v1 = dfdx(u_delt_v, x)
h1 = (dfdx(u,x)*v(x) - dfdx(v,x)*u(x)) / v(x)**2
print(f"Venstre side: {v1:5g}\nHøyre side:   {h1:7g}")