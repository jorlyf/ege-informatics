def f(x):
    s = x // 15
    n = 14
    while s < 285:
        if (s+n) % 9 == 0:
            s = s + 11
        n = n + 13

    return n

s = -10000
cnt = 0
while True:
    if f(s) == 118:
        cnt += 1
        print(cnt)
    s += 1