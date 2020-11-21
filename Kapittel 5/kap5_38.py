aminosyrer = {
    "Alanin" :      ["GCU","GCC","GCA","GCG"],
    "Arginin" :     ["CGU","CGC","CGA","CGG","AGA","AGG"],
    "Asparagin" :   ["AAU","AAC"],
    "Asparginsyre" :["GAU","GAC"],
    "Cystein" :     ["UGU","UGC"],
    "Glutamin" :    ["CAA","CAG"],
    "Glutaminsyre" :["GAA","GAG"],
    "Glycin" :      ["GGU","GGC","GGA","GGG"],
    "Histidin" :    ["CAU","CAC"],
    "Isoleucin" :   ["AUU","AUC","AUA"],
    "Leucin" :      ["CUU","CUC","CUA","CUG","UUA","UUG"],
    "Lysin" :       ["AAA","AAG"],
    "Phenylalanin": ["UUU","UUC"],
    "Prolin" :      ["CCU","CCC","CCA","CCG"],
    "Serin" :       ["UCU","UCC","UCA","UCG","AGU","AGC"],
    "Threonin" :    ["ACU","ACC","ACA","ACG"],
    "Tryptophan" :  ["UGG"],
    "Tyrosin" :     ["UAU","UAC"],
    "Valin" :       ["GUU","GUC","GUA","GUG"],
    "START" :       ["AUG"],
    "STOPP" :       ["UAA","UGA","UAG"]
    }


def DNA_til_mRNA(dna):
    return dna.replace("T", "U")

def oversette_kodon(kodon):
    antikodon = ""
    for base in kodon:
        if base == "A": antikodon += "U"
        if base == "U": antikodon += "A"
        if base == "C": antikodon += "G"
        if base == "G": antikodon += "C"
    return antikodon

def finn_aminosyre(antikodon):
    for key in aminosyrer:
        if antikodon in aminosyrer[key]:
            return key

def les_sekvens(sekvens):
    proteiner = []
    p = []
    for i in range(0, len(sekvens), 3):
        DNA = sekvens[i:i+3]
        mRNA_kodon = DNA_til_mRNA(DNA)
        mRNA_antikodon = oversette_kodon(mRNA_kodon)
        aminosyre = finn_aminosyre(mRNA_antikodon)
        if aminosyre == "STOPP":
            proteiner.append(p)
            p = []
        else:
            p.append(aminosyre)
        #print(aminosyre)
    return proteiner
        

filnavn = "kap5_38_data.txt"
# filen inneholder DNA-sekvensen til en gjær-mitokondrie
# https://www.ncbi.nlm.nih.gov/nuccore/AF437291

fil = open(filnavn, "r")
data = fil.read().replace("\n", "")
fil.close()


proteiner = les_sekvens(data)
proteiner = [p for p in proteiner if len(p) > 0]

print(f"DNA-sekvensen inneholder {len(proteiner)} proteiner.")
print("Se aminosyresammensetningen til protein nummer i med kommandoen proteiner[i]")