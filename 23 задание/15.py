"""
4 -> 24, где предпоследняя команда = 1
"""
def f(x, end):
    if x == end: return 1
    if x > end: return 0
    return f(x+1, end) + f(x*2, end)

a = (f(4, 24-2))
b = (f(4, 24/2-1))
print(a+b)