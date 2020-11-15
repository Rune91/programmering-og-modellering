penger = 20
epler = 0

butikk = """
Du står inne på Rema 2000. Hele butikken er full av bare epler.
Hva vil du gjøre?
1    Kjøpe et eple
2    Gå ut
"""
gate = """
Du står ute på gata. 
1    Spise et eple
2    Gå inn på Rema 2000
3    Gå hjem
"""


rom = 1
while rom != 0:
    print("\n\n-------------------------------------------------")
    print(f"Du har {penger} kroner i lomma og {epler} eple(r) i posen.")
    if rom == 1:
        print(butikk)
        valg = input()
        if valg == "1":
            if penger >= 5:
                penger -= 5
                epler += 1
        if valg == "2":
            rom = 2
            
    elif rom == 2:
        print(gate)
        valg = input()
        if valg == "1":
            if epler > 0:
                print("Du spiser et eple. Nam.")
                epler -= 1
            else:
                print("Du har ingen epler å spise!")
        elif valg == "2":
            rom = 1
        elif valg == "3":
            rom = 0

print("Du går hjem etter en lang dag i byen.\nSlutt.")