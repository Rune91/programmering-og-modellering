leggetid = float( input("Når skal Kari legge seg? ") )

if leggetid % 1 != 0 or leggetid // 24 != 0:
    print("Oppgitt tidspunkt er ikke et heltall mellom 0 og 23")
elif leggetid < 14:
    print("Tidspunktet er for tidlig for å legge seg!")
else:
    morgen = (leggetid + 10) % 24
    if morgen <= 6:
        print("Kari rekker skolen dersom hun sover i 10 timer!")
    else:
        print("Kari rekker ikke skolen dersom hun sover i 10 timer!")