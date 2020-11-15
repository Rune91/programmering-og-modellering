from pylab import sqrt

print(" --------------")
print("| tall |  rot  |")
print(" --------------")

i = 0
while i <= 100:
    print(f"| {i:4} | {sqrt(i):5.2f} |")
    i += 1
print(" --------------")