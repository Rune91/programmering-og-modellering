from pylab import log, e
# log i pylab er den naturlige logaritmen "ln"

N_0 = 4             # kg
T = 24000           # år
tid_slutt = 50000         # år
intervall = 5000    # år

a = log(2) / T

for tid in range(0, tid_slutt+1, intervall):
    N = N_0 * e**(-a*tid)
    print(f"{N:.2f} kg Plutonium-239 gjenstår etter {tid:5} år")