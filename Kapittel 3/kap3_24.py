def karv(H_maks, H_hvile, p):
    return (H_maks-H_hvile) * p/100 + H_hvile

def maks_puls(alder):
    return 220 - alder


alder = 20      # år
intensitet = 60 # %
hvilepuls = 70  # slag per min

print( karv(maks_puls(alder), hvilepuls, intensitet) )