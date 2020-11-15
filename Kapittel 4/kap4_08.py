
land = input("Bor du i eller utenfor Norge? ( I / U )")

if land == "I":
    region = input("Bor du i nord- eller sørnorge? ( N / S ) ")
    
    if region == "N":
        preferanse = input("Liker du snø? ( J / N ) ")
        
        if preferanse == "J":
            print("Uffda.")
        
        elif preferanse == "N":
            print("Perfekt match.")
    
    elif region == "S":
        preferanse = input("Liker du regn? ( J / N ) ")
        
        if preferanse == "J":
            print("Perfekt match.")
        
        elif preferanse == "N":
            print("Uffda.")

elif land == "U":
    antarktis = input("Bor du i eller utenfor antarktisk? ( I / U ) ")
    
    if antarktis == "I":
        dyr = input("Er du en pingvin? ( J / N ) ")
        
        if dyr == "J":
            mat = input("Spiser du fisk? (J / N ) ")
            
            if mat == "J":
                print("Flink pingvin.")
                
            elif mat == "N":
                print("Blir vel ikke så mett på snø.")
                
        elif dyr == "N":
            jobb = input("Er du en forsker? ( J / N ) ")
            
            if jobb == "J":
                print("Stå på!")
                
            elif jobb == "N":
                print("Da bør du komme deg hjem.")
    
    elif antarktis == "U":
        ferie = input("Vil du på ferie til antarktis? ( J / N ) ")
        
        if ferie == "J":
            print("Husk å ta med fisk til pingvinene.")
            
        elif ferie == "N":
            print("Kanskje neste år, da.")