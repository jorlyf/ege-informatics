def f(N):
    n = ""
    while N > 0:
        n = str(N % 9) + n
        N = N // 9
    
    if n.count("5") == n.count("7"):
        n = n + str(n.count("5"))[-1]
    else:
        n = n + str(max([n.count(x) for x in "012345678"]))
    
    if n.count("5") == n.count("7"):
        n = n + str(n.count("5"))[-1]
    else:
        n = n + str(max([n.count(x) for x in "012345678"]))

    if n.count("5") == n.count("7"):
        n = n + str(n.count("5"))[-1]
    else:
        n = n + str(max([n.count(x) for x in "012345678"]))

    if n.count("5") == n.count("7"):
        n = n + str(n.count("5"))[-1]
    else:
        n = n + str(max([n.count(x) for x in "012345678"]))

    if n.count("5") == n.count("7"):
        n = n + str(n.count("5"))[-1]
    else:
        n = n + str(max([n.count(x) for x in "012345678"]))

    
    return hex(int(n, 9))[2:]

for N in range(1, 10000):
    n = f(N)
    if "bac" in n:
        print(N)