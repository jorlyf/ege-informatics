def f(A, x):
    return ((x & 30) != 4) or (((x & 35) == 1) <= ((x & A) == 0))

A = 1
while True:
    if all(f(A, x) for x in range(1, 100000)):
        print(A)
    A += 1