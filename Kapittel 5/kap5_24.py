from pylab import array,dot,sqrt
v = array( [3,1,2] )
lengde = sqrt( dot(v, v) )
print(f"Lengden av vektoren {v} er {lengde:.2f}")