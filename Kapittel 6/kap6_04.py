from pylab import randint

N = 10000

kron = 0
for i in range(N):
    if randint(2) == 0:
        kron += 1
print(f"{N} myntkast ga kron {kron} ganger. Frekvens: {kron/N:.4f}")