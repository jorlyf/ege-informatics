def f(x):
    a = 0
    b = 0
    while x > 0:
        a = a + 1
        b = b + (x % 10)
        x = x // 10
    return a, b

cnt = 0
for x in range(-10000 , 500000):
    if f(x) == (2, 12):
        print(x)
        cnt += 1
print(cnt)