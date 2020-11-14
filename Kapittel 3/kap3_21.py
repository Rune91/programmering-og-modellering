from pylab import pi

# Alle funksjonene tar inn diameter som argument

def areal_sirkel(d):
    return pi * (d/2)**2

def radius_sirkel(d):
    return d / 2

def omkrets_sirkel(d):
    return pi * d

def volum_kule(d):
    return 4 / 3 * pi * (d/2)**3

def overflate_kule(d):
    return 4 * pi * (d/2)**2