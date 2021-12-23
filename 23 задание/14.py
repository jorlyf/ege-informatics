"""
+1; + число десятков на единицу, если десяток не равен 9
"""
def f(x, end):
    if x == end: return 1
    if x > end: return 0
    
    a = f(x+1, end)
    if (str(x)[-2] == "9"): b = f(x, end)
    else: b = f(x+10, end)
    return a+b

print(f(10, 33))