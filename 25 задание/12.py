def getM(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    if len(d) == 0: return 0
    return min(d) + max(d)

cnt = 0
for x in range(700_000, 10000000):
    M = getM(x)

    if M % 10 == 8:
        print(x, M)
        cnt += 1
        if cnt == 5: break