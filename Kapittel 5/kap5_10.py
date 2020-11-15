liste1 = [0.1, 2, 3.4, 9, 1, 2.2, 2.3, 0.1, 9]
liste2 = [1, 2, 3, 4.5, 4.5, 2.1, 1.7, 8, 8]

liste3 = []
for i in liste1:
    n = 0
    for j in liste2:
        n += j
    liste3.append(i * n)