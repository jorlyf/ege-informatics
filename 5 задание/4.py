def R(N):
    n = bin(N)[2:]

    n += str(n.count("1") % 2)
    n += str(n.count("1") % 2)

    return int(n, 2)

N = 1
while True:
    if R(N) > 181:
        print(N)
        break

    N += 1