bruker = "AzureDiamond"
passord = "hunter2"

sjanse = 1
while sjanse <= 3:
    bruker_in = input("Brukernavn: ")
    pass_in = input("Passord: ")
    if bruker_in == bruker and pass_in == passord:
        print(f"Velkommen tilbake, {bruker}.")
        break
    else:
        print(f"Feil brukernavn / passord. Du har {3-sjanse} forsøk igjen.")
        sjanse += 1
        