# Oppgave 4.23

from pylab import sqrt

print(" --------------")
print("| tall |  rot  |")
print(" --------------")


for i in range(100+1):
    print(f"| {i:4} | {sqrt(i):5.2f} |")
    i += 1
print(" --------------")



# Oppgave 4.30

bruker = "AzureDiamond"
passord = "hunter2"

for sjanse in range(3):
    bruker_in = input("Brukernavn: ")
    pass_in = input("Passord: ")
    if bruker_in == bruker and pass_in == passord:
        print(f"Velkommen tilbake, {bruker}.")
        break
    else:
        print(f"Feil brukernavn / passord. Du har {2-sjanse} forsøk igjen.")

        