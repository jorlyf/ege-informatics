for x in range(150000, 200000+1):
    j = 2

    for j in range(2, round(x**(0.5))+1):
        if (x % j == 0):
            if (j*j <= x):
                maxd = x//j
                q =  maxd**(1/3)
                if round(q) ** 3 == maxd:
                    print(j, maxd)
            break

    # while j*j <= x:
    #     if (x % j == 0): break
    #     j = j + 1

    # if (j*j <= x):
    #     maxd = x//j
    #     q =  maxd**(1/3)
    #     if round(q) ** 3 == maxd:
    #         print(j, maxd)
