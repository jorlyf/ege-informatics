def f(a1, a2, x):
    return (170 <= x <= 580) <= \
    (((not (290 <= x <= 800)) and (not (a1 <= x <= a2))) \
    <= (not (170 <= x <= 580)))

mn = 100000
for a1 in range(160, 810):
    for a2 in range(a1+1, 810):
        if all( f(a1, a2, x) for x in range(160, 810) ):
            if a2 - a1 < mn:
                mn = a2 - a1

print(mn)