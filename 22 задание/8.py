def f(x):
    M = 1; L = 0
    while x > 0:
        M = M * (x%10)
        if x % 10 > 5:
            L = L + 1
        x = x // 10
    return L, M

x = 0
while True:
    if f(x) == (0, 24):
        print(x)
        break
    x += 1