def f(A, x, y):
    return (x < 40) or (y < 50) or ((3*x + 2*y) > A)

A = 0
while True:
    if all(f(A, x, y) for x in range(-100, 100) for y in range(-100, 100)):
        print(A)
    A += 1