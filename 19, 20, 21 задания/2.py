print("19 задание")
a = []
def f(x, y, p=0):
    if (x + y >= 45) and (p==2): return True
    if (x + y >= 45) or (p==2): return False

    if p % 2 == 1:
        return f(x+2, y, p+1) or f(x, y+2, p+1) or \
               f(x*3, y, p+1) or f(x, y*3, p+1)
    else:
        return f(x+2, y, p+1) and f(x, y+2, p+1) and \
               f(x*3, y, p+1) and f(x, y*3, p+1)

for k in range(1, 43+1):
    for s in range(1, 43+1):
        if f(k, s) and (k+s <= 43):
            a.append((k, s))

print(len(a))

print("20 задание")
a = []
def f(x, y, p=0):
    if (x + y >= 45) and (p==3): return True
    if (x + y >= 45) or (p==3): return False

    if p % 2 == 0:
        return f(x+2, y, p+1) or f(x, y+2, p+1) or \
               f(x*3, y, p+1) or f(x, y*3, p+1)
    else:
        return f(x+2, y, p+1) and f(x, y+2, p+1) and \
               f(x*3, y, p+1) and f(x, y*3, p+1)

for s in range(1, 43+1):
    if f(4, s) and (4+s <= 43):
        a.append(s)

print(a)

print("21 задание")
a = []
def f(x, y, p=0):
    if (x + y >= 45) and (p==2): return True
    if (x + y >= 45) and (p==4): return True
    if (x + y >= 45) or (p>=4): return False

    if p % 2 == 1:
        return f(x+2, y, p+1) or f(x, y+2, p+1) or \
               f(x*3, y, p+1) or f(x, y*3, p+1)
    else:
        return f(x+2, y, p+1) and f(x, y+2, p+1) and \
               f(x*3, y, p+1) and f(x, y*3, p+1)

for s in range(1, 43+1):
    if f(13, s) and (13+s <= 43):
        a.append(s)

print(a)

a = []
def f(x, y, p=0):
    if (x + y >= 45) and (p==2): return True
    if (x + y >= 45) or (p>=4): return False

    if p % 2 == 1:
        return f(x+2, y, p+1) or f(x, y+2, p+1) or \
               f(x*3, y, p+1) or f(x, y*3, p+1)
    else:
        return f(x+2, y, p+1) and f(x, y+2, p+1) and \
               f(x*3, y, p+1) and f(x, y*3, p+1)

for s in range(1, 43+1):
    if f(13, s) and (13+s <= 43):
        a.append(s)

print(a)