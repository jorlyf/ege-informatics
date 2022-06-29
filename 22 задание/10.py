def f(a):
    R = 9
    L = 0
    while a >= R:
        L = L + 1
        a = a - R
    M = a
    if M < L:
        M = L
        L = a
    return (L, M)

for a in range(-19900, 1000):
    if f(a) == (2, 8):
        print(a)
        break