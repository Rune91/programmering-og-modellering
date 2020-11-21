from pylab import shuffle

def lag_kortstokk():
    kortstokk = []
    for symbol in ["Spar", "Kløver", "Hjerter", "Ruter"]:
        for nummer in ["ess", 2, 3, 4, 5, 6, 7, 8, 9, 10, "knekt", "dame", "konge"]:
            kort = [symbol, nummer]
            kortstokk.append(kort)
    shuffle(kortstokk)
    return kortstokk

print( lag_kortstokk() )