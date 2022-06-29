def f(x, end):
    if x == end: return 1
    if x > end: return 0
    if x == 30: return 0

    return f(x+1, end) + f(x*3, end) + f(x*4, end)

print( f(2, 15)*f(15, 100) )