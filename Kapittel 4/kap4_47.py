from math import cos, pi

N = 100
x = pi

def fakultet(n):
    if n == 1: return 1
    return n * fakultet(n-1)

T_sum = 1
for n in range(1, N):
    T_sum += (-1)**n / fakultet(2*n) * x**(2*n)

print(f"cos(pi) iterativt: {T_sum:.4f}")
print(f"cos(pi) med math.cos: {cos(x):.4f}")