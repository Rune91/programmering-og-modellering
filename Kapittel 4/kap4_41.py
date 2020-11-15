start = 5
intervall = 2
tid = 24

# Matematisk løsning
dyr = start * 2**(tid//intervall)
print(f"Det er {dyr} tøffeldyr etter {tid} timer.")

# Iterativ løsning
dyr = start
for i in range(intervall, tid+1, intervall):
    dyr *= 2
print(f"Det er {dyr} tøffeldyr etter {tid} timer.")