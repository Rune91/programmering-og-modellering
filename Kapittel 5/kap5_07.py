liste = [5, 12, 65, 13, 4, 45]

def storste_tall(liste):
    storst = 0
    for tall in liste:
        if tall > storst:
            storst = tall
    return storst

print(storste_tall(liste))