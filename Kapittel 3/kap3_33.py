from pylab import log10

def log_a(tall, a):
    return log10(tall) / log10(a)


a = int( input("Grunntall til logaritmen: ") )
tall = int( input("Regne logaritmen av: ") )

logaritme = log_a(tall, a)

print(f"Logaritmen (med grunntall {a}) av {tall} er {logaritme}")