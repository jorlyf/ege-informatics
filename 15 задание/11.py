def f(x, q1, q2):
    return (q1 <= x <= q2) <= ( (300 <= x <= 500) and not (100 <= x <= 800) )

mnq1 = 0
mnq2 = 0

for q1 in range(1, 900):
    for q2 in range(q1+1, 900):
        if all( f(x, q1, q2) for x in range(1, 1000) ):
            if mnq1 + mnq2 > q1 + q2:
                mnq1 = q1; mnq2 = q2
            # print(q2-q1)

print(mnq1, mnq2)