def f(s):
    x = s
    L = 0; M = 0
    while x > 0:
        M = M + 1
        if x % 4 > 1:
            L = L + 1
        x = x // 4
    return L, M

x = -1000
while True:
    if f(x) == (2, 4):
        print(x)
        break
    x += 1