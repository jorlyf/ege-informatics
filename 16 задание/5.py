def F(n):
    if n == 1: return 1
    if n == 2: return 2
    if n > 2 and n % 3 == 0:
        return n + F(n-1) + F(n//3)
    if n > 2 and n % 3 != 0:
        return F(n-2) + F(n-3)

n = 1
while True:
    if F(n) > 2000:
        print(n)
        break
    n += 1