def f(a1, a2, x):
    return ((254 <= x <= 800) and not (a1 <= x <= a2)) <= (410 <= x <= 823)

mn = 10000000000
for a1 in range(250, 830):
    for a2 in range(a1+1, 830):
        if all( f(a1, a2, x) for x in range(250, 830) ):
            if a1+a2 < mn:
                mn = a1 + a2
    

print(mn)