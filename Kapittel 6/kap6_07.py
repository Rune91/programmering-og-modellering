from pylab import randint

tall = []
while len(tall) < 5:
    t = randint(1, 1001)
    if t%7 == 0 and t%5 > 0:
        tall.append(t)

print(tall)