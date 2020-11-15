p = float( input("p: ") )
q = float( input("q: ") )

if p + q == 1:
    print(
f"""
AA: {p**2:.3f}
Aa: {2*p*q:.3f}
aa: {q**2:.3f}
""")
else:
    print("Opggitte verdier for p + q er ikke lik 1.")