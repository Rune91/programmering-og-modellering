from pylab import *

def y_eple(y_forrige, p):
    if p <= 0.5:
        return y_forrige+1
    else:
        return y_forrige-1

def y_burger(y_forrige, p, p_forrige):
    if p >= p_forrige:
        return y_forrige + 1
    else:
        return y_forrige - 1

# Del 1 og 2
N = 60
aksjer_eple = [0]
aksjer_burger = [0]
p = uniform(0, 1, N)
for i in range(1, N):
    aksjer_eple.append( y_eple(aksjer_eple[i-1], p[i]) )
    aksjer_burger.append( y_burger(aksjer_burger[i-1], p[i], p[i-1]) )

# Del 3
plot(aksjer_eple)
plot(aksjer_burger)
legend(["Epler&Pærer AS", "Noens Burger AS"])
xlabel("Dager")
ylabel("Aksjeverdi")