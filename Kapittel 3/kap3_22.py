# Alternativ 1 (mest ryddig)
def f(x):
    return 2*x
x = 12
x = x + 12
x = f(x)
print(x)


# Alternativ 2 (ikke gjør dette!)
def f(x_):
    global x
    x = 2*x_
x = 12
x = x + 12
f(x)
print(x)