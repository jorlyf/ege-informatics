def f(x):
    a = 3*x + 23
    b = 3*x - 17

    while a != b:
        print(x, a, b)
        if a > b:
            a -= b
        else:
            b -= a
    return a

for x in range(6, 10000000):
    if f(x) == 10:
        print(x)
        break 