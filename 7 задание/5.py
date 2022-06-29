V = 4 * 2**23
u = 2**18
Vzip = V / 2
Tzip = 20 + 5

T1 = V / u
T2 = (Vzip / u) + Tzip

print(T1)
print(T2)

print(T1 - T2)
# Б39