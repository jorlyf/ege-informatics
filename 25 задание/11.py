cnt = 0
def get(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    
    return d

for x in range(800_000, 10000000):
    d = get(x)

    sm = sum(d)
    pr = 1
    for q in d:
        pr = pr * q
    
    if sm % 2 != 0 and pr % 2 != 0:
        if len(d) > 10:
            print(x, len(d))