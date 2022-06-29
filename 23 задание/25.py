def f(x, end):
    if x == end: return 1
    if x > end: return 0

    return f(x+1, end) + f(x*2, end) + f(x*x, end)

print(f(5, 154))