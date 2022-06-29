def f(x, y):
    while x != y:
        if x + y < 1019: return 0
        if x > y:
            x -= y
        else:
            y -= x
    return x

cnt = 0
for x in range(1019, 100_000, 1019):
    for y in range(1019, 100_000, 1019):
        if f(x, y) == 1019:
            cnt += 1

print(cnt)