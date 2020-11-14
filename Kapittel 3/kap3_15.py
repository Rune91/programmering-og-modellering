priser = {1: 16.00, 2: 25.00, 3: 20.50}
print(f"""
      1 Sur sild:       {priser[1]:.2f} kr/hg
      2 Melkesjokolade: {priser[2]:.2f} kr/hg
      3 Potetgull:      {priser[3]:.2f} kr/hg
      """)
valg = int( input("Hva vil du ha? (1 / 2 / 3) ") )
penger = float( input("Hvor mange kroner har du? ") )
vekt = penger / priser[valg]
print(f"Du har råd til {vekt:.2f} hg av godteriet.")