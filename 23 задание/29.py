def f(x, end):
    if x > end: return 0
    if x == 10 or x == 15: return 0
    if x == end: return 1

    return f(x+1, end) + f(x+2, end) + f(x+3, end)

print(f(5, 11)*f(11,18))