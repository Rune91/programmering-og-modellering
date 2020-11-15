start = 1000    # kroner
rente = 5       # prosent
slutt = 5000    # kroner

penger = start
i = 0
while penger < slutt:
    penger *= (rente+100)/100
    i += 1

print(f"Det tar {i} år før {start} kr med {rente}% rente blir til {slutt} kr.")