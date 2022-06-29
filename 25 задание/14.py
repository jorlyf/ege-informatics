def getDividers(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)


cnt = 0
for x in range(800_000, 100000000):
    d = getDividers(x)
    if len(d) == 0: continue
    if (min(d) + max(d)) % 138 == 0:
        print(x, min(d) + max(d))
        cnt += 1
        if cnt == 5: break