"""
+2; +3; +"1"
"""
def f(x, end):
    if x == end: return 1
    if x > end: return 0
    return f(x+2, end) + f(x+3, end) + f(x*10+1, end)

a = f(3, 12)
b = f(12, 25)
print(a*b)