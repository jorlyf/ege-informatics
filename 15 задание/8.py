def f(A, x):
    return (((x&A) == 0) and ((x&36) == 0)) <= ((x&46) == 0)

A = 1
while True:
    if all( f(A, x) for x in range(1, 100) ):
        print(A)
        break
    A += 1