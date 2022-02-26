def f(x):
    a = 0; b = 1
    while x > 0:
        a = a + 2
        b = b * (x % 1000)
        x = x // 1000
    return (a, b)

x = -1000
while True:
    if f(x) == (4, 13):
        print(x)
    x += 1