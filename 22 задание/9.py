for i in range(1, 1000000):
    d = i
    c = 0; N = 0; T = d
    while N != 144:
        N = N + T
        T = T + d
        c = c + 1
        if c > 8: break
    if c % 2 != 0:
        c = c + 5
    
    if c == 8:
        print(i)