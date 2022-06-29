def f(a, b, d, c, m):
    if a + b + d >= 73: return c%2 == m%2
    if c == m: return 0

    h = [
        f(a+3, b, d, c+1, m),
        f(a, b+13, d, c+1, m),
        f(a, b, d+23, c+1, m)
    ]

    return any(h) if (c+1)%2 == m%2 else all(h)

for s in range(1, 24):
    a = 2
    b = s
    d = 2*s

    for m in range(1, 6):
        if f(a, b, d, 0, m):
            print(s, m)
            break