from pylab import uniform, pi, plot
# Obs! x**2 + y**2 <= 1 som gitt i oppgaven forutsetter
# at x- og y-verdiene ligger mellom -1 og 1

N = 1000
M = 0
for i in range(N):
    x = uniform(-1,1)
    y = uniform(-1,1)
    if x**2 + y**2 <= 1:
        #plot(x,y, "b.")
        M += 1

pi_ = M/N *4
avvik = abs(pi_-pi) / pi * 100
print(f"Tilnærmet pi: {pi_:5f}. Dette er et avvik på {avvik:4g}%")