from pylab import array,det,cross

v1 = array( [0,2,2] )
v2 = array( [1,1,2] )

# Determinant
v_prod1 = array( [ det(array( [[v1[1], v1[2]], [v2[1], v2[2]]] )),
                   det(array( [[v1[2], v1[0]], [v2[2], v2[0]]] )),
                   det(array( [[v1[0], v1[1]], [v2[0], v2[1]]] )) ] )

# Vektorprodukt direkte
v_prod2 = cross(v1, v2)