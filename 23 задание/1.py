def f(x, end):
    if x < end: return 0
    if x == end: return 1
    return f(x-8, end) + f(x//2, end)

a = f(102, 43)
b = f(43, 5)
print(a*b)

# 102 -> 5 с промежутком в 43
# +1; //2