from pylab import cos, tan, pi

g = 9.81    # m/s**2

def meter_over_bakken(v, theta, g):
    # theta oppgitt i grader
    theta_rad = theta * 2*pi / 360
    return -25/2 * g/(v**2*(cos(theta_rad)**2)) + 5*tan(theta_rad)

def treffer_hull(over_bakken):
    return over_bakken > 7.5 and over_bakken < 8

# Del 1
skytefart = float( input("Skytefart (m/s): ") )
vinkel = float( input("Vinkel (grader): ") )

hoyde = meter_over_bakken(skytefart, vinkel, g)
treff = treffer_hull(hoyde)

print(f"Kula treffer veggen {hoyde:.2f} m over bakken.")
if treff:
    print("Den treffer hullet.")
else:
    print("Den treffer ikke hullet.")