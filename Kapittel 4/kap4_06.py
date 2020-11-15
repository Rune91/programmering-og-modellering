def gi_karakter(poeng, maks_poeng, grenser):
    # Poenggrensene er oppgitt i prosent
    prosent = poeng / maks_poeng * 100
    for i in range( len(grenser) ):
        if prosent < grenser[i]:
            return i+1
    return len(grenser)

poeng = 13
maks_poeng = 20
grenser = [20, 40, 60, 80, 90]
# minst 20% for karakter 2, 40% for 3 osv.

print( gi_karakter(poeng, maks_poeng, grenser) )