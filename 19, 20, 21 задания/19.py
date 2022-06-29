def f(a, b, c, m, last=""):
    if a+b >= 100: return c%2 == m%2
    if c == m: return 0

    if last == "+1":
        h = [ f(a+2, b, c+1, m, "+2"), f(a+3, b, c+1, m, "+3"), f(a*2, b, c+1, m, "*2"),
              f(a, b+2, c+1, m, "+2"), f(a, b+3, c+1, m, "+3"), f(a, b*2, c+1, m, "*2") ]
    elif last == "+2":
        h = [ f(a+1, b, c+1, m, "+1"), f(a+3, b, c+1, m, "+3"), f(a*2, b, c+1, m, "*2"),
              f(a, b+1, c+1, m, "+1"), f(a, b+3, c+1, m, "+3"), f(a, b*2, c+1, m, "*2") ]
    elif last == "+3":
        h = [ f(a+1, b, c+1, m, "+1"), f(a+2, b, c+1, m, "+2"), f(a*2, b, c+1, m, "*2"),
              f(a, b+1, c+1, m, "+1"), f(a, b+2, c+1, m, "+2"), f(a, b*2, c+1, m, "*2") ]
    elif last == "*2":
        h = [ f(a+1, b, c+1, m, "+1"), f(a+2, b, c+1, m, "+2"), f(a+3, b, c+1, m, "+3"),
              f(a, b+1, c+1, m, "+1"), f(a, b+2, c+1, m, "+2"), f(a, b+3, c+1, m, "+3") ]
    else:
        h = [ f(a+1, b, c+1, m, "+1"), f(a+2, b, c+1, m, "+2"), f(a+3, b, c+1, m, "+3"), f(a*2, b, c+1, m, "*2"),
              f(a, b+1, c+1, m, "+1"), f(a, b+2, c+1, m, "+2"), f(a, b+3, c+1, m, "+3"), f(a, b*2, c+1, m, "*2") ]

    return any(h) if (c+1)%2 == m%2 else all(h)

a = 2
for b in range(1, 98):
    for m in range(1, 6):
        if f(a, b, 0, m):
            print(b, m)
            break