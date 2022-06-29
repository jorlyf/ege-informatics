def f(x):
    S = 5
    while x > 0:
        if x % 8 > 4:
            S = S + (x % 8)
        else:
            S = S * (x % 8)
        x = x // 8
    return S

for x in range(-100, 10000):
    s = f(x)
    if s > 0 and s % 100 == 0:
        print(x, s)
        break