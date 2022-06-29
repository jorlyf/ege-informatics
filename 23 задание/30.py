from functools import lru_cache


pow2 = [2**x for x in range(1, 16)]
prim = []
for i in range(2, 10000):
    k = False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            k = True
            break
    if not k:
        prim.append(i)


def f(x, end):
    if x == end: return 1
    if x > end: return 0
    if x == 3 or x == 14: return 0

    if x % 10 == 0:
        return f(x + min([a for a in prim if a > x]), end) + f(x + min([a for a in pow2 if a > x]), end)
    else:
        return f(x + min([a for a in prim if a > x]), end) + f(x + min([a for a in pow2 if a > x]), end) + f(x + x%10, end)

print( f(2, 1024)*f(1024, 3072) )
