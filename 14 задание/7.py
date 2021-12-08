a = (5**300 * 15**100) - (25**50 + 125**100)
def t(x, base):
    ost = ""
    while x > 0:
        ost = str(x%base) + ost
        x //= base
    return ost

a = t(a, 5)
print(a)
sum = 0
for i in a:
    if i in "0123":
        sum += int(i)

print(sum)