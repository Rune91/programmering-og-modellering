from pylab import loadtxt
import re

# Del 1 og 2
filnavn = "kap5_37_data.csv"
gs = loadtxt(filnavn, dtype="str", delimiter=",", usecols=[1]).tolist()
am = loadtxt(filnavn, dtype="str", delimiter=",", usecols=[3]).tolist()
grunnstoffer = {}
for i, stoff in enumerate(gs):
    stoff = stoff.strip()
    vekt_tekst = am[i]
    atomvekt = 0
    if "[" in vekt_tekst:
        atomvekt = float( vekt_tekst.replace("[","").replace("]","") )
    else:
        atomvekt = float( vekt_tekst.split("(")[0] )
    grunnstoffer[stoff] = atomvekt

# Del 3
def MM(forbindelse):
    treff = re.findall('[A-Z][a-z]*', forbindelse)
    if len(treff) == 0: return 0
    stoff = treff[0]
    forbindelse = forbindelse.replace(stoff, "", 1)
    antall = 1
    if len(tall := re.findall('^[^A-Z]', forbindelse)) > 0:
        antall = int(tall[0])
        forbindelse = forbindelse.replace(tall[0], "", 1)
    return antall * grunnstoffer[stoff] + MM(forbindelse)


forbindelse = "H2SO4"
mm = MM(forbindelse)
print(f"Molekylmassen til {forbindelse} er {mm} g/mol")

#Del 4

