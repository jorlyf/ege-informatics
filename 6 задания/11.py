for i in range(1, 100000):
    s = i
    n = s // 10 + s % 6

    while n < s:
        n = n + 5
        s = s + 4
    
    if n == 1024:
        print(i)