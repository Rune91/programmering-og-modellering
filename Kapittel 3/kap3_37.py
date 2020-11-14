def penger_i_banken(rente, belop, aar):
    # Regner ut pengebeløpet med rentesats i prosent etter gitt antall år
    # ved hjelp ab eksponentiell vekst
    # https://en.wikipedia.org/wiki/Exponential_growth
    return belop * ((100+rente)/100) ** aar

print( penger_i_banken(5, 100, 10) )