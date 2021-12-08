A = 25**40 - 5**30 + 24

def translate(x, base):
    ost = ""
    while x > 0:
        ost = str(x % base) + ost
        x = x // base
    return ost

b = translate(A, 5)
print(b.count("4"))
# найти кол-во четверок в пятиричной системе числа A