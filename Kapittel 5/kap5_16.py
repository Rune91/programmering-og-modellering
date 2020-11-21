from pylab import *

# Del 1
N = 100
liste = linspace(0, 1, N)
for element in liste:
    print(element)
    
# Del 2
liste1 = ["Liste", sum, "med", max, "funksjoner"]
liste2 = []
for element in liste1:
    liste2.append(element)

# Del 3
liste1 = [1,2,3,4,5,6,7]
liste2 = []
for element in liste1[2:6]:
    liste2.append(element)

# Del 4
liste1 = linspace(1, 10, 11)
liste2 = linspace(2, 11, 11)
for i in range(len(liste1)):
    for element in liste2:
        liste1[i] += element