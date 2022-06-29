def f(N):
    n = bin(N)[2:]

    if int(n, 2) % 2 == 0:
        n += "1"
    else:
        n += "0"

    if int(n, 2) % 2 == 0:
        n += "1"
    else:
        n += "0"

    return int(n, 2)

for N in range(1, 1000000):
    a = f(N)
    if a < 171:
        print(N)