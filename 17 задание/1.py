def u(x):
    return x % 11 == 0 and x % 2 != 0 and x % 5 != 0 and x % 17 != 0 and x % 33 != 0

diaposon = [x for x in range(1574, 9426+1) if u(x)]
print("sum =", sum(diaposon))

mx = 0
count = 0
for a in range(1574, 9426+1):
    if a not in diaposon:
        count += 1
        mx = max(mx, count)
    else: count = 0

print("mx count =", mx)