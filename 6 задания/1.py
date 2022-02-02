for s in range(1, 1000):
    k = 3
    q = s
    while s < 1000:
        s = s * 2
        k = k + 7
    
    if k == 31: print(q); break