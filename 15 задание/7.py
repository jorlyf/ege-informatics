def ДЕЛ(n, m):
    return n % m == 0

def f(A, x):
    return (ДЕЛ(x, 34) and (not ДЕЛ(x, 51))) <= ((not ДЕЛ(x, A)) or ДЕЛ(x, 51))

A = 1

while True:
    if all( f(A, x) for x in range(1, 1000000) ):
        print(A)
        break

    A += 1