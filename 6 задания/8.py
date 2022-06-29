def f(s):
    k = 4
    while s <= 67:
        s = s + 7
        k = k * 2
    return k

s = -100
while True:
    if f(s) == 256:
        print(s)
        break
    s += 1