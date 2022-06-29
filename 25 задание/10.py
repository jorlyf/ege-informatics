for x in range(164_700, 164_753):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
        
    if len(d) == 6:
        d = sorted(d)
        a = (max(d))
        d.pop()
        b = (max(d))
        print(b, a)