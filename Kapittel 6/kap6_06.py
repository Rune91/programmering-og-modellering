from pylab import shuffle

def lag_kortstokk():
    kortstokk = []
    for symbol in ["Spar", "Kløver", "Hjerter", "Ruter"]:
        for nummer in ["ess", 2, 3, 4, 5, 6, 7, 8, 9, 10, "knekt", "dame", "konge"]:
            kort = [symbol, nummer]
            kortstokk.append(kort)
    shuffle(kortstokk)
    return kortstokk

def del_ut(antall, haand):
    for i in range(antall):
        if len(stokk) > 0:
            kort = stokk.pop()
            haand.append(kort)

def lovlig(kort):
    return kort[0] == bord[-1][0] or kort[1] == bord[-1][1]


stokk = lag_kortstokk()
haand = []
del_ut(3, haand)
bord = []
del_ut(1, bord)

print("""
Du må spille ut et kort som har enten samme symbol eller samme tall
som det forrige kortet. Dersom du ikke kan spille ut noe, må du trekke inn 3 kort.
Du vinner dersom du bruker opp kortene på hånda.
Du taper dersom stokken går tom.
""")

while len(haand) > 0 and len(stokk) > 0:
    print(f"Det er {len(stokk)} kort igjen i stokken.")
    print(f"På bordet ligger {bord[-1]}\n")
    print("Hvilket kort vil du spille?")
    while True:
        for i, kort in enumerate(haand):
            print(f"({i}) {haand[i]}")
        print(f"(x) Trekke inn kort")
        valg = input("")
        if valg == "x":
            del_ut(3, haand)
            break
        kort = haand[int(valg)]
        if lovlig(kort):
            haand.pop(int(valg))
            bord.append(kort)
            break
        else:
            print("Du kan ikke spille det kortet!")

print("Spillet er over!")
if len(haand) == 0:
    print("Du vant!")
else:
    print("Du tapte!")
    