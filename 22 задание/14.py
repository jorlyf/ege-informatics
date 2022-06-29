def f(x):
    Q = 9
    L = 0
    while x >= Q:
        L = L + 1
        x = x - Q
    M = x
    if M < L:
        M = L
        L = x
    
    return L, M

for x in range(1, 1000000):
    if f(x) == (4, 5):
        print(x)