from scipy.special import binom

N = int( input("N: ") )

for n in range(N+1):
    rad = ""
    for r in range(0, n+1):
        verdi = int( binom(n, r) )
        rad += " " + str(verdi)
    print(rad)