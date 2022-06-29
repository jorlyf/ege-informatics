def F(n):
    if n == 1: return 1
    if n % 2 != 0: return 3 * n + F(n - 2)
    if n % 2 == 0: return 4 * F(n // 2)

print(F(42))