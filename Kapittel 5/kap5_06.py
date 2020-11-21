liste = []
for i in range(0, 51):
    liste.append(i)

def liste_sum(liste):
    totalt = 0
    for tall in liste:
        totalt += tall
    return totalt

print(liste_sum(liste))