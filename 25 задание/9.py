def M(x):
    delitels = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            delitels.add(i)
            delitels.add(x//i)

    if len(delitels) == 0: return 0
    return min(delitels) + max(delitels)

cnt = 0
for x in range(220_001, 300_000):
    m = M(x)
    if m % 10 == 4:
        print(x, m)
        cnt += 1
    if cnt == 5: break