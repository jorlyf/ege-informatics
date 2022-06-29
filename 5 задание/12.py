def f(N):
    n = bin(N)[2:]

    n += str(n.count("1") % 2)
    n += str(n.count("1") % 2)

    return int(n, 2)

for N in range(1, 100):
    if f(N) > 77:
        print(N)
        break