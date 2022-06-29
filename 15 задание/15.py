def f(a1, a2, x):
    return (170 <= x <= 540) <= (((370 <= x <= 830) and (not (a1 <= x <= a2))) <= (not (170 <= x <= 540)))

mn = 100000000
for a1 in range(160, 840):
    for a2 in range(a1 + 1, 840):
        if all( f(a1, a2, x) for x in range(160, 840) ):
            mn = min(mn, a2 - a1)

print(mn)