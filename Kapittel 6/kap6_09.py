from pylab import *

g = 9.81 # m/s**2
v = 20 # m/s
N = 1000

def hoyde_ved_vegg(theta):
    theta = theta * 2*pi / 360
    return -50*g/(v**2*cos(theta)**2) + 10*tan(theta)

def gir_treff(theta):
    hoyde = hoyde_ved_vegg(theta)
    return hoyde >= 5 and hoyde <= 5.25

# Del 1
vinkler1 = uniform(30, 60, N)

# Del 2
treff1 = [vinkel for vinkel in vinkler1 if gir_treff(vinkel)]
m = sum(treff1) / len(treff1)

# Del 3
vinkler2 = normal(m, 0.005, N)
treff2 = [vinkel for vinkel in vinkler2 if gir_treff(vinkel)]

# Del 4
print(f"Kula traff {len(treff1)} ganger med uniform fordeling.\nKula traff {len(treff2)} med normalfordeling.")