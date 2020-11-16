from pylab import linspace, array, append

def fordelt(a, b, N, i):
    return a + i*(b-a)/(N-1)

a = 10
b = 15
N = 11

x1 = array([])
for i in range(11):
    x1 = append(x1, fordelt(a, b, N, i))

x2 = linspace(a, b, N)

print(x1)
print(x2)