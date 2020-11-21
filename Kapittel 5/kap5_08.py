liste = [32, 76, 1, 49, 65, 5, 71, 19, 98, 123]

storst_i = 0
storst_verdi = 0
minst_verdi = float('inf')
for i, tall in enumerate(liste):
    if tall > storst_verdi:
        storst_verdi = tall
        storst_i = i
    if tall < minst_verdi:
        minst_verdi = tall

del liste[storst_i]
liste.append(minst_verdi)