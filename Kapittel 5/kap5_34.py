from pylab import *

# Løsning 1
x = [0, 1, 1, 2, 2, 3]
y = [1, 1, 2, 2, 3, 3]

# Løsning 2
x_ = linspace(0, 3, 1000) [:-1]
y_ = x_ // 1

title("En trapp")
xlabel("x")
ylabel("y")
#plot(x, y)
plot(x_, y_)