from pylab import *

filnavn = "kap7_12_data.dat"
# Fila inneholder tid og distanse for Robert Gesink
# i 12. etappe i Tour de France 2018
# hentet fra https://github.com/jdai20/Project_4

t = loadtxt(filnavn, usecols=[0], skiprows=1)
x = loadtxt(filnavn, usecols=[1], skiprows=1)

dx = array([])
ddx = array([])
for i in range(1, len(x)):
    dx = append(dx, (x[i]-x[i-1])/(t[i]-t[i-1]))
dx = append(dx, dx[-1])
for i in range(1, len(dx)):
    ddx = append(ddx, (dx[i]-dx[i-1])/(t[i]-t[i-1]))
ddx = append(ddx, dx[-1])

subplot(3,1,1)
title("Robert Gesink i 12. etappe Tour de France 2018")
plot(t, x)
legend(["Posisjon"])
subplot(3,1,2)
plot(t, dx)
legend(["Hastighet"])
subplot(3,1,3)
plot(t, ddx)
legend(["Akselerasjon"])

tight_layout()