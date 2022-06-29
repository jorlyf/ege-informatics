a = int("10110101", 2)
#b = int("С3", 16)
# a=11; b=12; c=13; d=14; e=15; f=15
b = 3 + 12 * 16

print(a, b)
c = (a+b) // 2

ost = ""
while c > 0:
    ost = str(c % 8) + ost
    c //= 8
print(ost)