def finn_stoerste_n(x):
    n = 0
    while 2**n <= x:
        n += 1
    return n-1

tall_ti = int(input(""))

n = finn_stoerste_n(tall_ti)

for i in range(n, 0-1, -1):
    if 2**i <= tall_ti:
        tall_ti -= 2**i
        print(1)
    else:
        pass
        print(0)