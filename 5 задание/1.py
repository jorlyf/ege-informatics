def getR(N):
    aBin = [x for x in bin(N)]
    aBin.pop(0); aBin.pop(0)

    aBin.append(str(aBin.count("1") % 2))
    aBin.append(str(aBin.count("1") % 2))
    return int("".join(aBin), 2)

for n in range(1, 1000):
    if getR(n) > 176: print(n, getR(n)); break
