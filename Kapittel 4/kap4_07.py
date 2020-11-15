
datamaskin = input("Har du Windows eller Mac? ( W / M ) ")

if datamaskin == "W":
    mening = input("Har du også Windows Phone? ( J / N ) ")
    if mening == "J":
        print("Du har Windows PC og Windows Phone.")
    if mening == "N":
        print("Du har Windows PC men ikke Windows Phone.")
        
elif datamaskin == "M":
    mening = input("Har du også iPhone? (J / N ) ")
    if mening == "J":
        print("Du har Mac og iPhone.")
    elif mening == "N":
        print("Du har Mac men ikke iPhone.")
else:
    print("Ugyldig svar")
        