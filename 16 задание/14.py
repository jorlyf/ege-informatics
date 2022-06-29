def F(n):
    if n < 2:
        return n
    if n % 2 == 0:
        return F(n//2) + 1
    else:
        return F(3*n + 1) + 1

cnt = 0
for n in range(1, 100_000+1):
    if F(n) == 16: cnt += 1

print(cnt)