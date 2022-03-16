def F(n):
    if n <= 1: return n
    return F(n-1) + G(n-1)


def G(n):
    if n <= 2: return n
    return F(n) + G(n-1)

print(F(11))