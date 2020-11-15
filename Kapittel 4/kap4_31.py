from pylab import log10

tall = int( input("Skriv et heltall: ") )


# Den enkle og teite løsningen

if "7" in str(tall):
    print(f"{tall} inneholder sifferet 7.")
else:
    print(f"{tall} inneholder ikke sifferet 7.")
    
    
# Den ordentlige løsningen

inneholder = False
plassering = 0
while plassering < log10(tall):
    siffer = ( tall // 10**plassering ) % 10
    
    # heltallsdivisjonen fjerner siffer fra tallet bakfra
    # 10**plassering bestemmer hvor mange siffer som går bort
    # % 10 fjerner delen av tallet som er delelig på 10, dvs
    # alt som ikke står på enerplassen i tallet    
    
    if siffer == 7:
        inneholder = True
        break
    plassering += 1
    
if inneholder:
    print(f"{tall} inneholder sifferet 7.")
else:
    print(f"{tall} inneholder ikke sifferet 7.")