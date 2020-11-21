from pylab import loadtxt

# Lese inn isotopdata fra fil
filnavn = "kap5_36_data.txt"
symboler = loadtxt(filnavn, dtype="str", delimiter=" ", usecols=[0], skiprows=1)
masser = loadtxt(filnavn, dtype="float", delimiter=" ", usecols=[1], skiprows=1)
isotoper = {}
for i in range(len(symboler)):
    isotoper[ symboler[i] ] = masser[i]
    
# Del 1
isotop = input("Skriv inn en isotop (f.eks U-238): ")
if isotop in isotoper.keys():
    masse = isotoper[isotop]
    print(f"{isotop} har massen {masse:4g} u.\n")
else:
    print(f"{isotop} er en ugyldig isotop.")

# Del 2 og 3
def energi_reaksjon(r):
    v = r.split(" -> ")[0]
    h = r.split(" -> ")[1]
    masse_v = 0
    for isotop in v.split(" + "):
        masse_v += isotoper[isotop]
    masse_h = 0
    for isotop in h.split(" + "):
        masse_h += isotoper[isotop]
    
    m = (masse_v-masse_h) * 1.660539e-27    # kg
    c = 2.99792458e8                        # m/s
    E = m * c**2                            # J
    return E

r1 = "He-3 + He-3 -> He-4 + H-1 + H-1"
E1 = energi_reaksjon(r1) # J
E1_ = E1 / 1.602177e-13   # MeV
print(f"\n{r1}\n{E1:4g} J\n{E1_:4g} MeV")