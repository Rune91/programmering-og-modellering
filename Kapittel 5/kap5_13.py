liste1 = ["dette", "er", "en", "ganske", "lang", "liste",
          "med", "ikke", "så", "viktig", "innhold"]

liste2 = []
liste2 += liste1[:3]
liste2 += liste1[5:7]
liste2 += liste1[9:]

print(liste2)