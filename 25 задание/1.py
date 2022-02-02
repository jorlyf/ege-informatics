for x in range(150000, 200000+1):
    j = 2
    while j*j <= x:
        if (x % j == 0): break
        j = j + 1
    if (j*j <= x):
        mxDelitel = x//j
        q =  mxDelitel**(1/3)
        if round(q) ** 3 == mxDelitel:
            print(j, mxDelitel)
