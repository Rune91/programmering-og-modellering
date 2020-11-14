from pylab import log10

def pH(h30):
    return -log10(h30)

print( pH(1.0e-7) )