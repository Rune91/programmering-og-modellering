from scipy.special import binom


a = float( input("a: ") )
b = float( input("b: ") )
n = int( input("n: ") )

def iterativ(a, b, n):
    totalt = 0
    for r in range(0, n+1):
        totalt += binom(n, r) * a**(n-r) * b**r
    return totalt

def analytisk(a, b, n):
    return (a+b)**n



res1 = iterativ(a, b, n)
res2 = analytisk(a, b, n)

print(f"({a}+{b})**{n} = {res1:.2f} = {res2:.2f}")