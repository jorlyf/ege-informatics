print("19 задание")
def f(x, y, p=0):
    if (x+y >= 41) and (p == 2): return True
    if (x+y >= 41) or (p == 2): return False
    
    return f(x+1, y+2, p+1) or f(x+2, y+1, p+1) \
        or f(x*2, y, p+1) or f(x, y*2, p+1)

for s in range(1, 32+1):
    if f(8, s): # перебор второй кучи
        print(s)
        break

print("20 задание")
a = []
def f(x, y, p=0):
    if (x+y >= 41) and (p == 3): return True
    if (x+y >= 41) or (p == 3): return False
    
    if p % 2 == 0:
        return f(x+1, y+2, p+1) or f(x+2, y+1, p+1) \
            or f(x*2, y, p+1) or f(x, y*2, p+1)
    
    else:
        return f(x+1, y+2, p+1) and f(x+2, y+1, p+1) \
            and f(x*2, y, p+1) and f(x, y*2, p+1)


for s in range(1, 32+1):
    if f(8, s): # перебор второй кучи
        a.append(s)
print(max(a))
