from pylab import *

def K(t, K_0, a):
    return K_0 * e**(-a*t)

K_0 = 4.73 # mg/l
a = 0.65 # /s

x = linspace(0, 48, 100)
y = K(x, K_0, a)


title("Konsentrasjon av medisin i blodet")
xlabel("Tid [timer]")
ylabel("Konsentrasjon [mg/l]")
plot(x, y)