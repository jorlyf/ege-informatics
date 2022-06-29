def F(n, r):
    if n == 0:
        return 2 * r
    else:
        return F(n // 10, r * 10 + n % 10)

for n in range(1, 10000000):
    if F(n, 0) == 628648:
        print(n)