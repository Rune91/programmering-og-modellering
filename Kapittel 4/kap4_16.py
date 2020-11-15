dx = float( input("Uskarphet i posisjonsmåling (m): ") )
dp = float( input("Uskarphet i bevegelsesmengde (kg*m/s): ") )

def uskarphet(dx, dp):
    h_bar = 1.055e-34 # [J*s = kg*m**2/s]
    return dx*dp >= h_bar / 2

if uskarphet(dx, dp):
    print("Verdiene er innenfor Heisenbergs uskarphetsrelasjon.")
else:
    print("Verdiene er utenfor Heisenbergs uskarphetsrelasjon.")
    