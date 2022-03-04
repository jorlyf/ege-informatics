def f(d):
    n = 8
    s = 78
    while s <= 1200:
        s = s + d
        n = n + 2
    return n

d = 1
while True:
    if f(d) == 46:
        print(d)
    d += 1