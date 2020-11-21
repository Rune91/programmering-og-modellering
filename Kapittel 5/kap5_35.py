from pylab import loadtxt

filnavn_inn = "kap5_35_data.dat"
# filen er ikke den samme som oppgitt i boka, men
# er strukturert på samme måte

# Del 1
material_navn = loadtxt(filnavn_inn, dtype="str", delimiter=" ", usecols=[0], skiprows=1).tolist()
material_tetthet = loadtxt(filnavn_inn, dtype="float", delimiter=" ", usecols=[1], skiprows=1).tolist()
material_volum = loadtxt(filnavn_inn, dtype="float", delimiter=" ", usecols=[2], skiprows=1).tolist()

# Del 2
material_masse = []
for i in range(len(material_tetthet)):
    tetthet = material_tetthet[i]
    volum = material_volum[i]
    material_masse.append(tetthet * volum)

# Del 3
filnavn_ut = "kap5_35_data2.dat"
fil = open(filnavn_ut, "w")

fil.write("materialtype : masse")
for i in range(len(material_navn)):
    navn = material_navn[i]
    masse = material_masse[i]
    fil.write(f"\n{navn} : {masse}")

fil.close()