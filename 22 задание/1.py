for x in range(1, 10000):
    q = x
    M = 1; L = 0
    while x > 0:
        M = M * (x % 10)
        if x % 10 > 3:
            L = L + 1
        x = x // 10
    
    if L == 1 and M == 60:
        print(q)
        break