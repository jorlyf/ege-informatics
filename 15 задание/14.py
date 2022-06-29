def f(A, x, y):
    return (2*y + x != 70) or (x < y) or (A < x)

A = 0
while True:
    if all( f(A, x, y) for x in range(0, 100) for y in range(0, 100) ):
        print(A)
    A += 1