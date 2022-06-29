P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {5, 10, 15, 20, 25, 30, 35, 40, 45}

A = {x for x in range(1000)}


def f(x):
    return ((x in A) <= (x in P)) and ((x in Q) <= (not (x in A)))


for x in range(1000):
    if not f(x):
        A.remove(x)

print(A)