def F(n):
    if n <= 3: return n
    if n <= 32: return n // 4 + F(n-3)
    return 2 * F(n-5)

print(F(100))