def f(x, end, param = 0):
    if x > end: return 0
    if param > 3: return 0
    if x == end: return 1
    return f(x+2, end, param) + f(x*3, end, param+1) + f(x*5, end, param+1)

print(f(2, 200))