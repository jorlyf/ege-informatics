for i in range(-1000, 1000):
    x = i
    a = 1
    b = a
    while a < x:
        c = a + b
        a = b
        b = c
    if b == 55:
        print(i)
        break