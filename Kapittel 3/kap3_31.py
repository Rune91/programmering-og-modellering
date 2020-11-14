from pylab import sqrt

def andregradsformel(a, b, c):
    # løsninger for f(x) = ax**2 + bx + c = 0
    # Tar ikke høyde for ligninger uten reelle løsninger eller
    # med flere enn én løsning
    return (-b + sqrt( b**2 - 4*a*c ))/(2*a)

print( andregradsformel(3,6,-24) )