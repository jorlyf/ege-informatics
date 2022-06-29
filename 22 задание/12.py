def f(x):
    M, L, t = 0, 1, 0

    for i in range(x - 1):
        t = M + L
        M = L
        L = t

    return L

for x in range(1, 100):
    if f(x) == 1134903170:
        print(x)