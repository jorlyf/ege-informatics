for s in range(1, 1000):
    q = s
    k = 3
    while s < 1000:
        s = s * 2
        k = k + 7
    
    if k == 31: print(q); break