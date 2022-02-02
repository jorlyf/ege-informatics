def f(n):
    if n == 0: return 0
    if n == 1: return 1
    if n == 2: return 3
    
    if (n % 2 == 0):
        return f(n - 2) + f(n / 2) + 1
    else:
        return f(n - 1) + f(n - 3)

print( f(35) )