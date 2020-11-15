verdi = 7500    # kroner
rente = 4       # prosent
tid = 10        # år

for t in range(0,tid+1):
    ny_verdi = verdi / (1+rente/100)**t
    print(f"{ny_verdi:.2f}")
    
# Kommentar: Formelen som vist i oppgaven beskriver renta r IKKE som
# en reduksjon i verdien til varen, men heller som en økning av
# sammenlignede verdier (inflasjon).
# Formel for r som direkte reduksjon i verdi vil være:
# P = 7500*(1-r)**t