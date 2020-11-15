n = 10

fib = 1
forrige = 1
for i in range(n):
    if i == 0 or i == 1:
        continue
    temp = fib
    fib += forrige
    forrige = temp

print(fib)