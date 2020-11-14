def bevegelse_avstand(startfart, tid, akselerasjon):
    return startfart * tid + 0.5 * akselerasjon * tid**2

print( bevegelse_avstand(2, 10, 9.81) )