def f(s):
    n = 4
    while s <= 400:
        s = s + 5
        n = n + 8
    return n

for s in range(-1000, 10000):
    if f(s) > 1000:
        print(s)