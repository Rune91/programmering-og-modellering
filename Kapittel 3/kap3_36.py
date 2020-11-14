from math import factorial

def utvalg(n, r):
    # Bruker binomialkoeffisienten til å regne hvor mange måter
    # r elever kan velges fra totalt n elever (uten rekkefølge)
    # https://en.wikipedia.org/wiki/Binomial_coefficient
    return int(factorial(n) / ( factorial(r) * factorial(n-r) ))

n = 10
r = 2

print( utvalg(n, r) )