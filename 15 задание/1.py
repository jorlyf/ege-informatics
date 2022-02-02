def de(n, m):
    return n % m == 0

def c(x, A):
    return (not de(x, A)) <= (de(x, 16) <= (not de(x, 12))) and (A < 40)

def f(A):
    if all( c(x, A) for x in range(1, 10000) ):
        print(A)

for A in range(1, 1000):
    f(A)
