# Program 1
# Feilene er at funksjonen bruker radianer
# og at den ikke er importert
from pylab import sin, pi
a = sin(30 * 2*pi / 360)
print("Sinus av 30 grader = ", a)

# Program 2
# Feilene er at prisene er oppgitt med "kr"
# og at totalpris er stavet på ulike måter
pris_kaffe = 45
pris_te = 40
total_pris = 3*pris_kaffe + 4*pris_te
print("Total pris: ", total_pris)

#Program 3
# Feilene er at tallene ikke tas inn som integers og
# at c = a * b kommer før a og b er definert
a = int( input("Skriv inn en verdi for a: ") )
b = int( input("Skriv inn en verdi for b: ") )
c = a * b
print(c)