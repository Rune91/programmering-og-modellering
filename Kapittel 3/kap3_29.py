
def bolgelengde(m, n):
    # Gir bølgelengden i nm til et foton som emitteres når et elektron
    # deeksiteres fra skall m til n
    h = 6.626e-34                       # Plancks konstant [J*s]
    c = 3e8                             # lyshastigheten [m/s]
    energi = (1/n**2 - 1/m**2) * 13.6   # [eV]
    energi = energi * 1.602e-19         # [J]
    lengde = h * c / energi             # [m]
    lengde = lengde * 1e9               # [nm]
    return lengde

print( bolgelengde(5, 2) )