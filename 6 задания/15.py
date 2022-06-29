for i in range(1, 1000000):
    s = i
    n = 5
    while s < 110:
        s = s + n
        n = n + 1
    if n == 15:
        print(i)