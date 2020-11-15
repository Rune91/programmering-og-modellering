penger = 5000   # kr
inn = 5         # prosent økning
ut = 10         # prosent reduksjon
tid_slutt = 20  # år

for tid in range(1, tid_slutt+1):
    penger *= (100+inn)/100
    
    # Ta bort neste linje for å svare på oppgave a)
    penger *= (100-ut)/100
    
    print(f"Etter {tid:2} år har Per {penger:.2f} kr på kontoen")