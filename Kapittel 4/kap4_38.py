tall = 12

# For-løkke
produkt = 1
for n in range(1, tall+1):
    produkt *= n
print(f"{tall}! = {produkt}")

# Rekursiv
def fakultet(n):
    if n == 1: return 1
    return n * fakultet(n-1)
print(f"{tall}! = {fakultet(tall)}")