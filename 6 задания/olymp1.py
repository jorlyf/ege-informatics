def f(x):
    s = x
    n = 0
    while 2*s*s <= 10*s: # 50 < 50
        s = s + 1 # 5
        n = n + 2 # 6
    return n

x = -10000
while True:
    if f(x) == 8:
        print(x)
    x += 1