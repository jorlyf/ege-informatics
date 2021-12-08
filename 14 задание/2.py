a = int("10110101", 2)
b = int("C3", 16)

def translate(x, base):
    ost = ""
    while x > 0:
        ost = str(x % base) + ost
        x = x // base
    return ost


c = (a+b) / 2
k = translate(int(c), 8)
print(k)
# найти середину между a и b