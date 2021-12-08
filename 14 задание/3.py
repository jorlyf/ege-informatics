a = int("1001001", 2)
b = int("57", 8)

def t(x, base):
    ost = ""
    while x > 0:
        ost = str(x%base) + ost
        x = x // base
    return ost

print(t(int((a+b)/2), 8))
# число между a и b найти