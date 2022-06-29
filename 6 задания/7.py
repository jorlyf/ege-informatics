def f(a):
    d = a
    n = 3
    s = 57
    while s <= 1200:
        s = s + d
        n = n + 4
    return n

for d in range(1, 10000):
    if f(d) == 63:
        print(d)