from pylab import array, sum

v1 = array( [2,2] )
v2 = array( [1,-3] )

if sum(v1 * v2) == 0:
    print("Vektorene er ortogonale")
else:
    print("Vektorene er ikke ortogonale")