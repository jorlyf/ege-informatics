a = (64**25 + 4**10) - (16**20 + 32**3)
def t(x, base):
    ost = ""
    while x > 0:
        ost = str(x%base) + ost
        x = x // base
    return ost

b = t(a, 4)
b = reversed(b)
b = "".join(b)
print(b.index("2"))