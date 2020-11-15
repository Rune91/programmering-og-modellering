# Del 1, 2 og 3

aminosyrer = {
    "Alanin" :      ["GCU","GCC","GCA","GCG"],
    "Arginin" :     ["CGU","CGC","CGA","CGG","AGA","AGG"],
    "Asparagin" :   ["AAU","AAC"],
    "Asparginsyre" :["GAU","GAC"],
    "Cystein" :     ["UGU","UGC"],
    "Glutamin" :    ["CAA","CAG"],
    "Glutaminsyre" :["GAA","GAC"],
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
    print(f"Finner ingen aminosyre som hører til {antikodon}!")
    

#DNA = input("Skriv tre DNA-baser (T, G, C, A): ")
DNA = "TCC"
mRNA_kodon = DNA_til_mRNA(DNA)
mRNA_antikodon = oversette_kodon(mRNA_kodon)
aminosyre = finn_aminosyre(mRNA_antikodon)
print(f"Tilhørende aminosyre til DNA-basene {DNA} er {aminosyre}.")


# Del 4

def les_sekvens(sekvens):
    for i in range(0, len(sekvens), 3):
        DNA = sekvens[i:i+3]
        mRNA_kodon = DNA_til_mRNA(DNA)
        mRNA_antikodon = oversette_kodon(mRNA_kodon)
        aminosyre = finn_aminosyre(mRNA_antikodon)
        print(aminosyre)

sekvens = "atgggcgaac gacgggaatt gaacccgcga tggtgaattc acaatccact gccttaatcc".upper().replace(" ","")

print(f"\nAminosyrer i følgende DNA-sekvens:\n{sekvens}\n")
les_sekvens(sekvens)





































