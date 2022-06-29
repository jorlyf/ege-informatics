def F(n):
    if n < 3:
        return n * 3
    if n % 2 == 0:
        return F(n-2) * F(n-1) - n
    else:
        return F(n-1) - F(n-2) + 2*n

print(F(30))