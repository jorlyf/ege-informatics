def f(s):
    k = 3
    while s <= 54:
        s = s + 7
        k = k * 2
    return k

s = -1000
while True:
    if f(s) == 96:
        print(s)

    s += 1