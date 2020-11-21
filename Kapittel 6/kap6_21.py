from pylab import uniform, randint

hp_scaredalot = 100
hp_monster = 100

while hp_scaredalot > 0 and hp_monster > 0:
    print("\nHva skal Scaredalot gjøre nå?")
    print("0 : drikke eliksir")
    print("1 : bruke sverd")
    print("2 : kaste stein")
    
    valg = input("Skriv her: ")
    if valg == "0":
        hp_scaredalot += 30
        print("Scaredalot drikker eliksir for 30 hp!")
    elif valg == "1":
        skade = int( 40 * uniform() )
        hp_monster -= skade
        print(f"Scaredalot gjør {skade} skade med sverdet!")
    elif valg == "2":
        skade = int( 20 * uniform(0.5, 1) )
        hp_monster -= skade
        print(f"Scaredalot gjør {skade} skade med steinen!")
    
    print(f"Monsteret har nå {hp_monster} hp")
    if hp_monster <= 0:
        break
    
    valg_monster = randint(3)
    if valg_monster == 0:
        print("Monsteret brukte: flammer !")
        hp_scaredalot -= 30
    elif valg_monster == 1:
        print("Monsteret brukte: klør !")
        hp_scaredalot -= 10
    elif valg_monster == 2:
        print("Monsteret brukte: bit !")
        hp_scaredalot -= 20
    
    print(f"Scaredalot har nå {hp_scaredalot} hp")

print("\nSpillet er ferdig")
if hp_monster <= 0:
    print("Scaredalot vant over monsteret og redda jomfrua.")
else:
    print("Monsteret vant over Scaredalot.")