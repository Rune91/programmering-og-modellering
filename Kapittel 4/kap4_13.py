while True:
    valg = input("""Hvilken konvertering vil du gjøre?
            1  Tommer   -> cm
            2  cm       -> tommer
    """)
    if valg == "1" or valg == "2":
        break
    
    print("Du har gjort et ugyldig valg.")

lengde_orig = float( input("Lengde: ") )

if valg == "1":
    lengde_konv = lengde_orig * 2.54
    print(f"{lengde_orig} tommer = {lengde_konv} cm")
elif valg == "2":
    lengde_konv = lengde_orig / 2.54
    print(f"{lengde_orig} cm = {lengde_konv} tommer")
    
    