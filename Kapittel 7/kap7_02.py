def derivert(f, x):
    dx = 1e-10
    fder = (f(x+dx)-f(x))/dx
    print(fder)
    return;