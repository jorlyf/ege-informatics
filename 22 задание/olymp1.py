def f(s):
    x = s
    a = 0
    b = 0
    while x > 0:
        a = a + 1
        b = b + (x % 10)
        x = x // 10
    return a, b

cnt = 0
for s in range(1, 10000000):
    if f(s) == (2, 12):
        cnt += 1
        print(s, cnt)