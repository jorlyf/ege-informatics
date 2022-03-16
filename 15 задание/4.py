def ДЕЛ(n, m):
    if (m == 0): return False
    return n % m == 0

def f(x, A):
    return (not (A > 30)) and ((ДЕЛ(x, 8) and (not ДЕЛ(x, A))) <= (not ДЕЛ(x, 10)))

A = -1000
while True:
    if all(f(x, A) for x in range(1, 1000)):
        print(A)
    A += 1
