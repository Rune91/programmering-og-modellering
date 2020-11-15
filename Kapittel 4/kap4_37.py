m = int(input(""))
s = 0
for n in range(1, m+1):
    s = s + n
print(s)
print(f"Analytisk løsning: {m*(m+1)/2:.0f}\nSer likt ut!")