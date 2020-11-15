tall1 = float( input("Tall: ") )
tall2 = float( input("Tall: ") )
operasjon = input("Regneoperasjon: ( + - * / ) ")

resultat = 0
if operasjon == "+":
    resultat = tall1 + tall2
elif operasjon == "-":
    resultat = tall1 - tall2
elif operasjon == "*":
    resultat = tall1 * tall2
elif operasjon == "/":
    resultat = tall1 / tall2


print(f"{tall1} {operasjon} {tall2} = {resultat}")