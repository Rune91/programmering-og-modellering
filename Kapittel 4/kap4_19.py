start_tt = int( input("Timer ved start: ") )
start_mm = int( input("Minutter ved start: ") )

if start_tt // 24 != 0 or start_mm // 60 != 0:
    print("Oppgitt tidspunkt er ugyldig")
else:
    print(f"Starttidspunktet er {start_tt}:{start_mm}")
    d_tt = int( input("Timer gått: ") )
    d_mm = int( input("Minutter gått: ") )
    
    ny_tt = ( start_tt + d_tt + (start_mm + d_mm)//60 ) % 24
    ny_mm = ( start_mm + d_mm ) % 60
    
    print(f"Nytt klokkeslett er {ny_tt}:{ny_mm}")