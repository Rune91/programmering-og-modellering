from pylab import sqrt

liste1 = []
for i in range(1, 101):
    liste1.append(i)

liste2 = [sqrt(n) for n in liste1]