
def V_ideel(P, n, T):
    # P: trykk          [pascal]
    # n: stoffmengde    [mol]
    # T: temperatur     [K]
    R = 8.3144598       # J/(K*mol)
    return n*R*T / P    # [m**3]

def V_vdW_CO2(P, n, T):
    b = 42.69e-6 # [m**3 / mol]
    # verdien for b er eksperimentell og ulik for ulike gassen.
    # denne funksjonen regner for gassen CO2
    return V_ideel(P, n, T) + n*b

trykk = float( input("Trykk [Pascal]: ") )
stoffmengde = float( input("Stoffmengde [mol]: ") )
temperatur = float( input("Temperatur [Kelvin]: ") )

print(f"Volum i følge ideel gasslov: {V_ideel(trykk, stoffmengde, temperatur)} m**3")
print(f"Volum i følge vdW gasslov: {V_vdW_CO2(trykk, stoffmengde, temperatur)} m**3")

"""
Ideel gasslov tar ikke hensyn til interaksjoner mellom molekylene i gassen.
På grunn av dette gir den verdier som er lite nøyaktig for tilstander med høyt
trykk og lave temperaturer.
Van der Waals likning tar høyde for molekylinteraksjoner, og er derfor mer nøyaktig.
Bakdelen med denne er at den krever eksperimentelle verdier som er ulike for
alle gasser.

Ideelle gasslov er mindre nøyaktig men mer generell.
"""