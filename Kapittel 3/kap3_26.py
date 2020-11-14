def tid(avstand, fart):
    return avstand / fart

avstand = int( input("Avstand (m): ") )
fart = int( input("Fart (m/s): ") )

tidsbruk = tid(avstand, fart)
print(f"Løperen bruker {tidsbruk} s på å løpe {avstand} m med en fart på {fart} m/s.")