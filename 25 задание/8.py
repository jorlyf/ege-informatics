xList = [q for q in range(200_000, 900_000+1)]

def получить_простые_делители(x):
    простые_делители = set()
    решето = [0] * (x+1)

    for i in range(2, x+1):
        if not решето[i]:
            простые_делители.add(i)
            for j in range(i, x+1, i):
                решето[j] = 1

    return простые_делители

простые_делители = получить_простые_делители(900_000+1)

for x in xList:
    k = 0
    mx_pd = 0
    for pd in простые_делители:
        if pd > x: break
        if x % pd == 0:
            k += 1
            mx_pd = max(mx_pd, pd)
            if k > 7: break

    if k != 7: continue

    mx_d = 0
    d = 2
    while mx_d == 0 and d < int(x**1/2) + 5:
        if x % d == 0:
            mx_d = x // d
        d += 1

    print(mx_pd, mx_d)
