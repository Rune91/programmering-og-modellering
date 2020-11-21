from pylab import *

matrise_par = array([], dtype=int32)
matrise_odde = array([], dtype=int32)

for i in range(102):
    if i % 2 == 0:
        matrise_par = append(matrise_par, i)
    else:
        matrise_odde = append(matrise_odde, i)

print( matrise_par + matrise_odde )