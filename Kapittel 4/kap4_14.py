def g(x):
    return 3*x**4 + 5*x**3 + 7*x**2 + x - 3.0625

x = float( input("x = ") )

if g(x) == 0:
    print(f"(x - {x}) er en faktor i g.")
else:
    print(f"(x - {x}) er ikke en faktor i g.")