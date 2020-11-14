def antall_mol(vekt, molmasse):
    return vekt * molmasse

vekt = float( input("Vekt (g): ") )
molmasse = float( input("Molmasse (g/mol): ") )
stoff = input("Stoff: ")

mol = antall_mol(vekt, molmasse)

print(f"{vekt} g {stoff} er {mol} mol.")