for i in range(-1000, 10000):
    s = i
    n = 1
    while s <= 70:
        s = s + 9
        n = n * 7
    if n == 343:
        print(i)