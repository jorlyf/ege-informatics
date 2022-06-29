def f(a, b, c, m):
    if a+b >= 211: return c%2 == m%2
    if c == m: return 0

    h = [f(a+1, b, c+1, m), f(a*2, b, c+1, m), f(a, b+1, c+1, m), f(a, b*2, c+1, m)]

    return any(h) if (c+1)%2 == m%2 else all(h)

a = 17
for b in range(1, 194):
    for m in range(1, 5):
        q = f(a, b, 0, m)
        if q:
            print(b, m)
            break