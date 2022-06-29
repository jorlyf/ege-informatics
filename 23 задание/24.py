def f(x, end, x2 = 0):
    if x == end and x2 == 1: return 1
    if x2 > 1: return 0
    if x == end: return 0
    if x > end: return 0

    return f(x+1, end, x2) + f(x+2, end, x2) + f(x*2, end, x2+1)

a = f(2, 12)
print(a)