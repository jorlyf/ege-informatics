def f(A, x, y):
    return (2*y + 3*x != 135) or (y > A) or (x > A)

A = 0
while True:
    if all(f(A, x, y) for x in range(1, 100) for y in range(1, 100)):
        print(A)
    A += 1