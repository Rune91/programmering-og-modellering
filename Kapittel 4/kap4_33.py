# Del 1
print("Alle heltall fra og med 0 til og med 100")
for n in range(0, 100+1):
    print(n)

# Del 2
print("Alle heltall fra 50 til 75")
for n in range(50+1, 75):
    print(n)

# Del 3
print("Alle partall fra og med 0 til og med 100")
for n in range(0, 100+1):
    if n % 2 == 0:
        print(n)

# Del 4
print("Alle oddetall fra og med 0 til og med 100")
for n in range(0, 100+1):
    if n % 2 > 0:
        print(n)

# Del 5
print("Alle primtall til og med 100")
for n in range(2, 100+1):
    primtall = True
    for i in range(2, n):
        if n % i == 0:
            primtall = False
            break
    if primtall:
        print(n)