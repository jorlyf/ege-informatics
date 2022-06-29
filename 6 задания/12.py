for i in range(-1000, 100):
    s = i
    s = (s + 13) * 10
    n = 512
    while s < 0: # 6 раз
        n = n // 2
        s = s + n
        if n < 8: break
    if n == 8: print(i)