def f(x):
    a = 0
    b = 1
    while x > 0:
        if x % 2 != 0:
            a = a + x % 8
        else:
            b = b * (x % 8)

        x = x // 8
    
    return (a, b)

x = 1
while True:
    if f(x) == (6, 12):
        print(x)
        break
    x += 1