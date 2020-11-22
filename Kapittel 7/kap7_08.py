from pylab import linspace, plot, figure, e, sqrt, log

def newton_kvotient(f, x, dx):
    return (f(x+dx)-f(x))/dx
def newton_symmetrisk(f, x, dx):
    return (f(x+dx)-f(x-dx))/(2*dx)

x = linspace(2,5,100)
dx = 1e-10

# Del 1
def f1(x):
    return 2*x+1
figure(0)
plot(x, f1(x))
plot(x, newton_kvotient(f1,x,dx))
plot(x, newton_symmetrisk(f1,x,dx))

# Del 2
def f2(x):
    return x**2-4*x+5
figure(1)
plot(x, f2(x))
plot(x, newton_kvotient(f2,x,dx))
plot(x, newton_symmetrisk(f2,x,dx))

# Del 3
def f3(x):
    return e**x
figure(2)
plot(x, f3(x))
plot(x, newton_kvotient(f3,x,dx))
plot(x, newton_symmetrisk(f3,x,dx))

# Del 4
def f4(x):
    return e**x-5*x
figure(3)
plot(x, f4(x))
plot(x, newton_kvotient(f4,x,dx))
plot(x, newton_symmetrisk(f4,x,dx))

# Del 5
def f5(x):
    return 6*sqrt(x)-x
figure(4)
plot(x, f5(x))
plot(x, newton_kvotient(f5,x,dx))
plot(x, newton_symmetrisk(f5,x,dx))

# Del 6
def f6(x):
    return 5*e**(-2*x)
figure(5)
plot(x, f6(x))
plot(x, newton_kvotient(f6,x,dx))
plot(x, newton_symmetrisk(f6,x,dx))

# Del 7
def f7(x):
    return sqrt(log(x))
figure(6)
plot(x, f7(x))
plot(x, newton_kvotient(f7,x,dx))
plot(x, newton_symmetrisk(f7,x,dx))

# Del 8
def f8(x):
    return 4*log(x**2)
figure(7)
plot(x, f8(x))
plot(x, newton_kvotient(f8,x,dx))
plot(x, newton_symmetrisk(f8,x,dx))

# Del 9
def f9(x):
    return 4*5**(x**3-2*x)
figure(8)
plot(x, f9(x))
plot(x, newton_kvotient(f9,x,dx))
plot(x, newton_symmetrisk(f9,x,dx))