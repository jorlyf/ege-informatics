def f(x, end, ln=0):
    if x == end:
        if ln % 2 != 0:
            return 1
        else:
            return 0
    if x > end: return 0

    if x == 1:
        return f(x+2, end, ln+1) + f(x+x, end, ln+1)
    return f(x+2, end, ln+1) + f(x+x, end, ln+1) + f(x*x, end, ln+1)

print( f(1, 100) )