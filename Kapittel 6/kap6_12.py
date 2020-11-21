from pylab import randint, zeros

def terning_2():
    return ( randint(1,7), randint(1,7) )

resultat_matrise = zeros((6,6), dtype=int)   # For del 1
resultat_liste = zeros(12, dtype=int)        # For del 2 og 3
for i in range(10000):
    kast = terning_2()
    resultat_matrise[ kast[0]-1 ][ kast[1]-1 ] += 1
    resultat_liste[ sum(kast)-2 ] += 1

print(resultat_matrise)

N = int( input("Sum av to terningkast: ") )
antall = resultat_liste[N-1]
print(f"Summen {N} forekom {antall} ganger ut av 10000 forsøk.")