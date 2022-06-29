def f(x):
    a = 0
    b = 0
    while x > 1:
        a = a + 1
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3*x + 1
        if x > b:
            b = x
    return a, b

for x in range(1, 10000):
    if f(x) == (9, 256):
        print(x)
        break