bolgelengde = float( input("Bølgelengden til lys (nm): ") )


farge = ""
if bolgelengde < 400:
    farge = "ultrafiolett"
elif bolgelengde < 475:
    farge = "blått"
elif bolgelengde < 530:
    farge = "grønt"
elif bolgelengde < 580:
    farge = "gult"
elif bolgelengde < 620:
    farge = "oransje"
elif bolgelengde < 700:
    farge = "rødt"
else:
    farge = "infrarødt"


print(f"Lyset med bølgelengde {bolgelengde} nm er {farge}.")