def f(x):
    k = 50
    s = x
    while s + k > 55:
        s = s + 2
        k = k - 4
    return k

x = -100000
while True:
    if f(x) == 22:
        print(x)
    x += 1