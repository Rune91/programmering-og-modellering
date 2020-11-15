from pylab import sin, pi

print(" ------------------------")
print("| Grader | Sinus(vinkel) |")
print(" ------------------------")

i = 0
while i <= 180:
    sin_verdi = sin( i/360*2*pi )
    print(f"| {i:^6} | {sin_verdi:^13.3f} |")
    i += 10
print(" ------------------------")